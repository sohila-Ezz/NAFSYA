from django.db import models
from django.contrib.auth.models import User
from docters.models import Docter
# Create your models here.
class Consulation(models.Model):
    content=models.CharField(max_length=1000)
    replay=models.BooleanField()
    consulation_user=models.ForeignKey(User,related_name="consulation",on_delete=models.CASCADE)
    Consulation_docter=models.ForeignKey(Docter,related_name="consulation",on_delete=models.CASCADE)

    def __str__(self):
        return  self.replay,self.content

