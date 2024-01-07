from rest_framework import serializers
from django.utils.text import slugify
from myport.models import Project, Category



# Serializer for the Project model
class ProjectSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)  # Set read_only to True to generate the slug automatically
    
    class Meta:
        model = Project
        fields = '__all__'
        
    def create(self, validated_data):
        # Generate slug from the tile field 
        title = validated_data.get('title', '')
        slug = slugify(title) #Slugify the title to create slug
        
        # Add the generated slug to the data before savings
        validated_data['slug'] = slug
        
        return super(ProjectSerializer, self).create(validated_data)
    
    
    
    def update(self, instance, validated_data):
        # Update the instance with the new validated data
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.website_url = validated_data.get('website_url', instance.website_url)
        instance.github= validated_data.get('github', instance.github)
        
        
        # Update other fields similarly
        
        # Regenerate the slug if the title has changed
        new_title = validated_data.get('title')
        if new_title and new_title != instance.title:
            instance.slug = slugify(new_title)
        
        instance.save()
        return instance
        
        


# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'