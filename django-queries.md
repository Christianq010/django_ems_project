### Examples of CRUD Queries performed in the Django Shell 

##### *Reading data*

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


* To handle a case where a value for a query may not exist in the db, we could use a try / catch block for exceptions 
```python
>>> try:
...     Employee.obejects.get(pk=1)
... except Employee.DoesNotExist:
...     print "Sorry! Record not found"
```

##### *Updating data in our database*
```python
>>> employeeObj = Employee.objects.get(pk=10001)
>>> employeeObj.first_name = 'Tim'
>>> employeeObj.save()
```

or 

```python
>>> Employee.objects.filter(first_name='Tim').update(first_name='Timothy')
```

##### *Creating Records*

```python
>>> from feedback.models import Feedback
>>> 
>>> feedback.objects.create(name="Timothy", subject="Check order status")
```

* Multiple entires via a for-loop

```python
>>> myFeedbackList = Feedback.objects.all()
>>> for obj in myfeedbackList:
...     print obj.name
``` 

##### *Removing / Deleting Records*

```python
>>> Employee.objects.filter(first_name='Tim').delete()
```

* Use count to check results 

```python
>>> Employee.objects.filter(first_name='Tim').count()
```

