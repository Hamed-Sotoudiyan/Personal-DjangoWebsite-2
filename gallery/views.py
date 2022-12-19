from django.shortcuts import render
from .models import Gallery

# Create your views here.
def main(request):
    context = {
        'Gallery_for_template' : Gallery.objects.all()
    }
    return render(request, 'gallery/gallery.html', context)
