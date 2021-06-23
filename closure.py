#VIDEO REFRENCE :- https://www.youtube.com/watch?v=swU3c34d2NQ
'''

def outer_func():
    message = 'HI'

    def inner_func():
        print(message) #message variable here is known as free variable

    return inner_func

my_func = outer_func()

print(my_func.__name__)
my_func()
my_func()
my_func()
'''

'''
def outer_func(msg):
    message = msg

    def inner_func():
        print(message)

    return inner_func

hi_func = outer_func('hi')
hello_func = outer_func('hello')

hi_func()
hello_func()
'''