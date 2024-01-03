from django.db import models
from django.urls import reverse

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=440)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    embed_code = models.CharField(max_length=550, blank=True)
    image = models.ImageField(upload_to='projects/images', blank=True)
    date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-date'])
        ]
           
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('feed:post_detail', args=[self.id, self.slug])