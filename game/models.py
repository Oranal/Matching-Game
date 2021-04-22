from django.db import models

class Board(models.Model):
    category = models.CharField(max_length=40)
    data = models.JSONField()

    def __str__(self):
        return self.category

class Institution(models.Model):
    name = models.CharField(max_length=40)
    data = models.JSONField()

    def __str__(self):
        return self.name