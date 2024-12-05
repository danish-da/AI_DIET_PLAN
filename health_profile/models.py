from django.db import models
from user.models import User
# Create your models here.

class HealthProfile(models.Model):
    health_id = models.AutoField(primary_key=True)
    #user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    height = models.IntegerField()
    weight = models.IntegerField()
    body_type = models.CharField(max_length=45)
    working_hour = models.TimeField()

    class Meta:
        managed = False
        db_table = 'health_profile'

