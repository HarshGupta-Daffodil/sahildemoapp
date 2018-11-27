

def get_name(func):
	"""
	Decorator  to getb the name of the function and its arguments
	"""
	def func_wrapper(*args, **kwargs):
		return "{},{}".format(func.__name__, *args, **kwargs)
	return func_wrapper


@get_name
def get_text(name):
	return ""


def squre_of_number(number):
	"""
	Function to obtain the Squre of 10 number
	:number		integer

	rtype		instance
	"""
	obj = (x*x for x in range(number, number+11))
	print "Square of number : "
	for i in obj:
		print i
	return obj


def series_of_number(number1, number2):
	"""
	Function to create a series of number fromm number1 to number2

	:number1		integer
	number2			integer

	rtype			instance
	"""
	obj = (x for x in range(number1, number2+1))
	print "Series of number : "
	for i in obj:
		print i
	return obj

squre_of_number(1)
series_of_number(1, 10)
print get_text("sahil")
