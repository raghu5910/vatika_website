from django.db import models
from django.urls import reverse
# Create your models here.

from django.contrib.auth import get_user_model
User = get_user_model()

class BookTable(models.Model):
    booked_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='booktables')
    customer = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    total_persons = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return self.customer

    def get_absolute_url(self):
        return reverse('Table:confirm-mail')
