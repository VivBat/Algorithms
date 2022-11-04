import numpy as np


class Node:
    def __init__(self, color, label, parent=None, left_child=None, right_child=None):
        self.color = color
        self.label = label
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child
        self.subtree_color_count = np.array([[0] for i in range(C)])
        self.full = []

    def is_full(self):
        for j in range(len(self.subtree_color_count)):
            if self.subtree_color_count[j][0] == D:
                self.full.append(j)


class BinaryTree:
    def __init__(self, root):
        self.root = root

    def build_tree(self, node_a,
                   node_b):  # node_a = label of parent, node_b = label of child, i.e node_a is the parent of node_b
        nodes[node_b].parent = nodes[node_a]

        if nodes[node_a].left_child is None:
            nodes[node_a].left_child = nodes[node_b]
        else:
            nodes[node_a].right_child = nodes[node_b]

    def count_colors(self, node):
        if node.left_child is None and node.right_child is None:  # if the node is a leaf
            node.subtree_color_count[node.color][0] += 1  # increment the count of color of the node
            return

        if node is not None:
            node.subtree_color_count[node.color][0] += 1  # increment the count of the color of the node

        if node.left_child is not None:
            self.count_colors(node.left_child)
            node.subtree_color_count += node.left_child.subtree_color_count
        if node.right_child is not None:
            self.count_colors(node.right_child)
            node.subtree_color_count += node.right_child.subtree_color_count

    def find_all_paths(self, node):
        """
        Finds all the paths from the root to the leaves in the tree
        :param node: a node of the tree
        :return: Updates the global list containing all the paths
        """
        global full_paths
        if node.left_child is None and node.right_child is None:
            paths.append(node)  # append the leaf to the path
            all_paths.append(
                paths.copy())  # finally append the entire path to the array containing all the paths in the tree
            paths.pop()
            return

        paths.append(node)  # append the node to the current path (collecting nodes)

        if node.left_child:
            self.find_all_paths(node.left_child)
        if node.right_child:
            self.find_all_paths(node.right_child)

        paths.pop()


def find_full_paths(path):
    """
    Finds all the "full-paths"
    :param path: a path from the root to a leaf
    :return: Updates the global list containing "full-paths"
    """
    local_full_path = []
    for node in path:
        for colors in node.full:
            if colors not in local_full_path:
                local_full_path += [colors]

    if len(local_full_path) == C:
        full_paths.append(local_full_path)


def make_all_nodes(colors_list):
    """
    Makes all the nodes of the tree
    :param colors_list: List containing the color of each node in the tree
    :return: Prepares the nodes of the tree
    """
    for i in range(len(colors_list)):
        nodes.append(Node(color=colors_list[i], label=i))


def solution():
    make_all_nodes(colors_of_all_nodes)  # make all the nodes of the tree

    tree = BinaryTree(nodes[0])  # nodes[0] -> root of the tree
    for i in range(N - 1):
        a, b = input().split()
        a = int(a)
        b = int(b)
        tree.build_tree(a, b)  # Build the tree using all the prepared nodes

    tree.count_colors(nodes[0])

    for node in nodes:
        node.is_full()

    tree.find_all_paths(nodes[0])  # finding all the paths in the tree from the root to the leaves

    for path in all_paths:  # finding which paths are "full-path" from all the paths
        find_full_paths(path)

    print(len(full_paths))  # printing only the count of the full-paths


if __name__ == "__main__":
    N, C, D = input().split()

    N = int(N)
    C = int(C)
    D = int(D)

    colors_of_all_nodes = (input().split())
    colors_of_all_nodes = list(map(int, colors_of_all_nodes))

    nodes = []  # to contain all the nodes
    all_paths = []  # to contain all the routes in the tree
    paths = []  # to temporarily hold a local path in the tree
    full_paths = []  # to contain all the "full-paths" in the tree

    solution()
