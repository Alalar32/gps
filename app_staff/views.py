from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Person
from django.contrib import messages
from django.db.models import Q
@login_required


# Create your views here.
def dashboard_view(request):
    students = Person.objects.all()
    
    if request.method == "GET":
        search_query = request.GET.get('search', '')
        if search_query:
            students = students.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(student_id__icontains=search_query))
            return render(request, 'app_staff/dashboard.html', {'students': students})
    return render(request, 'app_staff/dashboard.html', {'students': students,'search_query': search_query})

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
            return redirect('/staff/dashboard')
        else:
            s.save()
            messages.success(request, "Student enrolled successfully!")
            return redirect('/staff/dashboard')
    return render(request, 'app_staff/dashboard.html')
    

def delete_student(request, student_id):
    student = Person.objects.filter(student_id=student_id)
    if student.exists():
        student.delete()
        messages.success(request, "Student deleted successfully!")
    else:
        messages.error(request, "Student not found.")
    return redirect( '/staff/dashboard')

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
        return redirect('/staff/dashboard')
    
    return render(request, 'app_staff/editstudent.html', {'students': Person.objects.filter(student_id=student_id), 'student': student,})

def class_schedule_view(request):
    return render(request, 'app_staff/class_schedule.html')

def attendance_view(request):
    return render(request, 'app_staff/attendance.html')

def reports_view(request):
    return render(request, 'app_staff/reports.html')