
from django.urls import path
from . import views
#from main import views as v

urlpatterns = [
    path('home/', views.HomeView, name="home"),

]
