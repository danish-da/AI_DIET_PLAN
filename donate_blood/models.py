from django.db import models
from user.models import User
# Create your models here.
class DonateBlood(models.Model):
    blood_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    blood_group = models.CharField(max_length=45)
    health_condition = models.CharField(max_length=45)
    phn = models.IntegerField()
    # user_id = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        managed = False
        db_table = 'donate_blood'


