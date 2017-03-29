"""
graph_controller module

Created on 28.03.2017
Author: @Adrian
"""

from src.directed_graph.domain.edge import Edge


class GraphController(object):
    def __init__(self, directed_graph):
        self.__directed_graph = directed_graph

    def get_edge_by_id(self, edge_id):
        if self.__directed_graph.find_edge_by_id(edge_id) is not None:
            return self.__directed_graph.find_edge_by_id(edge_id)
        return None

    def add_edge(self, source, target, cost):
        edge = Edge(source, target, cost)
        self.__directed_graph.save(edge)

    def get_vertices_number(self):
        return self.__directed_graph.get_vertices_number()

    def find_edge(self, source, target):
        edges = self.__directed_graph.get_all_edges()
        for edge in edges:
            if edge.source == source and edge.target == target:
                return edge.edge_id
        return None

    def get_degree(self, vertex):
        in_degree = 0
        out_degree = 0
        for edge in self.__directed_graph.get_all_edges():
            if edge.source == vertex:
                out_degree += 1
            if edge.target == vertex:
                in_degree += 1
        return in_degree, out_degree

    def get_endpoints(self, edge_id):
        source, target = None, None
        for edge in self.__directed_graph.get_all_edges():
            if edge.edge_id == edge_id:
                source = edge.source
                target = edge.target
        return source, target
