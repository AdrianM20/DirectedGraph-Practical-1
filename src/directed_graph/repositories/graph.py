"""
graph module

Created on 28.03.2017
Author: @Adrian
"""

from directed_graph.domain.validators import GraphException, VertexValidator


class DirectedGraphException(GraphException):
    pass


class DirectedGraph(object):
    def __init__(self, validator_class):
        self.__validator_class = validator_class
        self.__n_vertices = None
        self.__n_edges = None
        self.__vertices = None
        self.__edges = {}

    def init_data(self, vertices, edges):
        self.__n_vertices = vertices
        self.__n_edges = edges

    def init_vertices(self):
        vertices_list = []
        for i in range(0, self.__n_vertices):
            vertices_list.append(i)
        self.__vertices = vertices_list

    def find_edge_by_id(self, edge_id):
        if edge_id in self.__edges.keys():
            return self.__edges[edge_id]
        return None

    def save(self, edge):
        if self.find_edge_by_id(edge.edge_id) is not None:
            raise DirectedGraphException("Edge with id {0} already exists. Nothing was added".format(edge.edge_id))
        if edge.source not in self.__vertices:
            raise DirectedGraphException("Source vertex does not exist. Cannot add edge.")
        if edge.target not in self.__vertices:
            raise DirectedGraphException("Target vertex does not exist. Cannot add edge.")
        self.__validator_class.validate(edge)
        self.__edges[edge.edge_id] = edge
        self.__n_edges += 1

    def save_vertex(self, vertex):
        if vertex in self.__vertices:
            raise DirectedGraphException("Vertex already exists. Nothing was added.")
        VertexValidator.validate(vertex)
        self.__vertices.append(vertex)

    def delete_edge_by_id(self, edge_id):
        if self.find_edge_by_id(edge_id) is None:
            raise DirectedGraphException("Edge with id {0} does not exist. Nothing was deleted".format(edge_id))
        del self.__edges[edge_id]
        self.__n_edges -= 1

    def delete_by_vertex(self, vertex):
        if vertex not in self.__vertices:
            raise DirectedGraphException("Vertex does not exist. Nothing was deleted.")
        for i in range(0, self.__n_vertices):
            if self.__vertices[i] == vertex:
                del self.__vertices[i]
                self.__n_vertices -= 12
                break
        edges = list(self.get_all_edges())
        for edge in edges:
            if edge.source == vertex or edge.target == vertex:
                del self.__edges[edge.edge_id]

    def update_cost(self, edge_id, new_cost):
        if self.find_edge_by_id(edge_id) is None:
            raise DirectedGraphException("Edge with id {0} does not exist. Nothing was updated.".format(edge_id))
        self.__validator_class.validate_cost(new_cost)
        self.__edges[edge_id].cost = new_cost

    def get_vertices_number(self):
        return self.__n_vertices

    def get_all_edges(self):
        return self.__edges.values()
