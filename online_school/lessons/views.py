from django.http import HttpResponse
from django.shortcuts import render
from .models import Students, Teachers, Subjects, Lessons
from django.contrib import admin

menu = [{'title': "Про сайт", 'url_name': 'students'},
        {'title': "Заняття", 'url_name': 'lessons'},
        {'title': "Додати", 'url_name': 'teachers'},
        {'title': "Увійти", 'url_name': 'users:login'},
         {'title': "Вийти", 'url_name': 'users:logout'},
        {'title': "Адмін", 'url_name': 'admin:index'},
]



# Create your views here.
def web_students(request):
    students = Students.objects.all()
    context = {'students': students, 'menu': menu}
    return render(request, 'lessons/students.html', context)

def web_teachers(request):
    teachers = Teachers.objects.all()
    context = {'teachers': teachers, 'menu': menu}
    return render(request, 'lessons/teachers.html', context)

def web_subjects(request):
    subjects = Subjects.objects.all()
    context = {'subjects': subjects, 'menu': menu}
    return render(request, 'lessons/subjects.html', context)

def web_lessons(request):
    lessons = Lessons.objects.all()
    context = {'lessons': lessons, 'menu': menu}
    return render(request, 'lessons/lessons.html', context)