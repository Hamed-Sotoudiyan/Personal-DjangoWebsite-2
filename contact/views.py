from django.shortcuts import render
import requests
from .models import Contact
from django.contrib import messages
from about.models import about_detail
# Create your views here.

# Saving Posts (ContatcUs) To DB
# all of html files are in templates folder in a main root of project

def main(request):
    if request.method == 'POST':
        if( len(request.POST.get('full_name')) !=0 and len(request.POST.get('subject')) !=0
            and len(request.POST.get('email')) !=0 and len(request.POST.get('message')) !=0 ):


            fullname_from_template = request.POST.get('full_name')
            email_from_template = request.POST.get('email')
            subject_from_template = request.POST.get('subject')
            message_from_template = request.POST.get('message')

            ContactFormData = Contact(full_name=request.POST.get('full_name'),
                                          email=request.POST.get('email'),
                                          subject=request.POST.get('subject'),
                                          message=request.POST.get('message'))
            ContactFormData.save()
            messages.success(request, 'پیام شما با موفقیت ثبت شد، متشکریم.')
        else:
            messages.error(request, 'وارد کردن همه فیلدها اجباری است')
    context = {
        'email_from_template' : about_detail.objects.last()
    }
    return render (request, 'contact/contact.html',context)
