from django.urls import path
from . import views

app_name = 'hiddenadmin'

# HTML pages of Hidden admin application

urlpatterns = [
    path('', views.authentication, name='authentication'),
    path('adminpagemenu/', views.adminpagemenu, name='adminpagemenu'),
    path('aboutpage/', views.aboutpage, name='aboutpage'),
    path('travelogue/', views.travelogue, name='travelogue'),
    path('note/', views.note, name='note'),
    path('article/', views.article, name='article'),
    path('gallery/', views.gallery, name='gallery'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.home, name='home'),
]
