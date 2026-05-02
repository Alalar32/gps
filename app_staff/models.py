from django.db import models

class Class(models.Model):
        name = models.CharField(max_length=20, unique=True)
        is_active = models.BooleanField(default=True)
        

class Person(models.Model):
        student_id = models.CharField(max_length=20)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        age = models.IntegerField()
        Gender = models.CharField(max_length=10)
        pname = models.CharField(max_length=50)
        pcontact = models.CharField(max_length=15)
        pemail = models.EmailField()
        Class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
        
class Subject(models.Model):
        name = models.CharField(max_length=50)
        code = models.CharField(max_length=10, default="SUBJ001")
        
class Teacher(models.Model):
        teacher_id = models.CharField(max_length=20)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        status= models.CharField(max_length=20, default="ACTIVE")
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class Academic_year(models.Model):
        name = models.CharField(max_length=20)
        start_date = models.DateField()
        end_date = models.DateField( null=True, blank=True)
        is_active = models.BooleanField(default=True)
        
class Term(models.Model):
        TERM_CHOICES = [('Term 1', 'Term 1'),
                ('Term 2', 'Term 2'),
                ('Term 3', 'Term 3')]
        name= models.CharField(max_length=10, choices=TERM_CHOICES, null=True, blank=True)
        academic_year= models.ForeignKey(Academic_year, on_delete=models.CASCADE)
        start_date = models.DateField()
        end_date = models.DateField( null=True, blank=True)
        is_active = models.BooleanField(default=True)
        
class Report(models.Model):
        student = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='reports')
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        classwork = models.IntegerField()
        exam = models.IntegerField()
        total = models.IntegerField(null=True, blank=True)
        grade = models.CharField(max_length=2, null=True, blank=True)
        terms = models.ForeignKey(Term, on_delete=models.CASCADE, null=True, blank=True)
