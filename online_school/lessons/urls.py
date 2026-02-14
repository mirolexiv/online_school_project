from django.urls import path
from . import views

app_name = 'lessons'

urlpatterns = [
    path('students/', views.web_students, name='students'),
    path('subjects/', views.web_subjects, name='subjects'),
    path('teachers/', views.web_teachers, name='teachers'),
    path('lessons/', views.web_lessons, name='lessons'),
    path('', views.web_about, name='about'),
]