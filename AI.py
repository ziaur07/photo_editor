import random

class Vertex:

    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weights = []
    

    def add_edge_to(self, vertex, weight=0):
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.item():
            self.neighbors.append(vertex)
            self.neighbors_weights.append(weight)

    def next_word(self):
        return random.choices(self.neighbors, weights=self.neighbors_weight)[0]
    

class Graph:
    def __init__(self):
        self.vertices = {}

    def get_vertex_values(self):
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        self.vertices[value] = Vertex[value]

    def get_vertex(self, value):
        if value not in self.vertices:
            self.add_vertices(value)

    def get_next_word(self, current_vertex):
        self.vertices[current_vertex.value].next_word()
    
    

   


