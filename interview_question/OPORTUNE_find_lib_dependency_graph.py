"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

Find the dependency graph of lib which has other dependent libraries.
# algo is mainly breadth first
"""


map = {}
map["A"] = ["B","F"]
map["B"] = ["C"]
map["C"] = ["D", "E"]
map["D"] = ["F"]
map["E"] = []
map["F"] = ["A"]
map["G"] = ["B"]

def get_dependecy(lib):
    mapd = { k:v.copy() for k,v in map.items() }
    ans = []
    queue = []
    queue.extend(mapd.get(lib))


    while queue:
        dlib = queue.pop()

        if dlib not in ans:
            queue.extend(mapd.get(dlib,[]))
        ans.append(dlib)

    return sorted(set(ans))

def get_dependecy2(lib):

    ans = []
    queue = []
    queue.extend(map.get(lib))

    while queue:
        dlib = queue.pop(0)

        if dlib not in ans:
            queue.extend(map.get(dlib, []))
        ans.append(dlib)

    return sorted(set(ans))

print(get_dependecy2("A"))
assert sorted(['A', 'B', 'C', 'D', 'E', 'F']) == get_dependecy2("A")
assert sorted(['A', 'B', 'C', 'D', 'E', 'F']) == get_dependecy("A")

