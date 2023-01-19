def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.quantity_calls += 1
        result = func(*args, **kwargs)
        print('{0} was called:{1}x'.format(func.__name__, wrapper.quantity_calls))
        return result

    wrapper.quantity_calls = 0
    return wrapper


@counter
def my_function():
    pass


my_function()
my_function()
my_function()
my_function()
my_function()



#Task
def debag(func):
    def wrapper(arg1, arg2):
        result = func(arg1, arg2)
        print('Run function:' + str(func.__name__) + '(),with param:' + str(arg1) + ',' + str(arg2))

        return 'The result is:', result

    return wrapper


@debag
def summ_(a, b):
    return a + b


print(summ_(3, 5))
