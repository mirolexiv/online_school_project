from django.shortcuts import render
from .form import TeacherForm, StudentForm, SubjectForm, LessonForm
from lessons.models import Lessons, Subjects, Teachers, Students



def add_teacher(request):
    form = TeacherForm(request.POST)
    if form.is_valid():
        try:
            Teachers.objects.create(**form.cleaned_data)
            form = TeacherForm()
        except:
            form.add_error(None, "Помилка введення даних")
    else:
        form = TeacherForm()
    context = {'form': form}
    return render(request, 'form_app/add_teacher.html', context)

def add_student(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        try:
            Students.objects.create(**form.cleaned_data)
            form = StudentForm()
        except:
            form.add_error(None, "Помилка введення даних")
    else:
        form = StudentForm()
    context = {'form': form}
    return render(request, 'form_app/add_student.html', context)

def add_subject(request):
    form = SubjectForm(request.POST)
    if form.is_valid():
        try:
            Subjects.objects.create(**form.cleaned_data)
            form = SubjectForm()
        except:
            form.add_error(None, "Помилка введення даних")
    else:
        form = SubjectForm()
    context = {'form': form}
    return render(request, 'form_app/add_subject.html', context)

def add_lessons(request):
    form = LessonForm(request.POST)
    if form.is_valid():
        try:
            Lessons.objects.create(**form.cleaned_data)
            form = LessonForm()
        except:
            form.add_error(None, "Помилка введення даних")
    else:
        form = LessonForm()
    context = {'form': form}
    return render(request, 'form_app/add_lessons.html', context)