from django.db import models
from django.contrib.auth.models import User

BLOOD_GROUPS = [
    ('A+', 'A+'), ('A-', 'A-'),
    ('B+', 'B+'), ('B-', 'B-'),
    ('AB+', 'AB+'), ('AB-', 'AB-'),
    ('O+', 'O+'), ('O-', 'O-'),
]

AVAILABILITY_CHOICES = [
    ('Available', 'Available'),
    ('Not Available', 'Not Available'),
]

STATUS_CHOICES = [
    ('Pending', 'Pending'),
    ('Fulfilled', 'Fulfilled'),
    ('Cancelled', 'Cancelled'),
]

class DonorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='donor_profile')
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)
    last_donation_date = models.DateField(null=True, blank=True)
    availability = models.CharField(max_length=20, choices=AVAILABILITY_CHOICES, default='Available')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name() or self.user.username} ({self.blood_group})"

class BloodRequest(models.Model):
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5, choices=BLOOD_GROUPS)
    hospital_name = models.CharField(max_length=150)
    location = models.CharField(max_length=100)
    required_date = models.DateField()
    bags_required = models.PositiveIntegerField(default=1)
    contact_number = models.CharField(max_length=15)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient_name} - {self.blood_group}"