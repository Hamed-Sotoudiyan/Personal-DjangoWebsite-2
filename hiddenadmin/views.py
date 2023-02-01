from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
import requests
from about.models import about_detail
from travelogue.models import Travelogue,Images
from note.models import Notes
from article.models import Articles
from gallery.models import Gallery
from contact.models import Contact
from home.models import Home
# Create your views here.

# CRUD Section of all applications of website
# all of html files are in templates folder in a main root of project


def authentication(request):
    if request.method == 'POST':
        user = authenticate(request,username=request.POST.get('username'),password=request.POST.get('password'))
        if user is not None:
            login(request,user)
            return redirect('hiddenadmin:adminpagemenu')
    return render(request, 'hiddenadmin/authentication.html')

def adminpagemenu(request):
    if request.method == 'POST':
        logout(request)
        return redirect('hiddenadmin:authentication')
    return render(request, 'hiddenadmin/adminpagemenu.html')

def aboutpage(request):
    if request.method == 'POST':
        if ('full_namebtn' in request.POST and len(request.POST.get('full_name')) !=0):
            about_detail.objects.filter(id=1).update(full_name=request.POST.get('full_name'))
        elif ('emailbtn' in request.POST and len(request.POST.get('email')) !=0):
            about_detail.objects.filter(id=1).update(email=request.POST.get('email'))
        elif ('title1btn' in request.POST and len(request.POST.get('title1')) !=0):
            about_detail.objects.filter(id=1).update(title1=request.POST.get('title1'))
        elif ('title2btn' in request.POST and len(request.POST.get('title2')) !=0):
            about_detail.objects.filter(id=1).update(title2=request.POST.get('title2'))
        elif ('textbtn' in request.POST and len(request.POST.get('text')) !=0):
            about_detail.objects.filter(id=1).update(text=request.POST.get('text'))
        elif ('imagebtn' in request.POST and request.FILES['image'] !=0):
            obj = about_detail.objects.last()
            obj.image = request.FILES['image']
            obj.save()
        elif ('resumebtn' in request.POST and request.FILES['resume'] !=0):
            obj = about_detail.objects.last()
            obj.resume = request.FILES['resume']
            obj.save()
        elif ('agebtn' in request.POST and len(request.POST.get('age')) !=0):
            about_detail.objects.filter(id=1).update(age=request.POST.get('age'))
        elif ('clubhousebtn' in request.POST and len(request.POST.get('clubhouse')) !=0):
            about_detail.objects.filter(id=1).update(clubhouse=request.POST.get('clubhouse'))
        elif ('telegrambtn' in request.POST and len(request.POST.get('telegram')) !=0):
            about_detail.objects.filter(id=1).update(telegram=request.POST.get('telegram'))
        context = {
            'about_detail' : about_detail.objects.last()
        }
    else:
        context = {
            'about_detail' : about_detail.objects.last()
        }
    return render(request, 'hiddenadmin/aboutpage.html' , context )

def travelogue(request):
    if request.method == 'POST':
        if ('save' in request.POST and len(request.POST.get('date')) !=0
            and len(request.POST.get('title')) !=0
            and len(request.POST.get('text')) !=0
            and len(request.POST.get('province')) !=0
            and len(request.POST.get('city')) !=0
            and ( 'image_one' in request.FILES)
            and ( 'image_two' in request.FILES)):

            TravelogueFormData = Travelogue(date=request.POST.get('date'),
                                          title=request.POST.get('title'),
                                          text=request.POST.get('text'),
                                          province=request.POST.get('province'),
                                          city=request.POST.get('city'),
                                          image_one=request.FILES['image_one'],
                                          image_two=request.FILES['image_two'])
            TravelogueFormData.save()

            if ('image_three' in request.FILES) :
                last_id = Travelogue.objects.last()
                ImageTravelogueFormData = Images(image=request.FILES['image_three'],
                                               travelogue_id=last_id)
                ImageTravelogueFormData.save()
            if ('image_four' in request.FILES) :
                last_id = Travelogue.objects.last()
                ImageTravelogueFormData = Images(image=request.FILES['image_four'],
                                               travelogue_id=last_id)
                ImageTravelogueFormData.save()
            if ('image_five' in request.FILES) :
                last_id = Travelogue.objects.last()
                ImageTravelogueFormData = Images(image=request.FILES['image_five'],
                                               travelogue_id=last_id)
                ImageTravelogueFormData.save()
        elif ('deleteBtn' in request.POST and len(request.POST.get('Tid')) !=0) :
            Travelogue.objects.filter(id=int(request.POST.get('Tid'))).delete()

    context = {
        'Travelogue_for_template' : Travelogue.objects.all()
    }
    return render (request,'hiddenadmin/travelogue.html',context)

def note(request):
    if request.method == 'POST':
        if ('save' in request.POST and len(request.POST.get('date')) !=0
            and len(request.POST.get('title')) !=0
            and len(request.POST.get('text')) !=0
            and ( 'image' in request.FILES)):

            NoteFormData = Notes(date=request.POST.get('date'),
                                          title=request.POST.get('title'),
                                          text=request.POST.get('text'),
                                          image=request.FILES['image'])
            NoteFormData.save()

            if (len(request.POST.get('note_url')) !=0) :
                last_id = Notes.objects.last()
                Notes.objects.filter(id=int(last_id.id)).update(note_url=request.POST.get('note_url'),
                                               is_note_url=True)
        elif ('deleteBtn' in request.POST and len(request.POST.get('Nid')) !=0) :
            Notes.objects.filter(id=int(request.POST.get('Nid'))).delete()

    context = {
        'Notes_for_template' : Notes.objects.all()
    }
    return render (request,'hiddenadmin/note.html',context)

def article(request):
    if request.method == 'POST':
        if ('save' in request.POST and len(request.POST.get('date')) !=0
            and len(request.POST.get('title')) !=0
            and len(request.POST.get('publisher')) !=0
            and len(request.POST.get('abstract')) !=0
            and ( 'article' in request.FILES)):

            ArticleFormData = Articles(date=request.POST.get('date'),
                                          title=request.POST.get('title'),
                                          publisher=request.POST.get('publisher'),
                                          abstract=request.POST.get('abstract'),
                                          article=request.FILES['article'])
            ArticleFormData.save()

            if (len(request.POST.get('article_url')) !=0) :
                last_id = Articles.objects.last()
                Articles.objects.filter(id=int(last_id.id)).update(article_url=request.POST.get('article_url'),
                                        is_article_url=True)

        elif ('deleteBtn' in request.POST and len(request.POST.get('Aid')) !=0) :
            Articles.objects.filter(id=int(request.POST.get('Aid'))).delete()

    context = {
        'Articles_for_template' : Articles.objects.all()
    }
    return render (request,'hiddenadmin/article.html',context)

def gallery(request):
    if request.method == 'POST':
        if ('save' in request.POST and len(request.POST.get('date')) !=0
            and len(request.POST.get('title')) !=0
            and ( 'image' in request.FILES)):

            GalleryFormData = Gallery(date=request.POST.get('date'),
                                          title=request.POST.get('title'),
                                          image=request.FILES['image'])
            GalleryFormData.save()

        elif ('deleteBtn' in request.POST and len(request.POST.get('Gid')) !=0) :
            Gallery.objects.filter(id=int(request.POST.get('Gid'))).delete()

    context = {
        'Gallery_for_template' : Gallery.objects.all()
    }
    return render (request,'hiddenadmin/gallery.html',context)

def contact(request):
    if (request.method == 'POST' and 'deleteBtn' in request.POST and len(request.POST.get('Cid')) !=0):
        Contact.objects.filter(id=int(request.POST.get('Cid'))).delete()
    context = {
        'contacts_for_template' : Contact.objects.all()
    }
    return render(request,'hiddenadmin/contact.html',context)

def home(request):
    if request.method == 'POST':
        if ('title1btn' in request.POST and len(request.POST.get('title1')) !=0):
            Home.objects.filter(id=1).update(title1=request.POST.get('title1'))
        elif ('title2btn' in request.POST and len(request.POST.get('title2')) !=0):
            Home.objects.filter(id=1).update(title2=request.POST.get('title2'))
        context = {
            'Home' : Home.objects.last()
        }
    else:
        context = {
            'Home' : Home.objects.last()
        }
    return render(request, 'hiddenadmin/home.html' , context )
