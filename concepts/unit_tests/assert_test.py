# quick testing or assertion without using heavy modules

def return_boolean(a,b):
    return a == b

# assert True
assert return_boolean(1,2)

# assert False
assert not return_boolean(1,2)

# assert Equals
assert 1 == 1