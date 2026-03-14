from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Person
from django.contrib import messages
@login_required


# Create your views here.
def dashboard_view(request):
    students = Person.objects.all()
    
    return render(request, 'app_staff/dashboard.html', {'students': students,})

def enroll_student(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        age = request.POST.get('age')
        Class = request.POST.get('Class')
        Gender = request.POST.get('Gender')
        Pname = request.POST.get('pname')
        Pcontact = request.POST.get('pcontact')
        Pemail = request.POST.get('pemail')
        s = Person(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            age=age,
            Class=Class,
            Gender=Gender,
            pname=Pname,
            pcontact=Pcontact,
            pemail=Pemail
        )
        if Person.objects.filter(student_id=student_id).exists():
            messages.error(request, "Student with this ID already exists.")
            return render(request, 'app_staff/dashboard.html', {'students': Person.objects.all(),}, {'messages': messages})
        else:
            s.save()
        # print(request.POST)
        # students = Person.objects.all()

        
            messages.success(request, "Student enrolled successfully!")

    # messages.success(request, message)
            return render(request, 'app_staff/dashboard.html', {'students': Person.objects.all(),}, {'messages': messages})
    

def delete_student(request, student_id):
    student = Person.objects.filter(student_id=student_id)
    if student.exists():
        student.delete()
        messages.success(request, "Student deleted successfully!")
    else:
        messages.error(request, "Student not found.")
    return render(request, 'app_staff/dashboard.html', {'students': Person.objects.all(),})

def edit_student(request, student_id):
    student = Person.objects.get(student_id=student_id)
    
    if request.method == "POST":
        student.first_name = request.POST.get('first_name')
        student.last_name = request.POST.get('last_name')
        student.age = request.POST.get('age')
        student.Class = request.POST.get('Class')
        student.Gender = request.POST.get('Gender')
        student.pname = request.POST.get('pname')
        student.pcontact = request.POST.get('pcontact')
        student.pemail = request.POST.get('pemail')
        student.save()
        messages.success(request, "Student information updated successfully!")
    return render(request, 'app_staff/dashboard.html', {'students': Person.objects.all(),})
