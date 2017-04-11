# from django.conf.urls import url
# from . import views

# from django.conf.urls import url
# from rest_framework import routers
# from article.views import ArticleViewSet, ArticleImageViewSet, ArticleCategoryViewSet
# 
# urlpatterns = [
#     url(r'^$', views.IndexView.as_view(), name='index'),
#     url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
#     #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
# ]
# 
# router = routers.DefaultRouter()
# router.register(r'articles', ArticleViewSet)
# router.register(r'images', ArticleImageViewSet)
# router.register(r'category', ArticleCategoryViewSet)
# 
# urlpatterns = router.urls

from django.conf.urls import url
from . import views
from rest_framework import routers
from article.views import ArticleViewSet, ArticleImageViewSet, ArticleCategoryViewSet, ArticleList, ArticleDetail, search_news
import os.path



#defining the site media path
site_media = os.path.join(
    os.path.dirname(__file__), 'article_images'
)

router = routers.DefaultRouter()
router.register(r'articles', ArticleViewSet)
router.register(r'images', ArticleImageViewSet)
router.register(r'category', ArticleCategoryViewSet)

urlpatterns = [
    
    url(r'^$', ArticleList, name='index'),
    url(r'^([0-9]+)/$', ArticleDetail, name='Cloud Edit'),
    url(r'^search', search_news, name='search_news'),
    
    
]
 
urlpatterns += router.urls