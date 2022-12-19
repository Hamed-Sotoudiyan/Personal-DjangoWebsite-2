from django.shortcuts import render
from .models import Notes
from about.models import about_detail

# Create your views here.


def main(request):
    context = {
        'Notes_for_template' : Notes.objects.all()
    }
    return render(request, 'note/note.html',context)

def detail(request,pk):
    context = {
        'Notes_for_template' : Notes.objects.filter(id=int(pk)),
        'about_detail_for_template' : about_detail.objects.last()
    }
    return render (request, 'note/note_detail.html',context)
