from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    
    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        
    def __str__(self):
            return self.name
        
    def get_absolute_url(self):
        return reverse('myport:project_list_by_category', args=[self.slug])
    
        
class Project(models.Model):
    category = models.ForeignKey(Category,  related_name='projects', on_delete=models.CASCADE)
    title = models.CharField(max_length=240)
    description = models.TextField()
    slug = models.SlugField(max_length=240)
    image = models.ImageField(upload_to='projects/images', blank=True)
    image_url = models.URLField(max_length=500, blank=True)
    embed_code = models.CharField(max_length=550, blank=True)
    website_url = models.URLField(max_length=500, blank=True)
    github = models.URLField(max_length=500, blank=True)
    date = models.DateField(auto_now=True)
    
    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['id', 'slug']), 
            models.Index(fields=['title']), 
            models.Index(fields=['-date']), 
            
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('myport:project_detail', args=[self.id, self.slug])
    

    

       
    
 

