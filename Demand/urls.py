from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('prediction',views.prediction,name='prediction'),
    path('reference',views.reference,name='reference'),
    path('about',views.about,name='about')
]
