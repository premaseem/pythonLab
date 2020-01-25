# switch of choice and case of grade assignment
choice = 90
try:
    grade=  {90:print("ais win"),80:"b", 70:"c" } [choice]
except:
    grade ="unknown"
print(grade)
try:
    grade=  {90:"a",80:"b", 70:"c" } [choice]
except:
    pass
print("max")

marks=99
result = ("Fail", "Pass")[marks > 70]
print(result)
