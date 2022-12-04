import time


class Node:
    def __init__(self, key, color):
        self.key = key
        self.color = color
        self.neighbours = []


class Graph:
    def __init__(self, NEC, colors, edges):
        self.num_nodes = NEC[0]
        self.num_edges = NEC[1]
        self.num_colors = NEC[2]
        self.colors = colors
        self.edges = edges

        self.nodes = []
        for node_id in range(self.num_nodes):
            node = Node(node_id, self.colors[node_id])
            self.nodes.append(node)

    def add_edges(self):
        for vertices in self.edges:
            node1 = self.nodes[vertices[0]]
            node2 = self.nodes[vertices[1]]
            node1.neighbours.append(node2)
            node2.neighbours.append(node1)

    def find_isolated_edges(self):
        isolated_edges = []

        # iterating over each edge
        for edge in self.edges:
            node1 = self.nodes[edge[0]]  # first vertex of the edge
            node2 = self.nodes[edge[1]]  # second vertex of the edge
            e_type = {node1.color, node2.color}

            flag = False
            # exploring the first level (incident) edges of node1
            for next_node1_1 in node1.neighbours:
                if flag is True:
                    break

                if next_node1_1 is not node2:
                    e_type1_1 = {node1.color, next_node1_1.color}
                    if e_type1_1 == e_type:
                        flag = True
                        break
                    elif e_type1_1 != e_type:
                        # exploring the 2nd level (adjacent) edges of node1
                        for next_node1_2 in next_node1_1.neighbours:
                            # if next_node1_2 is not next_node1_1:
                            if next_node1_2 is not node1:
                                e_type1_2 = {next_node1_2.color, next_node1_1.color}
                                if e_type1_2 != e_type:
                                    continue
                                else:
                                    flag = True
                                    break

            # exploring the first level (incident) edges of node2
            for next_node2_1 in node2.neighbours:
                if flag is True:
                    break
                if next_node2_1 is not node1:
                    e_type2_1 = {node2.color, next_node2_1.color}
                    if e_type2_1 == e_type:
                        flag = True
                        break
                    elif e_type2_1 != e_type:
                        # exploring the 2nd level (adjacent) edges of node2
                        for next_node2_2 in next_node2_1.neighbours:
                            # if next_node2_2 is not next_node2_1:
                            if next_node2_2 is not node2:
                                e_type2_2 = {next_node2_2.color, next_node2_1.color}
                                if e_type2_2 != e_type:
                                    continue
                                else:
                                    flag = True
                                    break

            if flag is False:
                isolated_edges.append({node1.key, node2.key})

        return len(isolated_edges)


def solution(NEC, colors, edges):
    t1_building_graphs = time.time()
    graph = Graph(NEC, colors, edges)
    graph.add_edges()
    t2_building_graphs = time.time()

    t1_finding_isolated_edges = time.time()
    num_isolated_edges = graph.find_isolated_edges()
    t2_finding_isolated_edges = time.time()

    # print(f"Time to build the graph: {t2_building_graphs - t1_building_graphs}")
    # print(f"Time to find isolated edges: {t2_finding_isolated_edges - t1_finding_isolated_edges}")

    return num_isolated_edges


if __name__ == "__main__":

    NEC_ = input().split()  # Number of Nodes, Edges, Colors respectively
    NEC_ = list(map(int, NEC_))

    colors_of_nodes = input().split()
    colors_of_nodes = list(map(int, colors_of_nodes))

    edges_ = []
    for i in range(NEC_[1]):
        edge = input().split()
        edge = list(map(int, edge))
        edges_.append(edge)

    result = solution(NEC_, colors_of_nodes, edges_)

    print(result)


