# objective is to learn different type of print statements and option

kind = "good"
weight = 140
# simple
print("aseem is a good man")

# multi line print
print(""" Aseem jain
is really 
a good person""")

# new line and tabbed
print("aseem is \t a good \n man")

# concat vars with +
print("aseem jain is a "+ kind + " man.")

# interpolate with ,
print("aseem jain is a ", kind , " man.")


# in the same line
print("aseem is a good man", end= " ")
print("after end")

# with variable
print("aseem is a good man weight", weight)

# with format
print("aseem is a {} man with {} pounds weight".format(kind, weight))

# with printf
print(f"aseem is a {kind} man with {weight} lbs")

# with variables place holders
print("aseem is a {k} man with {w} pounds weight".format(w=weight,k=kind))

# print emoji or speical chars
a = '😄'
b = '🥰'
print(a+b)
