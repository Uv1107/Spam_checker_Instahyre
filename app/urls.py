from django.urls import path
from .views import RegisterView, LoginView, SpamReportView, SearchView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('report-spam/', SpamReportView.as_view(), name='report_spam'),
    path('search/', SearchView.as_view(), name='search'),
]
