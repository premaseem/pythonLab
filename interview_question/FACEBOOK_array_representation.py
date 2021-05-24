"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

Given array, [1,2,5,6,8,9,23,34,35,36,45,56,57,58,99]

Represent as = [ 1,2,5-9,23,34-36,45,56-58,99]
and represt complement as = [0, 3, 4, 7, '10-22', '24-33', '37-44', '46-55']
feed values in array,
if value is arr is greater then 2, represent them in string of 0 and -1 element

"""

a = [1,2,5,6,7,8,9,23,26,27,34,35,36,45,56,57,58,99]
ans1 = [ 1,2,5-9,23,34-36,45,56-58,99]

#algo
t = []
ans = []
for e in range(1,100):
    if e in a:
        continue
    if not t or t[-1]+1 == e:
        t.append(e)
    else:
        if len(t) > 2:
            ans.append(str(t[0])+"-"+str(t[-1]))
        else:
            ans.extend(t)
        t = [e]
print(ans)

# main - [1, 2, '5-9', 23, 26, 27, '34-36', 45, '56-58']
# complementary - [3, 4, '10-22', 24, 25, '28-33', '37-44', '46-55']


