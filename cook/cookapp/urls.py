from django.urls import path
from . import views

urlpatterns = [
    path('rykacure/', views.cure_recipes, name='cure_recipes'),

]
