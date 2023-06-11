import os
import sys
from math import sqrt
import networkx as nx
import json


class Node:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.edges = []
        self.visited = False
    def add_edge(self, node):
        self.edges.append(node)


class MST:
    def __init__(self, max_range):
        self.V = 0
        self.max_range = max_range
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)
        self.V += 1

    def add_edge(self, node1, node2):
        self.edges.append((node1, node2))

    def get_node(self, col, row):
        # no se puede asumir orden de los nodos
        for node in self.nodes:
            if node.col == col and node.row == row:
                return node
        return None

    def manhattan_distance(self, node1, node2):
        return abs(node1.col - node2.col) + abs(node1.row - node2.row)

    def dfs_iterative(self, node):
        stack = [node]
        cost = 0
        while stack:
            node = stack.pop()
            if not node.visited:
                node.visited = True
                for edge in node.edges:
                    if not edge.visited:
                        stack.append(edge)
                        cost += self.manhattan_distance(node, edge)
        return cost

    def check_valid(self):
        # check if all nodes are connected
        for node in self.nodes:
            if not node.visited:
                return False
        return True


def build_mst(student_output, V, max_range, graph):
    # the file has the following format
    # a int that represents the number of edges
    # for each edge, there are four ints: node_1_row node_1_col node_2_row node_2_col
    with open(student_output, 'r') as f:
        mst = MST(max_range)
        line_count = f.readline()

        for i in range(int(line_count)):
            line = f.readline()
            if line == '':
                break
            col1, row1, col2, row2 = map(int, line.split())
            node1 = mst.get_node(col1, row1)
            node2 = mst.get_node(col2, row2)
            if node1 is None:
                node1 = Node(col1, row1)
                mst.add_node(node1)
            if node2 is None:
                node2 = Node(col2, row2)
                mst.add_node(node2)
            node1.add_edge(node2, )
            node2.add_edge(node1)
            mst.add_edge(node1, node2)
            graph.add_edge((col1, row1), (col2, row2))
    return mst


def get_input_nodes(test_file):
    # the file contains a line with a int that represents the max_range, other int with the number of nodes and a final int with a target_cost
    # followed by the nodes in the format: row col
    graph = nx.Graph()
    with open(test_file, 'r') as f:
        line = f.readline()
        V = int(line)
        nodes = []
        for i in range(V):
            line = f.readline()
            col, row = map(int, line.split())
            nodes.append((col, row))
            graph.add_node((col, row))
    return 2000, V, 23763, nodes, graph


def check_contains_original_nodes(nodes, mst):
    for node in nodes:
        if not mst.get_node(node[0], node[1]):
            return False
    return True


def check_improvement(graph, jsonfile, testfile, cost):

    tests = ["easy_0", "easy_1", "easy_2",
            "medium_0", "medium_1", "medium_2",
            "hard_0", "hard_1", "hard_2"]

    for test in tests:
        if test in testfile:
            key = test
            break

    with open(jsonfile, "r") as file:
        comparador = json.load(file)

    if comparador[key]["costo"] != cost:
        return "Output is not a MST", 0

    grados = [tupla[1] for tupla in list(graph.degree)]
    suma = 0

    if max(grados) > 6:
        return "PARTIAL CORRECT", 0.7

    for i in range(1, 7):
        if i == 6:
            print(grados.count(i), i)
            suma += i * grados.count(i) * 7
        elif i == 5:
            print(grados.count(i), i)
            suma += i * grados.count(i) * 3
        elif i == 4:
            print(grados.count(i), i)
            suma += i * grados.count(i) * 2
        else:
            print(grados.count(i), i)
            suma += i * grados.count(i)

    if (suma/comparador[key]["obj"]) > 1.35:
        return "PARTIAL CORRECT", 0.7

    elif (suma/comparador[key]["obj"]) > 1:
        print(suma, comparador[key]["obj"])
        return "PARTIAL CORRECT", 0.9
    else:
        return "CORRECT", 1


def check_mst(test_file, student_output, jsonfile):
    try:
        max_range, V, target_cost, nodes, graph = get_input_nodes(test_file)
        mst = build_mst(student_output, V, max_range, graph)
        cost = mst.dfs_iterative(mst.nodes[0])
        is_valid = mst.check_valid()
        if not is_valid:
            return False, "Output is not a MST"
        contains_original_nodes = check_contains_original_nodes(nodes, mst)
        if not contains_original_nodes:
            return False, "Original Nodes Not Found"
        return True, check_improvement(graph, jsonfile, test_file, cost)

    except FileNotFoundError:
        return False, "WRONG PATH"
    except Exception:
        return False, "WRONG OUTPUT FORMAT"


if __name__ == '__main__':
    # PUEDES REESCRIBIR ESTA SECCION PARA AUTOMATIZAR TU REVISION

    test_file_path = input("Introduce el path del archivo de test: ")
    output_file_path = input("Introduce el path de tu archivo de output: ")
    jsonfile = input("Introduce el path del archivo de pauta: ")

    _ ,score = check_mst(test_file_path, output_file_path, jsonfile)
    print('Score: {}'.format(score))
