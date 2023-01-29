from django.shortcuts import render
from .models import Articles
from about.models import about_detail

# Create your views here.

# rendering Articles model Info to template

def main(request):
    context = {
        'Articles_for_template' : Articles.objects.all()
    }
    return render(request, 'article/article.html',context)

def detail(request,pk):
    context = {
        'Articles_for_template' : Articles.objects.filter(id=int(pk)),
        'about_detail_for_template' : about_detail.objects.last()
    }
    return render (request, 'article/article_detail.html',context)
