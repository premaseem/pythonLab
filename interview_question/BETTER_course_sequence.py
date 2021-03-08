"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

You're developing a system for scheduling advising meetings with students in a Computer Science program. Each meeting should be scheduled when a student has completed 50% of their academic program.

Each course at our university has at most one prerequisite that must be taken first. No two courses share a prerequisite. There is only one path through the program.

Write a function that takes a list of (prerequisite, course) pairs, and returns the name of the course that the student will be taking when they are halfway through their program. (If a track has an even number of courses, and therefore has two "middle" courses, you should return the first one.)

Sample input 1: (arbitrarily ordered)
prereqs_courses1 = [
	["Foundations of Computer Science", "Operating Systems"],
	["Data Structures", "Algorithms"],
	["Computer Networks", "Computer Architecture"],
	["Algorithms", "Foundations of Computer Science"],
	["Computer Architecture", "Data Structures"],
	["Software Design", "Computer Networks"]
]

In this case, the order of the courses in the program is:
	Software Design
	Computer Networks
	Computer Architecture
	Data Structures
	Algorithms
	Foundations of Computer Science
	Operating Systems

Sample output 1:
	"Data Structures"


Sample input 2:



Sample output 2:
	"Algorithms"

Sample input 3:
prereqs_courses3 = [
	["Data Structures", "Algorithms"],
]


Sample output 3:
	"Data Structures"

Complexity analysis variables:

n: number of pairs in the input


"""








def sol(l):
    m = {}
    ans = []
    for e in l:
        m.setdefault(e[0],e[1])
    #     print("map",m )

    starter = ""
    for k in m.keys():
        if k not in m.values():
            starter = k

    #     print(starter)

    ans.append(starter)
    for i in range(len(m)):
        d = m.get(ans[i])
        ans.append(d)

    print(ans)
    mid = len(ans)//2
    if len(ans) %2 == 0:
        mid = mid - 1
    print("print ans", ans[mid])
    return ans[mid]


prereqs_courses1 = [
    ["Foundations of Computer Science", "Operating Systems"],
    ["Data Structures", "Algorithms"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]


prereqs_courses2 = [
    ["Data Structures", "Algorithms"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Foundations of Computer Science", "Logic"]
]

prereqs_courses3 = [
    ["Data Structures", "Algorithms"]
]



test_data = [
    (prereqs_courses1, "Data Structures"),
    (prereqs_courses2, "Algorithms"),
    (prereqs_courses3, "Data Structures"),
    ([], ""),
]

for given, expected in test_data:
    print(f"Test for: given {given} and expected = {expected}", end="\n\n")
    assert expected == sol(given)
