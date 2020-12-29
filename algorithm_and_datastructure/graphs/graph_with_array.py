class Graph:
    def __init__(self,num):
        self.vertices = []
        for i in range(num):
            self.vertices.append(list())

    def add_edge(self,s,d):
        self.vertices[s].insert(0,d)

    def display(self):
        for i, arr in enumerate(self.vertices):
            print(i, ": ", arr )

    def bfs(self,s,visited):
        s_arr = self.vertices[s]
        r = ""
        q = []
        q.insert(0,s_arr)
        r += str(s)
        visited[s] = True

        while len(q) > 0:
            cn = q.pop()
            for e in cn:
                if not visited[e]:
                    r += str(e)
                    q.insert(0, self.vertices[e])
                    visited[e] = True

        # print(r)
        return r, visited

    def traverse_bf(self,s):
        visited = [False] * len(self.vertices)
        r, visited = self.bfs(s,visited)
        for i, e in enumerate(visited):
            if not e:
                n_r, visited = self.bfs(i,visited)
                r += n_r
        print(r)
        return r

    def dfs(self,s,visited):
        s_arr = self.vertices[s]
        r = ""
        q = []
        q.append(s_arr)
        r += str(s)
        visited[s] = True

        while len(q) > 0:
            cn = q.pop()
            for e in cn:
                if not visited[e]:
                    r += str(e)
                    q.insert(0, self.vertices[e])
                    visited[e] = True

        # print(r)
        return r, visited

    def traverse_df(self,s):
        visited = [False] * len(self.vertices)
        r, visited = self.dfs(s,visited)
        for i, e in enumerate(visited):
            if not e:
                n_r, visited = self.dfs(i,visited)
                r += n_r
        print(r)
        return r

g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
# g.display()
# expect = 0231
print("bfs traverse", g.traverse_bf(0))

g1 = Graph(7)

g1.add_edge(1, 2)
g1.add_edge(1, 3)
g1.add_edge(2, 4)
g1.add_edge(2, 5)
g1.add_edge(3, 6)
# expect = 1360254
print(g1.traverse_df( 1))

# g = Graph(5)
# g.add_edge(0,1)
# g.add_edge(0,3)
# g.add_edge(2,3)
# g.add_edge(1,4)
# g.add_edge(3,1)
# g.add_edge(3,4)
# g.add_edge(4,0)
#
# # g.display()
# g.traverse_bf(0)

