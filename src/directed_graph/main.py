"""
main Module

Created on 28.02.2017
@author adiM
"""

from src.directed_graph.domain.edge import Edge
import sys


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '▌'):
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


if __name__ == "__main__":
    try:
        with open("../../data/graph1m.txt") as f:
            Edges = []
            print("\nReading data from file...\n")
            first_line = f.readline()
            i = 0
            printProgressBar(i, 4000000, prefix='Progress:', suffix='Complete', length=50)
            for line in f:
                args = line.split(' ')
                source = int(args[0].strip())
                target = int(args[1].strip())
                cost = int(args[2].strip())
                edge = Edge(source, target, cost)
                Edges.append(edge)
                i += 1
                if i % 80000 == 0:
                    # print("\r" + str(counter // 40000) + "%")
                    # sys.stdout.write("\r%d%%" % i)
                    printProgressBar(i, 4000000, prefix='Progress:', suffix='Complete', decimals=0, length=50)
            print()
            print("All data was read. Good bye!")
            f.close()
    except IOError as io:
        print("Cannot read.", io)
