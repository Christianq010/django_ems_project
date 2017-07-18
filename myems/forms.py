from django import forms
from .models import Employee, Salaries

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date')


class SalaryForm(forms.ModelForm):

    class Meta:
        model = Salaries
        fields = '__all__'