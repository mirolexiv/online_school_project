from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.web_students, name='students'),
    path('subjects/', views.web_subjects, name='subjects'),
    path('teachers/', views.web_teachers, name='teachers'),
    path('', views.web_lessons, name='lessons'),
]