from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_teacher = models.BooleanField(default=False)
    is_student = models.BooleanField(default=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=50, blank=True)
    is_teacher = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Class(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.name

class StudentClass(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.username} in {self.class_obj.name}"

class Quest(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField(default=10)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='quests')

    def __str__(self):
        return self.title

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    quest = models.ForeignKey(Quest, on_delete=models.CASCADE, related_name='quizzes')

    def __str__(self):
        return self.title

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct_option = models.IntegerField()

    def __str__(self):
        return self.text


