from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Person, Teacher
from .models import Subject
from .models import Report
from .models import Class
from django.contrib import messages
from django.db.models import Q
@login_required


# Create your views here.
def dashboard_view(request):
    students = Person.objects.all()
    
    if request.method == "GET":
        class_id = request.GET.get('class')
        search_query = request.GET.get('search', '')
        if search_query:
            students = students.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(student_id__icontains=search_query))
        if class_id:
            if class_id == "All Classes":
                students = students
            else:
                students = students.filter(Class_id=class_id)
    
            
    return render(request, 'app_staff/dashboard.html', {'students': students,'search_query': search_query, 'classes': Class.objects.all(), 'selected_class': class_id})

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
            Class_id=Class,
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

def manage_teachers_view(request):
    if request.method == "POST":
        Teacher_id = request.POST.get('teacher_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        subject_id= request.POST.get('subject')
        # age = request.POST.get('age')
        
        subject = Subject.objects.get(id=subject_id)
        
        t = Teacher(teacher_id=Teacher_id, first_name=first_name, last_name=last_name, subject=subject)
        
        # if Teacher.objects.filter(first_name=first_name, last_name=last_name).exists():
            # messages.error(request, "Teacher with this name already exists.")
            # return redirect('/staff/manage_teachers')

        # t = Teacher(first_name=first_name, last_name=last_name, subject=subject)
        t.save()
        

        messages.success(request, "Teacher added successfully!")
        return redirect('/staff/manage_teachers')
    
    
    teachers = Teacher.objects.all()
    
    if request.method == "GET":
        search_query = request.GET.get('search', '')
        if search_query:
            teachers = teachers.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(teacher_id__icontains=search_query))
    return render(request, 'app_staff/man_teachers.html', {'teachers': teachers, 'subjects': Subject.objects.all()})

def edit_teachers_view(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    
    if request.method == "POST":
        teacher.first_name = request.POST.get('first_name')
        teacher.last_name = request.POST.get('last_name')
        subject_id = request.POST.get('subject')
        teacher.status = request.POST.get('status')
        
        subject = Subject.objects.get(id=subject_id)
        teacher.subject = subject
        
        teacher.save()
        
        messages.success(request, "Teacher information updated successfully!")
        return redirect('/staff/manage_teachers')
    
    return render(request, 'app_staff/editteachers.html', {'teachers': Teacher.objects.filter(id=teacher_id), 'teacher': teacher, 'subjects': Subject.objects.all()})

def delete_teacher(request, teacher_id):
    teacher = Teacher.objects.get(id=teacher_id)
    teacher.delete()
    messages.success(request, "Teacher deleted successfully!")
    
    return redirect('/staff/manage_teachers')

def manage_subjects_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        code = request.POST.get('code')
        s = Subject(name=name, code=code)
        if Subject.objects.filter(name=name).exists():
            messages.error(request, "Subject with this name already exists.")
            return redirect('/staff/manage_subjects')
        else:
            s.save()
            messages.success(request, "Subject added successfully!")
            return redirect('/staff/manage_subjects')
    return render(request, 'app_staff/man_subjects.html', {'subjects': Subject.objects.all()})

def edit_subject_view(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    
    if request.method == "POST":
        subject.name = request.POST.get('name')
        subject.code = request.POST.get('code')
        subject.save()
        
        messages.success(request, "Subject information updated successfully!")
        return redirect('/staff/manage_subjects')
    
    return render(request, 'app_staff/editsubject.html', {'subjects': Subject.objects.filter(id=subject_id), 'subject': subject})

def delete_subject(request, subject_id):
    subject = Subject.objects.get(id=subject_id)
    subject.delete()
    messages.success(request, "Subject deleted successfully!")
    
    return redirect('/staff/manage_subjects')

def manage_classes_view(request):
    if request.method == "POST":
        name = request.POST.get('name')
        c = Class(name=name)
        if Class.objects.filter(name=name).exists():
            messages.error(request, "Class with this name already exists.")
            return redirect('/staff/manage-class')
        else:
            c.save()
            messages.success(request, "Class added successfully!")
            return redirect('/staff/manage-class')
    return render(request, 'app_staff/class.html', {'classes': Class.objects.all()})

def delete_class(request, class_id):
    class_instance = Class.objects.get(id=class_id)
    class_instance.delete()
    messages.success(request, "Class deleted successfully!")
    
    return redirect('/staff/manage-class')

def create_report_view(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        term_id  = request.POST.get('term')
        classwork_score = int(request.POST.get('classwork')or 0)
        exam_score = int(request.POST.get('exams') or 0)
        total= int(classwork_score) + int(exam_score)
        if total >= 90:
            grade = 'A'
        elif total >= 80:
            grade = 'B'
        elif total >= 70:
            grade = 'C'
        elif total >= 60:
            grade = 'D'
        else:
            grade = 'F'
        
        student = Person.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)
        
        report = Report(
            student=student,
            subject=subject,
            terms = term_id, 
            classwork=classwork_score,
            exam=exam_score,
            grade=grade,
            total=total)
        report.save()
        
        messages.success(request, "Progress report saved successfully!")
        return redirect('/staff/create-report')
    
    if request.method == "GET":
        class_id = request.GET.get('class')
        term_id = request.GET.get('term')
        subject = request.GET.get('subject')
        students = Person.objects.all()
        
        if class_id:
            if class_id=="All Classes":
                students = students
            else:
                students = students.filter(Class_id=class_id)
        report = Report.objects.filter(subject_id=subject, terms=term_id)if subject and term_id else Report.objects.none()
            
        return render(request, 'app_staff/create_report.html', {'students': students, 'subjects': Subject.objects.all(), 'classes': Class.objects.all(), 'terms': Report.TERM_CHOICES, 'report': report})

def edit_report(request, report_id):
    report = Report.objects.get(id=report_id)
    if request.method == "POST":
        
        report.classwork = int(request.POST.get('classwork') or 0)
        report.exam = int(request.POST.get('exams') or 0)
        if report.classwork + report.exam >= 90:
            report.grade = 'A'
        elif report.classwork + report.exam >= 80:
            report.grade = 'B'
        elif report.classwork + report.exam >= 70:
            report.grade = 'C'
        elif report.classwork + report.exam >= 60:
            report.grade = 'D'
        else:
            report.grade = 'F'
        report.save()
        messages.success(request, "Report updated successfully!")
        return redirect('/staff/reports')
    return render(request, 'app_staff/edit_report.html', {'report': report})

def class_schedule_view(request):
    return render(request, 'app_staff/class_schedule.html')

def attendance_view(request):
    return render(request, 'app_staff/attendance.html')

def reports_view(request):
    if request.method == "POST":
        student_id = request.POST.get('student')
        subject_id = request.POST.get('subject')
        classwork_score = int(request.POST.get('classwork') or 0)
        exam_score = int(request.POST.get('exams') or 0)

        student = Person.objects.get(id=student_id)
        subject = Subject.objects.get(id=subject_id)
        
        report = Report(student=student, subject=subject, classwork=classwork_score, exam=exam_score)
        report.save()
        
        messages.success(request, "Progress report saved successfully!")
        return redirect('/staff/reports')
    return render(request, 'app_staff/reports.html', {'students': Person.objects.all(), 'subjects': Subject.objects.all(), 'reports': Report.objects.all(), 'terms': Report.TERM_CHOICES, 'classes': Class.objects.all()})