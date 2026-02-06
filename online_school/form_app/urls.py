from django.urls import path
from . import views

urlpatterns = [
    path('add_teacher/', views.add_teacher),
    path('add_student/', views.add_student),
    path('add_subject/', views.add_subject),
    path('add_lessons/', views.add_lessons),
]

