"""
file_repo module

Created on 30.03.2017
Author: @Adrian
"""
from directed_graph.domain.edge import Edge
from directed_graph.repositories.graph import DirectedGraph
from directed_graph.domain.validators import GraphException, EdgeValidator
import sys


class FileRepositoryException(GraphException):
    pass


class DirectedGraphFile(DirectedGraph):
    def __init__(self, ValidatorClass, filename):
        super().__init__(ValidatorClass)
        self.__ValidatorClass = ValidatorClass
        self.__filename = filename
        self.load_graph()

    @staticmethod
    def printProgressBar(iteration, total, prefix='', suffix='', decimals=1, length=100, fill='▌'):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int) ███
            total       - Required  : total iterations (Int) ▌
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
        """
        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        filledLength = int(length * iteration // total)
        bar = fill * filledLength + '-' * (length - filledLength)
        sys.stdout.write('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix))
        # Print New Line on Complete
        if iteration == total:
            print()

    def load_graph(self):
        try:
            with open(self.__filename) as f:
                print("\nReading data from file...\n")

                first_line = f.readline().split()
                vertices = int(first_line[0].strip())
                edges = int(first_line[1].strip())
                self.init_data(vertices, edges)
                self.init_vertices()

                div = edges / 50
                i = 0
                if edges == 4000000:
                    self.printProgressBar(i, edges, prefix='Progress: ', suffix='Complete', length=50)

                for line in f:
                    data = line.split(' ')
                    source = int(data[0].strip())
                    target = int(data[1].strip())
                    cost = int(data[2].strip())
                    edge = Edge(source, target, cost)
                    self.save(edge)
                    i += 1
                    if edges == 4000000:
                        if i % div == 0:
                            self.printProgressBar(i, edges, prefix='Progress: ', suffix='Complete!', length=50)

                if edges == 4000000: print()
                print("All data was read. Ready to go!")
                f.close()
        except IOError as io:
            raise FileRepositoryException(io)
