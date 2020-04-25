from django.db import models
from django.contrib.auth.models import User

class Mifga(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    street = models.CharField(max_length=25)
    house_number = models.CharField(max_length=3)
    letter = models.CharField(max_length=1)
    neighborhood = models.CharField(max_length=25)

    def __str__(self):
        return self.title


