from django import forms
from mainpage.models import Article

class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ("title", "text", "image")
