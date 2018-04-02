class Vertex(object):
    def __init__(self, key):
        self.key = key


class Graph(object):
    def __init__(self, graph=None, directed=False, weighted=False):
        """Initializes a Graph using the adjacency list representation.

        The adjacency list representation has the following runtimes:
            adjacent(v, u)  O(deg(v))
            neighbours(v)   O(deg(v))
            insert(v, u)    O(deg(v))
        It uses O(V+E) memory.
        
        Parameters:
        ----------
        graph : {dict}
            A dictionary whose keys are the nodes of the graph. 
            For each key, the corresponding value is a list containing
            the nodes that are connected by a direct arc from this node.
        directed : {bool}, optional
            Whether or not the graph is directed (the default is False, which gives an undirected graph).
        """
        if graph is None:
            self._adjacency_list = {}
        else:
            self._adjacency_list = {Vertex(k): [] for k in graph.keys()}
            for k, vs in graph.items():
                for v in vs:
                    self._adjacency_list
        self.directed = directed

    def adjacent_vertices(v, u):
        """Checks if the vertices v and u are adjacent.

        In a graph, two vertices are said to be adjacent, if there
        is an edge between the two vertices. Here, the adjacency of
        vertices is maintained by the single edge that is connecting
        those two vertices.

        Parameters:
        ----------
        v : {str}
            The key of the first vertex
        u : {str}
            The key of the second vertex
        Returns
        -------
        bool
            Boolean of adjacency
        """
        return u in self._adjacency_list[v] or v in self._adjacency_list[u]

    def adjacent_edges(e, f):
        """Checks if the edges e and f are adjacent.

        In a graph, two edges are said to be adjacent, if there
        is a common vertex between the two edges. Here, the adjacency
        of edges is maintained by the single vertex that is connecting
        two edges.

        Parameters:
        ----------
        v : {str}
            The first edge
        u : {str}
            The second edge
        Returns
        -------
        bool
            Boolean of adjacency
        """
        are_adjacent = False
        #for e1 in self._adjacency_list.

    def neighbours(self, v):
        """Returns all neighbours of the vertex v.
        
        Parameters:
        ----------
        v : {str}
            The vertex
        """
        return self._adjacency_list[v]

    def insert(self, vertex, connected_vertices):
        """Inserts a vertex in the graph with the given edges.
        
        Parameters:
        ----------
        vertex : {str}
            The vertex to insert.
        connected_vertices : {list}
            The vertices to establish edges to from the inserted vertex.
        """
        self._adjacency_list[vertex] = connected_vertices
        if not self.directed:
            for v in connected_vertices:
                self._adjacency_list[v].append(vertex)

    def add_edge(self, v, u):
        """Adds an edge between vertices v and u.
        
        Parameters:
        ----------
        v : {str}
            Vertex v
        u : {str}
            Vertex u
        """
        assert v in self._adjacency_list and u in self._adjacency_list
        self._adjacency_list[v].append(u)
        if not self.directed:
            self._adjacency_list[u].append(v)

    def degree(self, vertex):
        """Returns the degree of a vertex.

        If the graph is directed, a tuple of the indegree and outdegree is returned.

        Parameters:
        ----------
        vertex : {str}
            The vertex the degree of which to compute and return

        Returns
        -------
        [type]
            [description]
        """
        if self.directed:
            outdegree = len(self.graph[vertex])
            indegree = 0
            for edge in self._adjacency_list.items():
                if vertex in edge:
                    indegree += 1
            return (indegree, outdegree)
        else:
            return len(self.graph[vertex])

    def display_vertex(self, v):
        print(self._adjacency_list[v])

    def display_graph(self):
        for v in self._adjacency_list.keys():
            self.display_vertex(v)

    def breath_first_search(self, v):
        stack = [v]



class DirectedGraph(object):
    pass
