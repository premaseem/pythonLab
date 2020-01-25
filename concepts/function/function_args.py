def cheeseshop( *argum, **keywords1):
    print("-- Do you have any",  "?")
    for arg in argum:
        print(arg)
    print("-" * 40)
    for kw in keywords1:
        print(kw, ":", keywords1[kw])

cheeseshop("Heart", "dick", "pussy",
           vegina="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

#############################################

def parrot(voltage, state:'a stiff', action:'voom') -> bool:
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")
    return "return"

# unpacked the dictionary
dict = {"state": "a stiff", "action":"voom"}
parrot("a", **dict)

# unpacked the list and passed
lst = ["a","b","c"]
print(parrot(*lst) + parrot(*lst))