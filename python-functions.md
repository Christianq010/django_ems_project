## *python functions* 
* `*args` - argument
* `*kwargs` - keyword argument 
* `(*argument)` - python unpacks the dictionary to be interpretted in an argument.

```python

def print_args_individual(value1, value2):
	print '{0}, {1}'.format(value1, value2)


print_args_individual('cat', 'dog')


def print_kwargs_individual(value1=1, value2=2):
	print '{0}, {1}'.format(value1, value2)


print_kwargs_individual()


def print_args(*args):
	"""
	Allows you to handle arguments that have not been defined
	Serves as a preventive measure to prevent program from crashing
	i.e we can add remove passed arguments and shouldnt cause program to crash
	"""
	for index_value, actual_value in enumerate(args):
		print '{0}. {1}'.format(index_value, actual_value)


print_args('cat', 'dog', 'fish', 'mouse', 'abc')


def print_kwargs(**kwargs):
	for name, value in kwargs.items():
		print '{0} = {1}'.format(name, value)


print_kwargs(dog='pet', fish='pet', orange='fruit', apple='fruit')


def print_args_kwargs(*args, **kwargs):
	"""
	You can also use both in the same function definition but
	*args must occur before **kwargs.
	"""
	print_args(*args)
	print_kwargs(**kwargs)


print_args_kwargs('cat', 'dog', 'fish', dog='pet', fish='pet', orange='fruit')


def print_three_things(value1, value2, value3):
	"""
	You can also use the * and ** syntax when calling a function
	"""
	print 'value1 = {0}, value2 = {1}, value3 = {2}'.format(value1, value2, value3)


list_of_random_things = ['books', 'pants', 'chromecast']

print_three_things(*list_of_random_things)

```