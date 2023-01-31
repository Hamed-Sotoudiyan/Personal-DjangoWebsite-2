from django.urls import path
from . import views

app_name = 'contact'

# just one page for showing ContactUs models atributes

urlpatterns = [
    path('', views.main, name='main'),
]
