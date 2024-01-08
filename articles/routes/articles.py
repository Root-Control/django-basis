from django.urls import path
from ..views.articles import ArticleView

urlpatterns = [
    path('articles', ArticleView.as_view(), name='article_api'),
]