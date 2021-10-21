from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import StudentForm, StudentUpdateForm
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


def student_update(request, id):
    student = Student.objects.get(id=id)
    form = StudentUpdateForm(instance=student)

    if request.method == "POST":
        form = StudentUpdateForm(request.POST, instance=student)
        print(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form,
        "student": student,
    }
    return render(request, "student_register/student_update.html", context)


def student_delete(request,id):
    student = Student.objects.get(id = id)
    if request.method == 'POST':
        student.delete()
        return redirect('list')
    context = {
        "student":student
        
    }
    
    return render(request, "student_register/student_delete.html", context)
    