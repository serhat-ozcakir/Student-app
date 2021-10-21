from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm
from .models import Student
# Create your views here.


def home(request):
    return render(request, 'student_register/home.html')



def student_list(request):
    students = Student.objects.all()
    
    context = {
        "students":students
    }
    
    return render(request, 'student_register/student_list.html', context)

def student_form(request):
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    
    context = {
       
       "form":form     
    }
    
    return render(request, "student_register/student_form.html", context)