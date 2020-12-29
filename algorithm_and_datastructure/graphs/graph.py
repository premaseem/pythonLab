import algorithm_and_datastructure.graphs.graph_helper as gh

class Graph:
    def __init__(self,vertexes):
        self.arr = []
        for i in range(vertexes):
            self.arr.append(gh.LinkedList())

    def add_vertex(self):
        self.arr.append(gh.LinkedList())

    def add_edge(self,s,d):
        if s < len(self.arr) and d < len(self.arr):
            ll = self.arr[s]
            ll.add(d)

    def display(self):
        print("Graph display")
        for i,e in enumerate(self.arr):

            print("vertex ", i , " has conneted edge :=> ", end="")
            c = e.head
            while c:
                print(c.data, " - ", end="")
                c = c.next
            print()

    def bfs_traversal_helper(self, g, source, visited):
        result = ""
        queue = gh.Q()
        queue.enqueue(source)
        visited[source] = True # Mark as visited

        # Traverse while queue is not empty
        while len(queue) > 0 :
            # Dequeue a vertex/node from queue and add it to result
            current_node = queue.dequeue()
            result += str(current_node)

            nn = g.arr[current_node].head
            while nn is not None:
                if not visited[nn.data]:
                    queue.enqueue(nn.data)
                    # result += nn.data
                    visited[nn.data] = True
                nn = nn.next
        return result, visited

    def bfs(self,g,source):
        visited = [False] * len(g.arr)
        result, visited = self.bfs_traversal_helper(g,source,visited)

        for i,e in enumerate(visited):
            if not e:
                result_new, visited = self.bfs_traversal_helper(g,i,visited)
                result += result_new
        return result












