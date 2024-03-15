from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignUpForm
from django.http import HttpResponseRedirect

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

@login_required
def logout_view(request):
    return render(request,'testapp/logout.html')

def signup_view(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        user = form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html', {'form':form})