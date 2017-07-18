from django.contrib import admin
from .models import (Employee, Departments, DeptEmp, DeptManager, Salaries, Titles)

from .forms import EmployeeForm

class EmployeeAdmin(admin.ModelAdmin):
    form = EmployeeForm
    search_fields = ('emp_no', 'first_name', 'last_name', 'hire_date', 'gender')
    list_display = ('emp_no', 'first_name', 'last_name', 'gender', 'hire_date')
    list_display_links = ('emp_no',)
    # django filter
    list_filter = ('hire_date','gender',)
    
    save_on_top = True
    actions_on_bottom = False
    ordering = ('-hire_date',)

admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Departments)
admin.site.register(DeptEmp)
admin.site.register(DeptManager)
admin.site.register(Salaries)
admin.site.register(Titles)
