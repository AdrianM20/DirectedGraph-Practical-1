"""
validators module

Created on 28.03.2017
Author: @Adrian
"""


class GraphException(Exception):
    pass


class EdgeValidatorException(GraphException):
    pass


class EdgeValidator(object):
    @staticmethod
    def validate(edge):
        if type(edge.source) is not int and edge.source < 0:
            raise EdgeValidatorException("Source should be a positive number.")
        if type(edge.target) is not int and edge.target < 0:
            raise EdgeValidatorException("Target should be a positive number.")
        if type(edge.cost) is not int and edge.cost < 0:
            raise EdgeValidatorException("Cost should be a positive number.")

    @staticmethod
    def validate_cost(cost):
        if type(cost)is not int and cost < 0:
            raise EdgeValidatorException("Cost should be a positive number.")
