import logging
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from ..models.articles import Article
from ..serializers.articles import ArticleSerializer

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def get_article_data():
    articles = Article.objects.all()
    articles_serializer = ArticleSerializer(articles, many = True)
    return JsonResponse(articles_serializer.data, safe = False)

def create_article(article_data):
    article_serializer = ArticleSerializer(data=article_data)
    if article_serializer.is_valid():
        article_serializer.save()
        return JsonResponse(article_serializer.data, status=201)
    else:
        return JsonResponse(article_serializer.errors, status=400)
