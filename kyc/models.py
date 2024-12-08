from django.contrib.auth.models import AbstractUser
from django.db import models

# Extended User model for Agents
class Agent(AbstractUser):
    auuid = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    # Resolve reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='agent_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='agent_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Agent"
        verbose_name_plural = "Agents"

# Customer Model
class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]

    ID_TYPE_CHOICES = [
        ('Passport', 'Passport'),
        ('National ID', 'National ID'),
        ('Driving License', 'Driving License'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    id_number = models.CharField(max_length=20, unique=True)
    id_type = models.CharField(max_length=20, choices=ID_TYPE_CHOICES)
    nationality = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


