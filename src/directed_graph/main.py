"""
main Module

Created on 28.02.2017
@author adiM
"""

import sys
from directed_graph.repositories.file_repo import DirectedGraphFile
from directed_graph.controllers.graph_controller import GraphController
from directed_graph.ui.console import Console
from directed_graph.domain.validators import GraphException, EdgeValidator

if __name__ == "__main__":
    print()

    try:
        directed_graph = DirectedGraphFile(EdgeValidator, "../../data/graph.txt")
        graph_controller = GraphController(directed_graph)
        console = Console(graph_controller)

        console.run_app()

    except GraphException as ge:
        print("An error occurred: ", ge)
        print("Program terminated.")

    print("Good bye!")
