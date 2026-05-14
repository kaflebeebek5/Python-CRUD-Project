from django.db import models

# Create your models here.

class Student(models.Model):
    studentid   = models.AutoField(primary_key=True)
    name        = models.CharField(max_length=100)
    address     = models.CharField(max_length=100)
    age         = models.IntegerField()
    created_by  = models.IntegerField(null=True, blank=True)
    created_ts  = models.DateTimeField(auto_now_add=True)
    modified_by = models.IntegerField(null=True, blank=True)
    modified_ts = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'students'   # exact table name in your DB
        managed  = False        # Django won't alter your existing table
        ordering = ['name']

class Course(models.Model):
    courseid    = models.AutoField(primary_key=True)
    coursename        = models.CharField(max_length=100)
    teacherid    = models.IntegerField()

    class Meta:
        db_table = 'courses'   # exact table name in your DB
        managed  = False      # Django won't alter your existing table
        ordering = ['coursename']

class Enrollment(models.Model):
    enrollmentid = models.AutoField(primary_key=True)
    studentid    = models.IntegerField()
    courseid     = models.IntegerField()

    class Meta:
        db_table = 'enrollments'   # exact table name in your DB
        managed  = False           # Django won't alter your existing table