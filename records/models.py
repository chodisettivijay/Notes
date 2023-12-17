from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    Tittle=models.CharField(max_length=100)
    discription=models.TextField()
    time_stamp=models.DateTimeField(auto_now_add=True)
    user_profile=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s' % (self.Tittle, self.user_profile)