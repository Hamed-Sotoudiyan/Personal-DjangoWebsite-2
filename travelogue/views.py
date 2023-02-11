from django.shortcuts import render
from .models import Travelogue,Images
from about.models import about_detail

# Create your views here.

# rendering Travelogue Info to template 
# all of html files are in templates folder in a main root of project

def main(request):
    context = {
        'travelogue_for_template' : Travelogue.objects.all()
    }
    return render(request, 'travelogue/travelogue.html' , context)

def detail(request,pk):
    context = {
        'travelogue_for_detail_template' : Travelogue.objects.filter(id=int(pk)),
        'travelogue_images_for_detail_template' : Images.objects.filter(travelogue_id=pk),
        'about_detail_for_template' : about_detail.objects.last()
    }
    return render (request, 'travelogue/travelogue_detail.html',context)
