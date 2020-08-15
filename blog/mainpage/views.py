from django.shortcuts import render
from mainpage.models import Article
from django.http import HttpResponseNotFound

# Create your views here.
def mainpage(request):
        queryset = Article.objects.all().order_by("-date")[:10]
        count = queryset.count()
        if count:
                content = {'p0' : {'id' : str(queryset[0].id),'title' : queryset[0].title, 'text' : queryset[0].text, 'image' : queryset[0].image, 'date' : queryset[0].date}}
                posts = { 'posts' : ({'id' : str(queryset[i].id),'title' : queryset[i].title, 'text' : queryset[i].text, 'image' : queryset[i].image, 'date' : queryset[i].date} for i in range(1, count))}
                content.update(posts)
                return render(request, "mainpage/res.html", content)
        return render(request, "mainpage/res.html")

def article(request, pk):
        queryset = Article.objects.filter(id = pk)
        if not queryset.count():
                return HttpResponseNotFound('<h1>Page not found</h1>')
        queryset = queryset[0]
        content = {'title' : queryset.title, 'text' : queryset.text, 'date' : queryset.date, 'image' : queryset.image}
        return render(request, "mainpage/article_res.html", content)
