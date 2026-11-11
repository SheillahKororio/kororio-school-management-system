from django.shortcuts import render


def base_context(page_name):
    return {'page_name': page_name}


def home(request):
    return render(request, 'dashboard.html', base_context('dashboard'))


def dashboard(request):
    return render(request, 'dashboard.html', base_context('dashboard'))


def students(request):
    return render(request, 'students.html', base_context('students'))


def teachers(request):
    return render(request, 'teachers.html', base_context('teachers'))


def classes(request):
    return render(request, 'classes.html', base_context('classes'))


def attendance(request):
    return render(request, 'attendance.html', base_context('attendance'))


def exams(request):
    return render(request, 'exams.html', base_context('exams'))


def fees(request):
    return render(request, 'fees.html', base_context('fees'))


def reports(request):
    return render(request, 'reports.html', base_context('reports'))


def settings(request):
    return render(request, 'settings.html', base_context('settings'))


def about(request):
    return render(request, 'about.html')


def contactus(request):
    return render(request, 'contactus.html')


def services(request):
    return render(request, 'services.html')