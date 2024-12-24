from django.contrib import admin
from .models import User, SpamReport

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email', 'phone_number']

@admin.register(SpamReport)
class SpamReportAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'reported_by', 'is_spam']
    search_fields = ['phone_number']
