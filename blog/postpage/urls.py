from django.urls import path
from postpage.views import ArticleCreate

urlpatterns = [
    path('', ArticleCreate.as_view(), name='formpage'),
]