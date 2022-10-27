import queue
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

    def build_tree(self, node_a, node_b): # node_a = label of parent, node_b = label of child, i.e node_a is the parent of node_b
        nodes[node_b].parent = nodes[node_a]

        if nodes[node_a].left_child is None:
            nodes[node_a].left_child = nodes[node_b]
        else:
            nodes[node_a].right_child = nodes[node_b]

    def count_colors(self, node):
        if node.left_child is None and node.right_child is None:
            return

        if node.left_child is not None:
            node.subtree_color_count[node.left_child.color][0] += 1

        if node.right_child is not None:
            node.subtree_color_count[node.right_child.color][0] += 1


        if node.left_child is not None:
            self.count_colors(node.left_child)
            node.subtree_color_count += node.left_child.subtree_color_count
        if node.right_child is not None:
            self.count_colors(node.right_child)
            node.subtree_color_count += node.right_child.subtree_color_count



# # ........................................................................
#     #   S E R V I C E   M E T H O D S    (mainly printing)
#     def countNodes(self, node):
#         if node == None: return 0
#         return 1 + self.countNodes(node.left) + self.countNodes(node.right)
#
#     # calculates x coord = node order of in Inorder traversal
#     def setXcoord(self, node, x_coord):
#         if node == None: return x_coord
#         node.xcoord = self.setXcoord(node.left, x_coord) + 1
#         # print(node.key, node.setXcoord)
#         return self.setXcoord(node.right, node.xcoord)
#
#     def display(self):
#         self.setXcoord(self.root, 0)
#         qu = queue.Queue()
#         prevDepth = -1
#         prevEndX = -1
#         # in the queue store pairs(node, its depth)
#         qu.put((self.root, 0))
#         while not qu.empty():
#             node, nodeDepth = qu.get()
#
#             LbranchSize = RbranchSize = 0
#             if node.left != None:
#                 LbranchSize = (node.xcoord - node.left.xcoord)
#                 qu.put((node.left, nodeDepth + 1))
#             if node.right != None:
#                 RbranchSize = (node.right.xcoord - node.xcoord)
#                 qu.put((node.right, nodeDepth + 1))
#
#             LspacesSize = (node.xcoord - LbranchSize) - 1  # if first on a line
#             if prevDepth == nodeDepth:  # not first on line
#                 LspacesSize -= prevEndX
#
#             # print the node, branches, leading spaces
#             if prevDepth < nodeDepth and prevDepth > -1: print()  # next depth occupies new line
#             nodelen = 3
#             print(" " * nodelen * LspacesSize, end='')
#             print("_" * nodelen * LbranchSize, end='')
#             # print( "." + ("%2d"%node.key) + node.tag+".", end = '' )
#             print(node.tag + ("%2d" % node.key), end='')
#             print("_" * nodelen * RbranchSize, end='')
#
#             # used in the next run of the loop:
#             prevEndX = node.xcoord + RbranchSize
#             prevDepth = nodeDepth
#         # end of queue processing
#
#         N = self.countNodes(self.root)
#         print("\n" + '-' * N * nodelen)  # finish the last line of the tree
#----------------------------------------------------------------------------------------------

def make_all_nodes(colors_list):

    for i in range(len(colors_list)):
        nodes.append(Node(color=colors_list[i], label=i))


if __name__ == "__main__":
    # N,C,D = input().split()
    #
    # N = int(N)
    # C = int(C)
    # D = int(D)
    #
    # colors_of_all_nodes = (input().split())
    # colors_of_all_nodes = list(map(int, colors_of_all_nodes))

    nodes = []  # to contain all the nodes

    # test example 1
    N, C, D = 25, 3, 4
    colors_of_all_nodes = [0, 2, 0, 0, 0, 1, 1, 2, 0, 0, 2, 0, 1, 2, 2, 1, 2, 2, 2, 2, 0, 2, 2, 0, 0]


    # test example 2
    # N, C, D = 6, 5, 1
    # colors_of_all_nodes = [0, 1, 2, 3, 4, 4]

    make_all_nodes(colors_of_all_nodes)

    tree = BinaryTree(nodes[0])
    for i in range(N-1):
        a, b = input().split()
        a = int(a)
        b = int(b)
        tree.build_tree(a, b)

    # tree.display()

    tree.count_colors(nodes[0])

    for node in nodes:
        node.is_full()

    print("done!")
    print("done!")

