#VIDEO REFRENCE :- https://www.youtube.com/watch?v=kr0mpwqttM0


# A function is said to be a first class fucntion if it can be stored inside a variable,sent to another function as argument or returned from an fuction

'''
# 1.Storing a function inside a variable

def square(x):
    return x*x

f = square #storing square function inside f variable(not the result of function f)

print(square)
print(f)
print(f(5))

'''

# Note:- A function which accepts other functions as argument or returns a function as result is known as higher order function

'''
# 2.Passing an function as an argument to a fucntion 
def square(x):
    return x*x

def cube(x):
    return x*x*x

def  my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube,[1,2,3,4,5]) 

print(squares)

'''
'''
# 3.return an fuction from an another fuction

Example 1
def logger(msg):
    
    def log_message():
        print('Log:',msg)
    return log_message

log_hi = logger('Hi!')
log_hi()

#Example 2

def html_tag(tag):
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))

    return wrap_text 

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('test_paragraph!')
'''