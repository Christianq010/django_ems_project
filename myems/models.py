# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()

    def __str__(self):
        return "first_name=%s, last_name=%s" % (self.first_name, self.last_name)

    class Meta:
        db_table = 'employees'


class Departments(models.Model):
    dept_no = models.CharField(primary_key=True, max_length=4)
    dept_name = models.CharField(unique=True, max_length=40)

    class Meta:
        db_table = 'departments'


class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no')
    dept_no = models.ForeignKey(Departments, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)


class DeptManager(models.Model):
    dept_no = models.ForeignKey(Departments, db_column='dept_no')
    emp_no = models.ForeignKey(Employee, db_column='emp_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_manager'
        unique_together = (('emp_no', 'dept_no'),)


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    category = models.CharField(max_length=10)
    email = models.CharField(max_length=150)
    comment = models.CharField(max_length=500)
    is_read = models.BooleanField()
    created_on = models.DateTimeField()

    class Meta:
        db_table = 'feedback'


class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no', related_name='employeeSalaries')
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'salaries'
        unique_together = (('emp_no', 'from_date'),)


class Titles(models.Model):
    emp_no = models.ForeignKey(Employee, db_column='emp_no', related_name='employeeTitles')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'titles'
