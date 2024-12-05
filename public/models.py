from django.db import models

# Create your models here.


class Public(models.Model):
    p_id = models.AutoField(primary_key=True)
    pname = models.CharField(max_length=45)
    age = models.IntegerField()
    gender = models.CharField(max_length=45)
    place = models.CharField(max_length=45)
    phone_number = models.IntegerField()
    password = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'public'
