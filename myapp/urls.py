from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('students/', views.students, name='students'),
    path('teachers/', views.teachers, name='teachers'),
    path('classes/', views.classes, name='classes'),
    path('attendance/', views.attendance, name='attendance'),
    path('exams/', views.exams, name='exams'),
    path('fees/', views.fees, name='fees'),
    path('reports/', views.reports, name='reports'),
    path('settings/', views.settings, name='settings'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('services/', views.services, name='services'),
]