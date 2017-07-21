from django.utils import timezone
from django import forms
from .models import Employee, Salaries
from django.utils.safestring import mark_safe


class AdminImageFieldWidget(forms.widgets.FileInput):
    	def __init__(self, placeholder='/images/profile/placeholder.thumbnail.jpg'):
		self.placeholder = placeholder
		super(AdminImageFieldWidget, self).__init__({})

	def render(self, name, image, attrs=None):
		render_html = '<img src="%s"/>' % (image.thumbnail.url) if image and hasattr(image, "url") else '<img src="%s"/>' % (self.placeholder)
		return mark_safe("%s%s" % (render_html, super(AdminImageFieldWidget, self).render(name, image, attrs)))


class EmployeeForm(forms.ModelForm):

	# Its important when you use SelectDateWidget to specify the year as it will only show
	# Future years from today not past
	hire_date = forms.DateField(widget=forms.SelectDateWidget(years=range(1980, 2025)), initial=timezone.now)

	birth_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))

	image = forms.ImageField(label='Profile Image', widget=AdminImageFieldWidget(), required=False)

	class Meta:
		model = Employee
		fields = ('emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date', )



class SalaryForm(forms.ModelForm):

    class Meta:
        model = Salaries
        fields = '__all__'