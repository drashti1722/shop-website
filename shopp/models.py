from django.db import models
from django.db.models.deletion import CASCADE
class category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class shpping(models.Model):
    categories=models.ForeignKey(category,on_delete=CASCADE)
    img=models.ImageField(upload_to='photo')
    name=models.CharField(max_length=20)
    price=models.PositiveBigIntegerField()
    colour=models.CharField(max_length=20)
    def __str__(self):
        return self.name

# Create your models here.
