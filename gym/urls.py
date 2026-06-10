from django.urls import path
from gym import views

app_name = 'gym'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('gym/', views.gym_page, name='gym_page'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('classes/', views.classes_page, name='classes'),
    path('contact/', views.contact, name='contact'),

    path('register/', views.register, name='register'),
    path('user-login/', views.user_login, name='user_login'),
    path('user-logout/', views.user_logout, name='user_logout'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('user-profile/', views.user_profile, name='user_profile'),
    path('subscribe-plan/<int:pid>/', views.subscribe_plan, name='subscribe_plan'),

    path('admin-login/', views.admin_login, name='admin_login'),
    path('admin-home/', views.admin_home, name='admin_home'),
    path('change-password/', views.changePassword, name='changePassword'),
    path('logout/', views.Logout, name='logout'),

    path('add-enquiry/', views.addEnquiry, name='addEnquiry'),
    path('view-enquiry/', views.viewEnquiry, name='viewEnquiry'),
    path('edit-enquiry/<int:pid>/', views.edit_Enquiry, name='edit_Enquiry'),
    path('delete-enquiry/<int:pid>/', views.delete_Enquiry, name='delete_Enquiry'),

    path('add-plan/', views.addPlan, name='addPlan'),
    path('view-plan/', views.viewPlan, name='viewPlan'),
    path('edit-plan/<int:pid>/', views.edit_Plan, name='edit_Plan'),
    path('delete-plan/<int:pid>/', views.delete_Plan, name='delete_Plan'),

    path('add-equipment/', views.addEquipment, name='addEquipment'),
    path('view-equipment/', views.viewEquipment, name='viewEquipment'),
    path('edit-equipment/<int:pid>/', views.edit_Equipment, name='edit_Equipment'),
    path('delete-equipment/<int:pid>/', views.delete_Equipment, name='delete_Equipment'),

    path('add-member/', views.addMember, name='addMember'),
    path('view-member/', views.viewMember, name='viewMember'),
    path('edit-member/<int:pid>/', views.edit_Member, name='edit_Member'),
    path('delete-member/<int:pid>/', views.delete_Member, name='delete_Member'),

    path('admin-users/', views.viewUsers, name='viewUsers'),
    path('admin-edit-user/<int:pid>/', views.edit_User, name='edit_User'),
    path('admin-delete-user/<int:pid>/', views.delete_User, name='delete_User'),

    path('unread-queries/', views.unread_queries, name='unread_queries'),
    path('read-queries/', views.read_queries, name='read_queries'),
    path('view-queries/<int:pid>/', views.view_queries, name='view_queries'),
    path('delete-contact/<int:pid>/', views.delete_contact, name='delete_contact'),
]
