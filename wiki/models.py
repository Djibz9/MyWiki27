from django.db import models
from django.urls import reverse

class Page(models.Model):
    title = models.CharField(max_length=64, primary_key = True)
    #allows content to be added to the page
    content = models.TextField()
    #collects statistics about how many times page has been accessed
    counter = models.IntegerField(default = 1)
    
    #collects the title of the page
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse ('wiki:detail', args=[self.title])
#this is the class where we enable the upload images on the website. 
class UserFileUpload(models.Model):
    upload = models.FileField(upload_to='upload/')
    
    def __str__(self):
        return self.upload.name
    

