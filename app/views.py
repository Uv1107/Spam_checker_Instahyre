from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q

from .models import User, SpamReport
from .serializers import UserSerializer, SpamReportSerializer, SearchResultSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token)
            })
        return Response({"error": "Invalid credentials"}, status=400)




class SpamReportView(generics.CreateAPIView):
    serializer_class = SpamReportSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(reported_by=self.request.user)



class SearchView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        query = request.query_params.get('query')
        search_type = request.query_params.get('type')

        if search_type == 'name':
            users = User.objects.filter(
                Q(username__istartswith=query) | Q(username__icontains=query)
            )
        elif search_type == 'phone':
            users = User.objects.filter(phone_number=query)
        else:
            return Response({"error": "Invalid search type"}, status=400)

        serializer = SearchResultSerializer(users, many=True)
        return Response(serializer.data)
