from django.db import models
import uuid

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('NEW_CONNECTION', 'New Connection'),
        ('BILLING_ISSUE', 'Billing Issue'),
        ('METER_PROBLEM', 'Meter Problem'),
        ('OTHER', 'Other'),
    ]

    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
        ('CLOSED', 'Closed'),
    ]

    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    customer_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tracking_id} - {self.customer_name}"
