from rest_framework import serializers
from .models import User, SpamReport

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


# class SpamReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SpamReport
#         fields = ['id', 'reported_by', 'phone_number', 'is_spam']

class SpamReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpamReport
        fields = ['id', 'phone_number', 'is_spam', 'reported_by']
        read_only_fields = ['reported_by']


class SearchResultSerializer(serializers.ModelSerializer):
    spam_likelihood = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['username', 'phone_number', 'spam_likelihood']

    def get_spam_likelihood(self, obj):
        reports = SpamReport.objects.filter(phone_number=obj.phone_number)
        return reports.count()
