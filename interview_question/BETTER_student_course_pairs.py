"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""


def sol(student_course_pairs_1):
    m = {}
    for sid,c in student_course_pairs_1:
        course = m.setdefault(sid,set())
        course.add(c)

    print("course map", m )

    students = list(m.keys())
    print("students list ",students)
    pairs = []
    courses = []
    ans = []
    for i in range(len(students)):
        for j in range(i+1,len(students)):
            pairs.append([students[i],students[j]])
            s1 = m.get(students[i])
            s2 = m.get(students[j])
            common = s1.intersection(s2)
            print(common)
            name = str(students[i]) + " " + str(students[j])
            value = list(common)
            ans.append([ name, value ])

    return ans


