
from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager
    
Usertype =(
    ('collage', 'collage'),
    ('teacher', 'teacher'),
    
)

class College(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.name
    
class User(AbstractUser):
    # username = None
    collage = models.ForeignKey(College, on_delete=models.CASCADE,null = True,blank=True)
    username = models.CharField(unique=True, max_length=16)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    usertype = models.CharField(choices= Usertype ,max_length=60)
    USERNAME_FIELD = "username"
    objects = UserManager()


class Batch(models.Model):
    name = models.CharField(max_length=255)  # E.g., "3rd Semester"
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Class(models.Model):
    name = models.CharField(max_length=255)  # E.g., "Java Class"
    description = models.TextField(blank=True, null=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'usertype': 'teacher'})
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE,null = True, blank= True)

    def __str__(self):
        return self.name