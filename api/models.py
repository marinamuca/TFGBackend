from django.db import models
from django.core.validators import *

# Create your models here.
class Exhibition(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.TextField()
    theme = models.TextField()
    room_width = models.IntegerField(default = 1, validators=[MinValueValidator(1)])
    room_length = models.IntegerField(default = 1, validators=[MinValueValidator(1)])

    class Meta:
        ordering = ['name']
     
    def __str__(self):
        return self.name
    
class Illustration(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.TextField()
    description = models.TextField(null=True)
    position = models.IntegerField(default= -1)
    image = models.ImageField(upload_to='illustrations', default="illustrations/default-placeholder.png")
    date_painted = models.DateField()
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

    class Meta:
        ordering = ['position', 'id']
     
    def __str__(self):
        return self.title
    
