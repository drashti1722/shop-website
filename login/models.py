from django.db import models
class login(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField()
    FEMALE='F'
    MALE='M'
    CHOICES=[
        ('FEMALE',FEMALE),
        ('MALE', MALE)
    ]
    gender=models.CharField(max_length=20,choices=CHOICES)
    def __str__(self):
        return self.username

# Create your models here.
