from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.web_students),
    path('subjects/', views.web_subjects),
    path('teachers/', views.web_teachers),
    path('lessons/', views.web_lessons),
]