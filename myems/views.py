from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Count,  F

from .forms import EmployeeForm
from .models import Employee, Salaries, generate_next_emp_no, DeptEmp


# Function based View
def my_profile(request, pk):
    profile = get_object_or_404(Employee, pk=pk)

    # save our for data when subbmitted
    if request.method.upper() == 'POST':
        form = EmployeeForm(request.POST, instance=profile)
        if form.is_valid():
            # <process form cleaned data>
            form.save()
            return redirect ('my_profile', pk=pk)

    form = EmployeeForm(instance=profile)
    return render(request, 'profile.html', {'form': form})


def index(request):
    if request.method.upper == 'GET':
        return render (request, 'index.html', {})

# Class based view
class IndexView(View):
    	def get(self, request, *args, **kwargs):
		return render(request, 'index.html', {})


class IndexGenericView(TemplateView):
	template_name = 'index.html'


class ProfileView(View):

	form_class = EmployeeForm
	# initial = {'hire_date': 'TODAY_DATE'}
	template_name = 'my_profile_detail.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class(instance=self.get_context_data().get('profile'))
		return render(request, self.get_template_name(), {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST, instance=self.get_object())
		if form.is_valid():
			# <process form cleaned data>
			form.save()
			return HttpResponseRedirect('/success/')
		return render(request, self.template_name, {'form': form})

	def get_template_name(self):
		"""Returns the name of the template we should render"""
		return self.template_name

	def get_context_data(self):
		"Returns the data passed to the template"""
		return {
			'profile': self.get_object(),
		}

	def get_object(self):
		"""Returns the BlogPost instance that the view displays"""
		return get_object_or_404(Employee, pk=self.kwargs.get('pk'))


class ProfileListView(ListView):
	model = Employee
	template_name = 'profile_list.html'
	paginate_by = 100

	def get_queryset(self):
		order_by_field = self.request.GET.get('order_by') or '-hire_date'
		queryset = super(ProfileListView, self).get_queryset()
		return queryset.order_by(order_by_field)


class ProfileDetailView(DetailView):
	template_name = 'my_profile_detail.html'
	model = Employee
	# pk_url_kwarg = "my_new_id"

	def get_context_data(self, **kwargs):
		context = super(ProfileDetailView, self).get_context_data(**kwargs)
		context['salary_entries'] = Salaries.objects.filter(emp_no__exact=self.object.emp_no)
		return context


class ProfileCreateView(CreateView):
	template_name = 'my_profile_create.html'
	form_class = EmployeeForm
	success_url = reverse_lazy('profile_list')

	def get_initial(self):
		# Get the initial dictionary from the superclass method and fill it up with additional details
		initial = super(ProfileCreateView, self).get_initial()
		initial['emp_no'] = generate_next_emp_no()
		return initial


class ProfileDeleteView(DeleteView):
	model = Employee
	success_url = reverse_lazy('profile_list')

	def get(self, request, *args, **kwargs):
		"""
		Take note this is a hack as we dont want to
		show confirmation page before deleting, By default
		django will try to look for a template called objectname__confirm_delete.html
		"""
		return self.post(request, *args, **kwargs)


class ProfileUpdateView(UpdateView):
	template_name = 'my_profile_update.html'
	model = Employee
	form_class = EmployeeForm
	success_url = reverse_lazy('profile_list')


def employee_dept_stats(request):
	"""
	This is what Django will do based on the query below. Count and group all employees by department
	select dept_name,count(dp_emp.emp_no) as total from dept_emp dp_emp inner join departments dp on 
	dp_emp.dept_no = dp.dept_no group by dept_name; 
	F object expression allows us to convert the dictionary key dept_no__dept_name to something more meaning i.e department_name 
	hence we can then do this empDepartments[0].get('department_name')
	"""
	empDepartments = DeptEmp.objects.all().values('dept_no__dept_name').annotate(total=Count('id'), department_name=F('dept_no__dept_name')).order_by('total')
	return render(request, 'employee_dept_stats.html', {'empDepartments': empDepartments})
