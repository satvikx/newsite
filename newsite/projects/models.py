from django.db import models
from django.utils import timezone

class User(models.Model):
    first_name = models.CharField('First Name', max_length=30)
    last_name = models.CharField('Last Name', max_length=30)
    email = models.EmailField('User Email')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Project Name', max_length=120)
    points = models.IntegerField(default=0)
    description = models.TextField(blank=True)
    date = models.DateTimeField('Date', blank = True, default=timezone.now)
    due_date = models.DateField('Due Date', blank = True)
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name
    

    

# Create your models here.
