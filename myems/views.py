from django.shortcuts import render, get_object_or_404, redirect
from .forms import EmployeeForm
from .models import Employee


def index(request):
    return render (request, 'index.html', {})


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