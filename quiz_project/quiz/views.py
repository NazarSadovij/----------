from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import (StudentRegisterForm, ClassForm, JoinClassForm,
                    QuestForm, QuizForm, QuestionForm)
from .models import Profile, Class, StudentClass, Quest, Quiz, Question
from django.http import HttpResponseForbidden


def home(request):
    return render(request, 'quiz/home.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if user.profile.is_teacher:
                return redirect('teacher_dashboard')
            else:
                return redirect('student_dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'quiz/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def student_register(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = StudentRegisterForm()
    return render(request, 'quiz/student_register.html', {'form': form})

@login_required
def teacher_dashboard(request):
    classes = Class.objects.filter(teacher=request.user)
    return render(request, 'quiz/teacher_dashboard.html', {'classes': classes})

@login_required
def student_dashboard(request):
    student_classes = StudentClass.objects.filter(student=request.user)
    classes = [sc.class_obj for sc in student_classes]
    return render(request, 'quiz/student_dashboard.html', {'classes': classes})

@login_required
def create_class(request):
    if request.method == "POST":
        form = ClassForm(request.POST)
        if form.is_valid():
            class_obj = form.save(commit=False)
            class_obj.teacher = request.user
            class_obj.save()
            return redirect('teacher_dashboard')
    else:
        form = ClassForm()
    return render(request, 'quiz/create_class.html', {'form': form})

@login_required
def join_class(request):
    if request.method == "POST":
        form = JoinClassForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            class_obj = get_object_or_404(Class, code=code)
            StudentClass.objects.get_or_create(student=request.user, class_obj=class_obj)
            return redirect('student_dashboard')
    else:
        form = JoinClassForm()
    return render(request, 'quiz/join_class.html', {'form': form})


@login_required
def quiz_create(request):
    if not request.user.is_teacher:
        return HttpResponseForbidden("Тільки вчитель може створювати вікторини")

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect('home')
    else:
        form = QuizForm()

    return render(request, 'quiz/quiz_create.html', {'form': form})
