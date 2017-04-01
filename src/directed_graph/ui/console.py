"""
consol module

Created on 30.03.2017
Author: @Adrian
"""

from directed_graph.domain.validators import GraphException


class Console(object):
    def __init__(self, graph_controller):
        self.__graph_controller = graph_controller

    def run_app(self):
        options = {1: self.__UI_add_vertex,
                   2: self.__UI_delete_vertex,
                   3: self.__UI_add_edge,
                   4: self.__UI_delete_edge}

        self.__greet_user()
        self.__graph_controller.load_from_file()

        while True:
            self.__print_menu()
            option = input("|| Enter Option:")
            if option == 'x':
                break
            try:
                option = int(option)
                options[option]()
            except ValueError as ve:
                print("Invalid input: ", ve)
            except KeyError as ke:
                print("Feature not implemented. Try another one.", ke)
            except GraphException as ge:
                print("An error occurred: ", ge)
                print("Try again.")

    @staticmethod
    def __print_menu():
        print("\n||----------Choose an option--------------||")
        print("||  1 - Add vertex                        ||")
        print("||  2 - Delete vertex                     ||")
        print("||  3 - Add edge                          ||")
        print("||  4 - Delete edge                       ||")
        print("||  5 - Print number of vertices          ||")
        print("||  6 - Print in and out degree of vertex ||")
        print("||  7 - Find edge                         ||")
        print("||  8 - Print endpoints of edge           ||")
        print("||  9 - Print cost of edge                ||")
        print("|| 10 - Modify cost of edge               ||")
        print("|| 11 - Print outbound edges              ||")
        print("|| 12 - Print inbound edges               ||")
        print("||  x - Exit program                      ||")
        print("||----------Choose an option--------------||")

    @staticmethod
    def __greet_user():
        print("Directed Graph v1.3")
        print("The program is menu-based.")
        print("Use the menu options to operate the program.")

    def __UI_add_vertex(self):
        vertex = int(input("Vertex ID: "))
        self.__graph_controller.add_vertex(vertex)

    def __UI_delete_vertex(self):
        vertex = int(input("Vertex ID: "))
        self.__graph_controller.delete_vertex(vertex)

    def __UI_add_edge(self):
        source = int(input("Edge source: "))
        target = int(input("Edge target: "))
        cost = int(input("Edge cost: "))
        self.__graph_controller.add_edge(source, target, cost)

    def __UI_delete_edge(self):
        edge_id = input("Edge ID: ")
        self.__graph_controller.delete_edge(edge_id)
