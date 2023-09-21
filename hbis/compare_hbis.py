import re
import sys
import networkx as nx

def usage():
    print("Usage: python compare_hbis.py <input file 1> <input file 2>")

def load_pairs_from_file(filename, delimiter=' '):
    hbis = set()
    with open(filename, 'r') as file:
        for line in file:
            s = line.split(delimiter)
            first = s[0].strip()
            second = s[1].strip()
            pair = (first, second)

            assert pair not in hbis, "Found pair {} in hbi set in file {}".format(pair, filename)
            hbis.add(pair)
    return hbis

if __name__ == '__main__':

    if len(sys.argv) != 3:
        usage()
        exit(-1)
    
    first_filename = sys.argv[1]
    second_filename = sys.argv[2]

    first_hbis = load_pairs_from_file(first_filename, ' ')
    second_hbis = load_pairs_from_file(second_filename, ',')

    # Summarize
    print("Filename:{}, Number of Unique HBIs:{}".format(first_filename, len(first_hbis)))
    print("Filename:{}, Number of Unique HBIs:{}".format(second_filename, len(second_hbis)))

    intersection_hbis = first_hbis.intersection(second_hbis)
    print("Intersection has {} HBIs".format(len(intersection_hbis)))
