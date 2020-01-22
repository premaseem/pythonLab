from random import randint

num_list = []
for num in range(0,10):
    num_list.append(randint(0,1000))
print(num_list)

# one liner list comprehension
comp_num_list = [randint(0, 1000) for num in range(0,10)]

#########################

h_letters = []

for letter in 'human':
    h_letters.append(letter)

print(h_letters)

h_letters = [c for c in 'god']
print(h_letters)

#########################
# list fist 10 even numbers
r = [n for n in range(20) if n%2 == 0 ]
print("even num", r)

#########################
# Example 5: Nested IF with List Comprehension

r = [n for n in range(100) if n % 2 == 0 if n % 5 == 0]
print("common multiple of 5 and 2 ", r)

#########################

obj = ["Even" if i% 2==0 else "Odd" for i in range(10)]
print(obj)


#########################
# compare 2 equal list and populate resultant with smaller numbers
a  = [2,9,4]
b  = [3,5,10]

# for x in a:
#     for y in b:


r = []
for n1,n2 in zip(a,b):
    r.append((n1,n2) [n1 >n2])
    # r.append((n1,n2) if n1>n2 )
    # if n1 < n2:
    #     r.append(n1)
    # else:
    #     r.append(n2)

print(r)

r = [n1 if n1 < n2 else n2 for n1,n2 in zip (a,b)]
print(r)

r = [(n1,n2) [n1 >n2] for n1,n2 in zip(a,b)]
print(r)