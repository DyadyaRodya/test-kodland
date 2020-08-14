from django.urls import path
from mainpage.views import mainpage, article

urlpatterns = [
    path('', mainpage, name='mainpage'),
    path('<int:pk>/', article, name='article'),
]