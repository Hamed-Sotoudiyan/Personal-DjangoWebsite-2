from django.shortcuts import render
from .models import about_detail

# Create your views here.

# rendering AboutUs Info (about_detail) to template
def main(request):
    context = {
        'about_detail_for_template' : about_detail.objects.last()
    }
    return render(request, 'about/about.html', context)
