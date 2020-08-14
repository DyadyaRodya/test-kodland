from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import ArticleForm
from mainpage.models import Article
from datetime import datetime

# Create your views here.
def form(request):
        return render(request, "postpage/res.html")

class ArticleCreate(View):
        def get(self, request):
                form = ArticleForm()
                return render(request, "postpage/res.html", context={'form' : form})
        
        def post(self, request):
                bound_form = ArticleForm(request.POST, request.FILES)
                if bound_form.is_valid():
                        new_article = Article.objects.create(
                        title = bound_form.cleaned_data['title'],
                        text = bound_form.cleaned_data['text'],
                        date = datetime.now(),
                        image = bound_form.cleaned_data['image']
                )
                        return redirect("/"+str(new_article.id))
                return render(request, "postpage/res.html", context={'form' : bound_form})