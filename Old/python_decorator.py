"""
def decorator(some_function):

        def wrapper():
                print('Before some_function')
                some_function()
                print('After some_function')


        return wrapper


@decorator
def prints_hello():
	print('Hello')


prints_hello()
"""


import time

def get_runtime_decorator(function):


	def wrapper():
		time_start = time.time()
		print('Start time: {}'.format(time_start))
		function()
		time_end = time.time()
		print('End time: {}'.format(time_end))
		time_taken = time_end - time_start
		print('Total time taken: {}'.format(time_taken))

	return wrapper


@get_runtime_decorator
def some_long_service():
	num_list = []
	for num in (range(0, 100000)):
		num_list.append(num)
	print("\nSum of all the numbers: " + str((sum(num_list))))


some_long_service()

######################################################################################

def logger(f):
  def log_printer(lst):
    print("[INFO] Logging.")
    return f(lst)
  
  return log_printer
  
@logger
def sum_values(values):
  return sum(values)
  
print(sum_values([1, 2, 3, 4]))
