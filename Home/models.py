from django.db import models

# Create your models here.

class vc(models.Model):
    name= models.CharField(max_length=50, null=True, blank=True)
    
    
from django.db import models

class About(models.Model):
    section_title = models.CharField(max_length=100, default="About")
    section_text = models.TextField()
    profile_image = models.ImageField(upload_to='profile_images/')
    heading = models.CharField(max_length=100, default="UI/UX Designer & Web Developer")
    intro_text = models.TextField()
    birthday = models.DateField()
    website = models.URLField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    age = models.IntegerField()
    degree = models.CharField(max_length=50)
    email = models.EmailField()
    freelance_status = models.CharField(max_length=50)
    additional_text = models.TextField()

    def __str__(self):
        return self.section_title
