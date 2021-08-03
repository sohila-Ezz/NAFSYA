from django.contrib.auth.models import User
from django.db import models
from docters.models import Docter
# Create your models here.
class Dates(models.Model):
    startdate=models.TimeField()
    enddate=models.TimeField()
    bookedup=models.BooleanField()
    docter_fullname=models.ForeignKey(Docter,related_name="dates",on_delete=models.CASCADE)
    booked=models.ForeignKey(User,related_name="booked_by",on_delete=models.CASCADE)
    added=models.ForeignKey(User,related_name="added_by",on_delete=models.CASCADE)
