"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

You have to implement the trace_path() function which will take in a list of source-destination pairs and return the correct sequence of the whole journey from the first city to the last.

Input:
dict = {
  "NewYork": "Chicago",
  "Boston": "Texas",
  "Missouri": "NewYork",
  "Texas": "Missouri"
}

Output:
[["Boston", "Texas"] , ["Texas", "Missouri"] , ["Missouri", "NewYork"] , ["NewYork", "Chicago"]]

# iterate map key and value for next would be key for next, append the pair
"""
cities = {
    "NewYork": "Chicago",
    "Boston": "Texas",
    "Missouri": "NewYork",
    "Texas": "Missouri"
}

path = []
def trace_path(s,d):
    while s != d:
        r = cities.get(s)
        path.append([s,r])

        if r == d:
            break
        # to avoid infinite loop
        if len(path) > len(cities):
            break
        s = r

trace_path("Boston", "NewYork1" )
print(path)



