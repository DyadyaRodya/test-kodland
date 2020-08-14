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
                        print()
                        print(bound_form.cleaned_data)
                        print()
                        new_article = Article.objects.create(
                        title = bound_form.cleaned_data['title'],
                        text = bound_form.cleaned_data['text'],
                        date = datetime.now(),
                        image = bound_form.cleaned_data['image']
                )
                        return redirect("/"+str(new_article.id))
                print()
                print(bound_form.errors)
                print()
                return render(request, "postpage/res.html", context={'form' : bound_form})