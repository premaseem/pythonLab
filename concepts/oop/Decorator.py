__author__ = 'asee2278'

def interceptor(func):

    def wrapper_func():
        print ("code before call of function")
        func()
        print ("code after call of function")
    return wrapper_func

# def wrapper_func(func):
#     print ("code before call of function")
#     func()
#     print ("code after call of function")
#     return wrapper_func


@interceptor
def main_function():
    print ("I am the main function ")

#main_function = interceptor(main_function)
main_function()

# main_function = interceptor(main_function)
# main_function1 = interceptor(main_function)
# #main_function()
# main_function1()