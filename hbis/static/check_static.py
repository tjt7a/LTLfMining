import re
import sys
import networkx as nx
import matplotlib.colors
import matplotlib.pyplot as plt

# Graph settings
K = 10

def usage():
    """
    Print out usage
    """
    print("Usage: python check_static.py <input HBI file>")

def make_pairs_from_cycle(cycles):
    """
    Convert a cycle of 2 or more nodes into edge pairs
    """
    pairs = set()
    assert len(cycles) > 1, "Provided cycles of fewer than 2 nodes"
    for src in range(-1, len(cycles) - 1):
        pairs.add((cycles[src], cycles[src + 1]))
    return pairs


def draw_graph_with_cycles(pairs):
    """
    Draw directed graph with cycles in red
    """
    G = nx.DiGraph(pairs)
    cycles = nx.recursive_simple_cycles(G)
    print("{} Cycles".format(len(cycles)))
    print(cycles)

    pairs_with_cycles = set()
    for cycle in cycles:
        cycle_pairs = make_pairs_from_cycle(cycle)
        pairs_with_cycles = pairs_with_cycles.union(cycle_pairs)
    
    pairs_without_cycles = pairs - pairs_with_cycles
    print("There are {} rules without cycles".format(len(pairs_without_cycles)))
    POS = nx.spring_layout(G,k=K)

    CMAP = matplotlib.colors.ListedColormap(["black", "matplotlib.colors.red"])
   
    #print("Find a cycle")
    #print(nx.find_cycle(DG))
    nx.draw(G, pos=POS)
    nx.draw_networkx_edges(
        G,
        POS,
        edgelist=pairs_with_cycles,
        width=8,
        alpha=0.5,
        edge_color="tab:red",
    )
    nx.draw_networkx_labels(G, pos=POS, font_size=10, font_family="sans-serif")
    plt.show()



if __name__ == '__main__':

    if len(sys.argv) != 2:
        usage()
        exit(-1)

    HBIs = set()

    # Load pairs from file
    with open(sys.argv[1], 'r') as in_file:
        for line in in_file:
            s = line.split(',')
            first = s[0].strip()
            second = s[1].strip()
            pair = (first, second)
                
            assert pair not in HBIs, "Found pair {} in HBIs".format(pair)
            HBIs.add(pair)
           
    # print out graph with highlighted cycles
    HBIs = draw_graph_with_cycles(HBIs)
