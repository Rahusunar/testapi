from rest_framework import serializers
from .models import BlogPost  # Ensure you have imported your BlogPost model

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'  # Include all fields from the model
