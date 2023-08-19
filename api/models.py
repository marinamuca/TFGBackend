import sys
from typing import Iterable, Optional
from django.db import models
from django.core.validators import *
from io import BytesIO
from PIL import Image
from django.core.files import File
from django.contrib.auth.models import User

#image compression method
def compress(image, quality):
    im = Image.open(image)
    im_io = BytesIO() 
    x, y = im.size

    maxDim = 1000
    if x>y and x>maxDim:
         x=maxDim
         y=y*(maxDim/x)
    else:
        if y>x and y>maxDim:
            y=maxDim
            x=x*(maxDim/y)
    
    im.thumbnail((x,y), Image.Resampling.LANCZOS)
    im.save(im_io, format='JPEG', optimize=True, quality=quality) 
    new_image = File(im_io, name=image.name)
    return new_image


class UserProfile(models.Model):
    USER_TYPE=(
        ('ARTIST', 'ARTIST'),
        ('VISITOR', 'VISITOR'),
    )

    id = models.AutoField(primary_key = True)
    type = models.CharField(blank = False, max_length=7, choices = USER_TYPE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # following = models.ManyToManyField("self", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 
    
    def isArtist(self):
        return self.type=="ARTIST"

class Exhibition(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.TextField()
    theme = models.TextField()
    room_width = models.IntegerField(default = 1, validators=[MinValueValidator(1)])
    room_length = models.IntegerField(default = 1, validators=[MinValueValidator(1)])
    artist = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
     
    def __str__(self):
        return self.name
    
class Illustration(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.TextField()
    description = models.TextField(null=True)
    position = models.IntegerField(default= -1)
    image = models.ImageField(upload_to='illustrations')
    date_painted = models.DateField()
    exhibition = models.ForeignKey(Exhibition, on_delete=models.CASCADE)

    class Meta:
        ordering = ['position', 'id']

    def save(self, *args, **kwargs):
                new_image = self.image
                if new_image.size > 0.3*1024*1024: #if size greater than 300kb
                    self.image = compress(new_image, 70)
                super().save(*args, **kwargs)
     
    def __str__(self):
        return self.title

    