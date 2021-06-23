#Video Refrence:- https://www.youtube.com/watch?v=FsAPt_9Bf3U

'''
#revision of closure and function
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)
    return inner_function

hi_func = outer_function('hi')
my_func = outer_function('bye')

hi_func()
my_func()
'''

'''
# Decorator :- A decorator is just a funciton which take another function as an argument adds some kind of functionality and returns the function all this without altering the source code of the original function

def decorator_function(original_function):
    def wrapper_function():
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function()
    return wrapper_function

def display():
    print('display function ran')

decorator_display = decorator_function(display)
decorator_display()
'''

'''
#CLASSES AS DECORATORS

class decorator_class(object):
    def __init__(self, original_function):
        self.original_function = original_function

    def __call__(self,*args,**kwargs):
        print("call method executed this before {}".format(self.original_function.__name__))
        return self.original_function(*args,**kwargs)

@decorator_class
def display():
    print('display function ran')    

@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('john', 25)

display()
'''
'''
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("wrapper executed this before {}".format(original_function.__name__))
        return original_function(*args,**kwargs)
    return wrapper_function

@decorator_function
def display():
    print('display function ran')    

@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('john', 25)

display()
'''
'''
def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level = logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs:{}'.format(args,kwargs)
        )
    
    return wrapper

def my_timer(orig_func):
    import time

    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in : {} sec'.format(orig_func.__name__,t2))
        return result
    
    return wrapper

import time
@my_timer
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('john', 25)


 '''







