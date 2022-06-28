from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    #body = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    project_file = models.FileField(upload_to='project_data/', null=True)
    project_image = models.ImageField(upload_to='project_images/', null=True)