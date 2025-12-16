from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('student/register/', views.student_register, name='student_register'),
    path('teacher/', views.teacher_dashboard, name='teacher_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('teacher/create_class/', views.create_class, name='create_class'),
    path('student/join_class/', views.join_class, name='join_class'),
]
