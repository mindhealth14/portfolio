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
        
        


# Serializer for the Category model
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'