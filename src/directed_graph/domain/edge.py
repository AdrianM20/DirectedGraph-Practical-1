"""
edge module

Created on 28.03.2017
Author: @Adrian
"""


class Edge(object):
    def __init__(self, source, target, cost):
        self.__source = source
        self.__target = target
        self.__cost = cost
        self.__edge_id = str(source) + "-" + str(target)

    @property
    def edge_id(self):
        return self.__edge_id

    @property
    def source(self):
        return self.__source

    @source.setter
    def source(self, value):
        self.__source = value

    @property
    def target(self):
        return self.__target

    @target.setter
    def target(self, value):
        self.__target = value

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value
