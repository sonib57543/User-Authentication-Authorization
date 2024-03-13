from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home_page_view(request):
    return render(request, 'testapp/home.html')

@login_required
def java_exams_view(request):
    return render(request, 'testapp/java.html')

def start_java_exam(request):
    return render(request, 'testapp/start_java_exam.html' )

@login_required
def python_exams_view(request):
    return render(request, 'testapp/python.html')

def start_python_exam(request):
    return render(request,'testapp/start_python_exam.html')

@login_required
def Aptitude_exams_view(request):
    return render(request, 'testapp/aptitude.html')

def start_aptitude_exam(request):
    return render(request, 'testapp/start_aptitude_exam.html')