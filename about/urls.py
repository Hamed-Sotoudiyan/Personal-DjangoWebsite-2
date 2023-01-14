from django.urls import path
from . import views

app_name = 'about'

# just one page for showing AbouUs models atributes
urlpatterns = [
    path('', views.main, name='main'),
]
