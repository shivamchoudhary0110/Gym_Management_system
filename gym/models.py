from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True)
    emailid = models.CharField(max_length=50, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    subject = models.CharField(max_length=100, blank=True)
    message = models.CharField(max_length=300, blank=True)
    msgdate = models.DateField(null=True, blank=True)
    isread = models.CharField(max_length=10, default='no')

    def __str__(self):
        return self.name or ''


class Enquiry(models.Model):
    name = models.CharField(max_length=150, blank=True)
    mobile = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.name or ''


class Equipment(models.Model):
    name = models.CharField(max_length=150, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    unit = models.CharField(max_length=50, blank=True)
    purchasedate = models.DateField(null=True, blank=True)
    description = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name or ''


class Plan(models.Model):
    name = models.CharField(max_length=150, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    duration = models.PositiveIntegerField(default=1, help_text='Duration in months')

    def __str__(self):
        return self.name or ''


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='memberships')
    name = models.CharField(max_length=150, blank=True)
    contact = models.CharField(max_length=15, blank=True)
    email = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True, blank=True)
    joindate = models.DateField(null=True, blank=True)
    initamount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name or ''


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, blank=True, choices=[('Male', 'Male'), ('Female', 'Female')])

    def __str__(self):
        return f'{self.user.username} Profile'
