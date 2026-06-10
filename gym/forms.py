from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Enquiry, Equipment, Plan, Member, UserProfile


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'emailid', 'contact', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}),
            'emailid': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email ID'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message...', 'rows': 4}),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'mobile', 'email', 'age', 'gender']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Mobile Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Age'}),
            'gender': forms.RadioSelect(attrs={'class': 'gender-radio'}),
        }


class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['name', 'amount', 'duration']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Plan Name'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Amount (IN Rs.)'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Duration in Months'}),
        }


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = ['name', 'price', 'unit', 'purchasedate', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Equipment Name'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price (IN Rs.)'}),
            'unit': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Unit'}),
            'purchasedate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Describe about Equipment', 'rows': 3}),
        }


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'contact', 'email', 'gender', 'plan', 'joindate', 'initamount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
            'gender': forms.RadioSelect(attrs={'class': 'gender-radio'}),
            'plan': forms.Select(attrs={'class': 'form-control'}),
            'joindate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'initamount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Initial Amount (IN Rs.)'}),
        }


class MemberEditForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['name', 'contact', 'email', 'gender', 'initamount']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact Number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email ID'}),
            'gender': forms.RadioSelect(attrs={'class': 'gender-radio'}),
            'initamount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Initial Amount (IN Rs.)'}),
        }


class ChangePasswordForm(forms.Form):
    oldpassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter current password'})
    )
    newpassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter new password'})
    )
    confirmpassword = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter confirm password'})
    )


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=50,
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm Password'})


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'date_of_birth', 'gender']
        widgets = {
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.RadioSelect(attrs={'class': 'gender-radio'}),
        }


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
    )
