from rest_framework import serializers
from .models import Article, ArticleCategory, ArticleImage

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'author', 'pub_date', 'category_id', 'hero_image', 'description')

class ArticleImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleImage
        
class ArticleCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleCategory