### Addional Examples of Queries performed in the Django Shell 

* Filtering Data - (case sensitive)
```python
Employee.objects.filter(first_name_icontains='Geo')
```

* Non case sensitive
```python
Employee.objects.filter(first_name_contains='Geo')
```

* Filter Salary data
```python
>>> from myems.models import Salaries
>>>
>>> Salaries.objects.filter(salary__gte=60000)
```

* Filter by Employee Sex
```python
>>> Employee.objects.filter(gender='F')
```
or 

```python
>>> Employee.objects.exclude(gender='M')
```

* Filter by a date range - 
```python
>>> Employee.objects.filter(hire_date__range=["1994-01-01","1994-12-31"])
```

* Return first row of filter

```python
>>> employeeObj = Employee.objects.filter(hire_date__range=["1994-01-01","1994-12-31"]).first()
>>> print employeeObj
>>>
>>> print employeeObj.first_name
```

* Return an employee with a certain id /pk number

```python
>>> Employee.objects.get(pk=10001)
```
