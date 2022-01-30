from django.urls import path
from . import views

urlpatterns = [
    path('adquieralo5/',views.hola5,name= 'inicio5'),
    path('adquieralo4/',views.hola4,name= 'inicio4'),
    path('adquieralo3/',views.hola3,name= 'inicio3'),
    path('adquieralo2/',views.hola2,name= 'inicio2'),
    path('adquieralo1/',views.hola1,name= 'inicio1'),
    path('adquieralo/',views.hola,name= 'inicio'),
    path('pa/',views.pa,name='pa'),
    path('pa1/',views.pa1,name= 'pa1'),
    path('pa2/',views.pa2,name= 'pa2'),
    path('pa3/',views.pa3,name= 'pa3'),
    path('pa4/',views.pa4,name= 'pa4'),
    path('pa5/',views.pa5,name= 'pa5'),
]