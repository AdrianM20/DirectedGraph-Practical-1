"""
graph module

Created on 28.03.2017
Author: @Adrian
"""

from directed_graph.domain.validators import GraphException


class DirectedGraphException(GraphException):
    pass


class DirectedGraph(object):
    def __init__(self, validator_class, n_vertices, n_edges):
        self.__validator_class = validator_class
        self.__n_vertices = n_vertices
        self.__n_edges = n_edges
        self.__vertices = self.__initialize_vertices()
        self.__edges = {}

    def __initialize_vertices(self):
        vertices_list = []
        for i in range(0, self.__n_vertices):
            vertices_list.append(i)
        return vertices_list

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

    def delete_edge_by_id(self, edge_id):
        # TODO implement a delete function to delete an edge by its ID
        pass

    def delete_by_vertex(self, vertex):
        # TODO implement a delete function to delete a vertex and all its adjacent edges
        pass

    def update_cost(self, edge_id, new_cost):
        if self.find_edge_by_id(edge_id) is None:
            raise DirectedGraphException("Edge with id {0} does not exist. Nothing was updated.".format(edge_id))
        self.__validator_class.validate_cost(new_cost)
        self.__edges[edge_id].cost = new_cost

    def get_vertices_number(self):
        return self.__n_vertices

    def get_all_edges(self):
        return self.__edges.values()
