from django.db import models

class Class(models.Model):
        name = models.CharField(max_length=20)
        

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
        
class Report(models.Model):
        student = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='reports')
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        classwork = models.IntegerField()
        exam = models.IntegerField()
        total = models.IntegerField(null=True, blank=True)
        grade = models.CharField(max_length=2, null=True, blank=True)
        TERM_CHOICES = [('Term 1', 'Term 1'),
                ('Term 2', 'Term 2'),
                ('Term 3', 'Term 3')]
        terms= models.CharField(max_length=10, choices=TERM_CHOICES, null=True, blank=True)
