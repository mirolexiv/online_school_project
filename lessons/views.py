from django.http import HttpResponse
from django.shortcuts import render
from .models import Students, Teachers, Subjects, Lessons

# Create your views here.
def web_students(request):
    students = Students.objects.all()
    context = {'students': students}
    return render(request, 'lessons/students.html', context)

def web_teachers(request):
    teachers = Teachers.objects.all()
    context = {'teachers': teachers}
    return render(request, 'lessons/teachers.html', context)

def web_subjects(request):
    subjects = Subjects.objects.all()
    context = {'subjects': subjects}
    return render(request, 'lessons/subjects.html', context)

def web_lessons(request):
    lessons = Lessons.objects.all()
    context = {'lessons': lessons}
    return render(request, 'lessons/lessons.html', context)