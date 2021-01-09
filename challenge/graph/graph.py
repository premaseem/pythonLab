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

    def traverse_breath(self,s):
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

    def traverse_depth(self, s):
        visited = [False] * len(self.vertices)
        r, visited = self.dfs(s,visited)
        for i, e in enumerate(visited):
            if not e:
                n_r, visited = self.dfs(i,visited)
                r += n_r
        print(r)
        return r


