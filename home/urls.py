from django.urls import path
from . import views

app_name = 'home'

# just one page for HomePage

urlpatterns = [
    path('', views.main, name='main'),
]
