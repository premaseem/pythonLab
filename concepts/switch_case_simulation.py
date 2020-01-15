# switch of choice and case of grade assignment
choice = 85
try:
    grade=  {90:"a",80:"b", 70:"c" } [choice]
except:
    grade ="unknown"
print(grade)
try:
    grade=  {90:"a",80:"b", 70:"c" } [choice]
except:
    pass
print("max")
