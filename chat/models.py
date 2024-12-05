from django.db import models

# Create your models here.

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    message = models.CharField(max_length=100)
    sender_type = models.CharField(max_length=50)
    rec_type = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'chat'
