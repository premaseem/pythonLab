import algorithm_and_datastructure.graphs.graph_helper as gh
import algorithm_and_datastructure.graphs.graph as gf


g = gf.Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
# g.display()

print("bfs traverse", g.bfs(g,0))
#####################

g = gf.Graph(7)

g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)
print(g.dfs_traversal(g, 1))
