from django.views.decorators.csrf import csrf_exempt
from ..services.articles import get_article_data,create_article
from django.views import View
from django.utils.decorators import method_decorator
from rest_framework.parsers import JSONParser
from ..serializers.articles import ArticleSerializer

class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return get_article_data()

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        article_data = JSONParser().parse(request)
        return create_article(article_data)    
        
        