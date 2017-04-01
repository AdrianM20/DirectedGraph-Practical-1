"""
validators module

Created on 28.03.2017
Author: @Adrian
"""


class GraphException(Exception):
    pass


class EdgeValidatorException(GraphException):
    pass


class VertexValidatorException(GraphException):
    pass


class EdgeValidator(object):
    @staticmethod
    def validate(edge):
        if type(edge.source) is not int or edge.source < 0:
            raise EdgeValidatorException("Source should be a positive number.")
        if type(edge.target) is not int or edge.target < 0:
            raise EdgeValidatorException("Target should be a positive number.")
        if type(edge.cost) is not int or edge.cost < 0:
            raise EdgeValidatorException("Cost should be a positive number.")

    @staticmethod
    def validate_cost(cost):
        if type(cost) is not int or cost < 0:
            raise EdgeValidatorException("Cost should be a positive number.")


class VertexValidator(object):
    @staticmethod
    def validate(vertex):
        if type(vertex) is not int or vertex < 0:
            raise VertexValidatorException("Vertex should be a positive number.")
