from django.db import models

# Create your models here.
class Alert(models.Model):
    alert_id = models.AutoField(primary_key=True)
    alert = models.CharField(max_length=45)
    date = models.DateField()
    time = models.TimeField()

    class Meta:
        managed = False
        db_table = 'alert'
