from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Stocks(models.Model):

    stock_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    price = models.FloatField(blank=True, null=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.stock_name
    
    class Meta:
        db_table = 'stocks'
