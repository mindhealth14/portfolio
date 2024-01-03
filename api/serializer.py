from rest_framework import serializers
from django.utils.text import slugify
from feed.models import Post


        
        
class PostSerializer(serializers.ModelSerializer):
    slug = serializers.SlugField(read_only=True)  # Set read_only to True to generate the slug automatically
    
    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        # Generate slug from the title field or any other field you want
        title = validated_data.get('title', '')
        slug = slugify(title)  # Slugify the title to create the slug
        
        # Add the generated slug to the data before saving
        validated_data['slug'] = slug
        
        return super(PostSerializer, self).create(validated_data)