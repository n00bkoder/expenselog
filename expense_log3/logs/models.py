from django.db import models
from django.conf import settings
# Create your models here.




class Log(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.CharField(max_length=50)
    cost = models.DecimalField(max_digits=11, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)


