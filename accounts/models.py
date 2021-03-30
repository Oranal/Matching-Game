from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)    
    rating = models.IntegerField()
    institution = models.CharField(max_length=60)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name + self.last_name