from rest_framework import serializers
from ..models.articles import Article

class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    content = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance
