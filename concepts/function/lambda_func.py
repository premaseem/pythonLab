
# single line function with carries its own scope
def add_total(x):
    print("called first time only", end= " ")
    return lambda x: x + (x * 0.08)

f = add_total(2)
g = add_total(20)
f(1)

print(f(100))

#####################

lambda_func = lambda x,y : x * y

print(lambda_func(2, 6))
print(lambda_func(4, 8))

#####################
# function returning another function / lambda function

def math_op(c):
    if c == 1:
        return lambda x,y:x+y
    else :
        return lambda x,y:x*y

f= math_op(1)
print(f(2,4))

f= math_op(2)
print(f(2,4))

####################

