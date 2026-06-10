from django.contrib import admin
from .models import Contact, Enquiry, Equipment, Plan, Member, UserProfile


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'emailid', 'contact', 'subject', 'msgdate', 'isread')
    list_filter = ('isread', 'msgdate')
    search_fields = ('name', 'emailid', 'subject')


@admin.register(Enquiry)
class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'mobile', 'email', 'age', 'gender')
    search_fields = ('name', 'email')


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'unit', 'purchasedate')
    search_fields = ('name',)


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'duration')
    search_fields = ('name',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'email', 'gender', 'plan', 'joindate', 'initamount')
    list_filter = ('gender', 'plan')
    search_fields = ('name', 'email')


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'date_of_birth', 'gender')
    search_fields = ('user__username', 'phone')
