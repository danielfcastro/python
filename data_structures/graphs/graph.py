class Graph:

    def __init__(self, vertexes):
        self._vertexes = vertexes
        self._graph = [[0] * vertexes for i in range(vertexes)]
        self._visited = [False] * vertexes

    def add_edge(self, u, v):
        #adjacent list
        #self._graph[u - 1].append(v - 1)
        self._graph[u - 1][v - 1] = 1
        self._graph[v - 1][u - 1] = 1

    def show_list_adjacence(self):
        print('Adjacent List')
        for i in range(self._vertexes):
            print('%d: ' % (i + 1), end=' ')
            for j in self._graph[i]:
                print('%d -> ' % (j + 1), end=' ')
            print('')

    def depth_first_search(self, start):
        # list of visited nodes
        self._visited[start - 1] = True
        print('%d visited' % start)
        for i in range(1, self._vertexes + 1):
            #checks if there is edge linking start with i and it was not yet visited
            if self._graph[start - 1][i - 1] == 1 and self._visited[i - 1] == False:
                #if so recursive call
                self.depth_first_search(i)

    def breadth_first_search(self, v):

        # list of visited nodes
        visited = [False] * self._vertexes
        # mark 'v' as a visited node
        visited[v - 1] = True
        # adds 'v' into queue
        queue = [v - 1]

        print('%d visited' % v)

        # while queue is not empty
        while len(queue) > 0:

            # get the elemento of queue
            v = queue[0]

            # for each vertex 'u' adjacent to 'v'
            for u in range(self._vertexes):
                # vchecks if there is edge
                if self._graph[v][u] == 1:
                    # checks if 'u' was not visited
                    if visited[u] == False:
                        # mark 'u' as visited
                        visited[u] = True
                        # adds 'u' into queue
                        queue.append(u)
                        # prints
                        print('%d visited' % (u + 1))

            # remove 'v' from queue
            queue.pop(0)