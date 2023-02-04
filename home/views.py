from django.shortcuts import render
import requests
from .models import Home
from article.models import Articles
from note.models import Notes
from travelogue.models import Travelogue
# Create your views here.

# rendering HomePage Info (Home, Articles, Notes, Travelogue) to template

def main(request):
    context = {
        'home_for_template' : Home.objects.all(),
        'last_article_for_template' : Articles.objects.last(),
        'last_note_for_template' : Notes.objects.last(),
        'last_travelogue_for_template' : Travelogue.objects.last(),
    }
    return render(request,'home/home.html',context)
