from django.db import models

# Create your models here.
class Appointments(models.Model):

    description = models.CharField(max_length=200)
    time = models.TimeField('Time of Appointment ')
    day = models.DateField()

    class Meta:
        verbose_name_plural = 'appointments'