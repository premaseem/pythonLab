
def title_decorator(func):
        def decorate():
            print("Program is presented by : PREM ASEEM JAIN")
            func()
            print("like and subscribe")
        return decorate

@title_decorator
def print_story():
    print("This is my love story")
    
print_story()