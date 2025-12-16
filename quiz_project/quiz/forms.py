from django import forms
from django.contrib.auth.models import User
from .models import Class, Quest, Quiz, Question

class StudentRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'code']

class JoinClassForm(forms.Form):
    code = forms.CharField(max_length=20)

class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['title', 'duration']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'option1', 'option2', 'option3', 'option4', 'correct_option']
