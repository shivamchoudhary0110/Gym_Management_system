import os
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from datetime import date, datetime

from .models import Contact, Enquiry, Equipment, Plan, Member, UserProfile
from .forms import (
    ContactForm, EnquiryForm, PlanForm, EquipmentForm, MemberForm, MemberEditForm,
    ChangePasswordForm, UserRegistrationForm, UserProfileForm, UserLoginForm
)


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def gym_page(request):
    return render(request, 'gym.html')


def testimonials(request):
    return render(request, 'testimonials.html')


def classes_page(request):
    return render(request, 'classes.html')


def contact(request):
    error = ""
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                contact_obj = form.save(commit=False)
                contact_obj.msgdate = date.today()
                contact_obj.isread = "no"
                contact_obj.save()
                error = "no"
            except Exception:
                error = "yes"
        else:
            error = "yes"
    else:
        form = ContactForm()
    context = {
        'form': form,
        'error': error,
        'EMAILJS_SERVICE_ID': os.environ.get('EMAILJS_SERVICE_ID', ''),
        'EMAILJS_TEMPLATE_ID': os.environ.get('EMAILJS_TEMPLATE_ID', ''),
        'EMAILJS_PUBLIC_KEY': os.environ.get('EMAILJS_PUBLIC_KEY', ''),
    }
    return render(request, 'contact.html', context)


def register(request):
    error = ""
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
                UserProfile.objects.create(
                    user=user,
                    phone=request.POST.get('phone', ''),
                    date_of_birth=request.POST.get('date_of_birth') or None,
                    gender=request.POST.get('gender', ''),
                )
                login(request, user)
                return redirect('gym:user_dashboard')
            except Exception:
                error = "yes"
        else:
            error = "yes"
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form, 'error': error})


def user_login(request):
    error = ""
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                login(request, user)
                if user.is_staff:
                    return redirect('gym:admin_home')
                return redirect('gym:user_dashboard')
            else:
                error = "yes"
        else:
            error = "yes"
    else:
        form = UserLoginForm()
    return render(request, 'user_login.html', {'error': error})


@login_required
def user_dashboard(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    members = Member.objects.filter(user=request.user).select_related('plan')
    active_member = members.filter(plan__isnull=False).order_by('-joindate').first()
    context = {
        'profile': profile,
        'plans': Plan.objects.all(),
        'members': members,
        'active_member': active_member,
    }
    return render(request, 'user_dashboard.html', context)


@login_required
def subscribe_plan(request, pid):
    plan = get_object_or_404(Plan, id=pid)
    profile, _ = UserProfile.objects.get_or_create(user=request.user)
    existing = Member.objects.filter(user=request.user, plan=plan).first()
    if not existing:
        Member.objects.create(
            user=request.user,
            name=request.user.get_full_name() or request.user.username,
            contact=profile.phone or '',
            email=request.user.email,
            gender=profile.gender or '',
            plan=plan,
            joindate=date.today(),
            initamount=plan.amount,
        )
    return redirect('gym:user_dashboard')


@login_required
def user_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            if request.POST.get('first_name'):
                request.user.first_name = request.POST['first_name']
            if request.POST.get('last_name'):
                request.user.last_name = request.POST['last_name']
            if request.POST.get('email'):
                request.user.email = request.POST['email']
            request.user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('gym:user_profile')
    else:
        form = UserProfileForm(instance=profile)
    return render(request, 'user_profile.html', {'form': form, 'profile': profile})


def user_logout(request):
    logout(request)
    return redirect('gym:index')


def admin_login(request):
    return redirect('gym:user_login')


@login_required
def admin_home(request):
    if not request.user.is_staff:
        return redirect('gym:index')
    context = {
        'en': Enquiry.objects.count(),
        'eq': Equipment.objects.count(),
        'p': Plan.objects.count(),
        'm': Member.objects.count(),
        'u': User.objects.count(),
        'recent_enquiries': Enquiry.objects.all().order_by('-id')[:5],
        'recent_members': Member.objects.select_related('plan', 'user').order_by('-id')[:5],
        'recent_users': User.objects.order_by('-date_joined')[:5],
    }
    return render(request, 'admin_home.html', context)


@login_required
def changePassword(request):
    error = ""
    if request.method == "POST":
        form = ChangePasswordForm(request.POST)
        if form.is_valid():
            user = request.user
            if user.check_password(form.cleaned_data['oldpassword']):
                user.set_password(form.cleaned_data['newpassword'])
                user.save()
                error = "no"
            else:
                error = "not"
    else:
        form = ChangePasswordForm()
    return render(request, 'changePassword.html', {'form': form, 'error': error})


@login_required
def Logout(request):
    logout(request)
    return redirect('gym:index')


@login_required
def addEnquiry(request):
    error = ""
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = EnquiryForm()
    return render(request, 'addEnquiry.html', {'form': form, 'error': error})


@login_required
def viewEnquiry(request):
    enquiry = Enquiry.objects.all()
    return render(request, 'viewEnquiry.html', {'enquiry': enquiry})


@login_required
def edit_Enquiry(request, pid):
    error = ""
    enquiry = get_object_or_404(Enquiry, id=pid)
    if request.method == "POST":
        form = EnquiryForm(request.POST, instance=enquiry)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = EnquiryForm(instance=enquiry)
    return render(request, 'edit_Enquiry.html', {'form': form, 'enquiry': enquiry, 'error': error})


@login_required
def delete_Enquiry(request, pid):
    if request.method == "POST":
        enquiry = get_object_or_404(Enquiry, id=pid)
        enquiry.delete()
    return redirect('gym:viewEnquiry')


@login_required
def addPlan(request):
    error = ""
    if request.method == "POST":
        form = PlanForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = PlanForm()
    return render(request, 'addPlan.html', {'form': form, 'error': error})


@login_required
def viewPlan(request):
    plan = Plan.objects.all()
    return render(request, 'viewPlan.html', {'plan': plan})


@login_required
def edit_Plan(request, pid):
    error = ""
    plan = get_object_or_404(Plan, id=pid)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=plan)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = PlanForm(instance=plan)
    return render(request, 'edit_Plan.html', {'form': form, 'plan': plan, 'error': error})


@login_required
def delete_Plan(request, pid):
    if request.method == "POST":
        plan = get_object_or_404(Plan, id=pid)
        plan.delete()
    return redirect('gym:viewPlan')


@login_required
def addEquipment(request):
    error = ""
    if request.method == "POST":
        form = EquipmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = EquipmentForm()
    return render(request, 'addEquipment.html', {'form': form, 'error': error})


@login_required
def viewEquipment(request):
    equipment = Equipment.objects.all()
    return render(request, 'viewEquipment.html', {'equipment': equipment})


@login_required
def edit_Equipment(request, pid):
    error = ""
    equipment = get_object_or_404(Equipment, id=pid)
    if request.method == "POST":
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = EquipmentForm(instance=equipment)
    return render(request, 'edit_Equipment.html', {'form': form, 'equipment': equipment, 'error': error})


@login_required
def delete_Equipment(request, pid):
    if request.method == "POST":
        equipment = get_object_or_404(Equipment, id=pid)
        equipment.delete()
    return redirect('gym:viewEquipment')


@login_required
def addMember(request):
    error = ""
    plan_list = Plan.objects.all()
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = MemberForm()
    return render(request, 'addMember.html', {'form': form, 'plan': plan_list, 'error': error})


@login_required
def viewMember(request):
    member = Member.objects.select_related('plan', 'user').all()
    return render(request, 'viewMember.html', {'member': member})


@login_required
def edit_Member(request, pid):
    error = ""
    member = get_object_or_404(Member, id=pid)
    if request.method == "POST":
        form = MemberEditForm(request.POST, instance=member)
        if form.is_valid():
            try:
                form.save()
                error = "no"
            except Exception:
                error = "yes"
    else:
        form = MemberEditForm(instance=member)
    return render(request, 'edit_Member.html', {'form': form, 'member': member, 'error': error})


@login_required
def delete_Member(request, pid):
    if request.method == "POST":
        member = get_object_or_404(Member, id=pid)
        member.delete()
    return redirect('gym:viewMember')


@login_required
def viewUsers(request):
    users = User.objects.all().order_by('-date_joined')
    user_profiles = {}
    for up in UserProfile.objects.all():
        user_profiles[up.user_id] = up
    return render(request, 'viewUsers.html', {'users': users, 'user_profiles': user_profiles})


@login_required
def edit_User(request, pid):
    error = ""
    target_user = get_object_or_404(User, id=pid)
    profile, _ = UserProfile.objects.get_or_create(user=target_user)
    if request.method == "POST":
        target_user.first_name = request.POST.get('first_name', '')
        target_user.last_name = request.POST.get('last_name', '')
        target_user.email = request.POST.get('email', '')
        target_user.is_staff = request.POST.get('is_staff') == 'on'
        target_user.is_superuser = request.POST.get('is_superuser') == 'on'
        target_user.save()
        profile.phone = request.POST.get('phone', '')
        dob = request.POST.get('date_of_birth')
        profile.date_of_birth = dob if dob else None
        profile.gender = request.POST.get('gender', '')
        profile.save()
        error = "no"
    return render(request, 'edit_User.html', {'target_user': target_user, 'profile': profile, 'error': error})


@login_required
def delete_User(request, pid):
    if request.method == "POST":
        target_user = get_object_or_404(User, id=pid)
        if target_user != request.user:
            target_user.delete()
    return redirect('gym:viewUsers')


@login_required
def unread_queries(request):
    contact = Contact.objects.filter(isread="no")
    return render(request, 'unread_queries.html', {'contact': contact})


@login_required
def read_queries(request):
    contact = Contact.objects.filter(isread="yes")
    return render(request, 'read_queries.html', {'contact': contact})


@login_required
def view_queries(request, pid):
    contact = get_object_or_404(Contact, id=pid)
    contact.isread = "yes"
    contact.save()
    return render(request, 'view_queries.html', {'contact': contact})


@login_required
def delete_contact(request, pid):
    if request.method == "POST":
        contact = get_object_or_404(Contact, id=pid)
        contact.delete()
    return redirect('gym:read_queries')


def health_check(request):
    return JsonResponse({"status": "ok"})
