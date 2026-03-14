from django.db import models


class Person(models.Model):
        student_id = models.CharField(max_length=20)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        age = models.IntegerField()
        Class = models.CharField(max_length=20)
        Gender = models.CharField(max_length=10)
        pname = models.CharField(max_length=50)
        pcontact = models.CharField(max_length=15)
        pemail = models.EmailField()