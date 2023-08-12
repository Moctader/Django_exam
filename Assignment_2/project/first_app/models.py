from django.db import models

# Create your models here.
class To_Do_Model(models.Model):
    id=models.IntegerField(primary_key=True)
    taskTitle=models.CharField(max_length=20)
    taskDescription=models.CharField(max_length=20)
    is_completed=models.BooleanField(default=False)