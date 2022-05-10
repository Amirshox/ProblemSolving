class Graph(object):
    def __init__(self, graph_dict):
        if graph_dict is None:
            graph_dict = {}

        self.graph_dict = graph_dict

    def vertices(self):
        return list(self.graph_dict.keys())

    def edges(self):
        return self.__get_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = vertex2

    def __get_edges(self):
        edges = []
        for vertex in self.graph_dict:
            for neighbor in self.graph_dict[vertex]:
                if {neighbor: vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def get_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path = []

        graph = self.graph_dict
        path = path + [start_vertex]

        if start_vertex not in graph:
            return None

        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.get_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
                else:
                    return None


g = {
    "a": ["c", "f", "b"],
    "b": ["a", "c", "d"],
    "c": ["f", "a", "b"],
    "d": ["b", "c", "e"],
    "e": ["f", "d"],
    "f": ["e", "c", "a"],
}

my_graph = Graph(g)
