from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.index),
    path('home/about/', views.about),
    path('hello/<str:username>',views.hello),
    path('home/projects/', views.projects),
    path('home/tasks/<str:title>', views.tasks),
]