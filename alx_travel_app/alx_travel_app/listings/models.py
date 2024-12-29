from django.db import models
import uuid

# Create your models here.

def generate_uuid():
    """
    Generate UUID for primary keys
    """
    return str(uuid.uuid4())

class Property(models.Model):
    property_id = models.UUIDField(primary_key=True, default=generate_uuid)
    name = models.CharField(max_length=250, null=False)
    description = models.TextField(null=False)
    location = models.CharField(max_length=250, null=False)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Booking(models.Model):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELED = "canceled"
    
    STATUS_CHOICES = [
        (PENDING, "Pending"),
        (CONFIRMED, "Confirmed"),
        (CANCELED, "Canceled"),
    ]

    booking_id = models.UUIDField(primary_key=True, default=generate_uuid)
    property_id = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(
        max_length=10, choices=STATUS_CHOICES, default=PENDING, null=False
    )
    created_at = models.DateTimeField(auto_now_add=True)

