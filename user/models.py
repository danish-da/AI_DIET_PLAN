from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    address = models.CharField(max_length=45)
    phn_number = models.IntegerField()
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'user'

