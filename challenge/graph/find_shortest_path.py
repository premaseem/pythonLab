import challenge.graph.graph as gf


# applied breadth first algo
def find_min(g,s,d):
    g.display()
    num_of_vertices = len(g.vertices)

    visited = [False] * num_of_vertices

    distance = [0] * num_of_vertices

    queue = []
    queue.insert(0,s)
    visited[s] = True

    while (len(queue) > 0 ):
        c = queue.pop()
        node_list = g.vertices[c]
        print("looking for all connections from ", c)
        for e in node_list:
            if (not visited[e] or e == d):
                queue.insert(0,e)
                visited[e] = True
                distance[e] = distance[c] +1
                print("current distance",distance)
                if e == d:
                    return distance[d]

    return -1





g = gf.Graph(7)

g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(2, 5)
g.add_edge(5, 6)
g.add_edge(3, 6)

print(find_min(g, 1, 5))

