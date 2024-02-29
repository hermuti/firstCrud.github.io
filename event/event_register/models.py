from django.db import models

# Create your models here.

class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    event_name = models.CharField(max_length=255)
    date_and_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    description = models.TextField()
    organizer_details = models.CharField(max_length=255)

    def __str__(self):
        return self.event_name
    
class Registration(models.Model):
      registration_id = models.AutoField(primary_key=True)
      event = models.ForeignKey('Event', on_delete=models.CASCADE)
      attendee_name = models.CharField(max_length=255)
      email = models.EmailField()
      phone_number = models.CharField(max_length=20)
      additional_info = models.TextField(blank=True, null=True)

def __str__(self):
        return f"{self.attendee_name} ({self.event.event_name})"