from django.db import models

role_choices = (
    ('Kindergarden', 'Kindergarden'),
    ('Child', 'Child'),
)


class Account(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    rating = models.IntegerField(null=True, blank=True)
    institution = models.CharField(max_length=60)
    role = models.CharField(
        max_length=15, choices=role_choices, default='Child')
    categories = models.JSONField(default={})

    def __str__(self):
        return self.username

    def get_permission(self):
        if self.role == 'Administrator':
            return 'All'
        if self.role == 'Kindergarden':
            return 'Limited'
        if self.role == 'Child':
            return 'Player'
        else:
            return 'ERROR'
