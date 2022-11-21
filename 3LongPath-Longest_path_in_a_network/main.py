class Node:
    def __init__(self, key=None, parent=None):
        self.key = key
        self.parent = parent
        self.children = []
        self.cost = 0
        self.sums = []


class Tree:
    def __init__(self, in_str):
        self.in_str = in_str

    def build_tree(self, node):
        """
        Build a tree from the given string of the specific format: (4(3(2(3)(5)(1)(6))))
        :param node: starts with the root node
        """
        length = len(self.in_str)
        i = 2  # start with i=2 since root is already accounted for
        while i < length:
            if self.in_str[i] == "(":    # if the char is "(", the following number is a child
                num = ''
                while self.in_str[i+1] != "(" and self.in_str[i+1] != ")":   # to extract the number from the string
                    num += self.in_str[i+1]
                    i += 1
                child = Node(int(num))     # a child node created with the number as the key
                node.children.append(child)  # the child node is appended to the list of children of the current node
                child.parent = node       # current node is set as the parent of the child
                node = child             # the child is set as the current node

            if self.in_str[i] == ")":  # if the char is "(", climb out to the parent
                node = node.parent      # current node's parent set as the current node
                i += 1

            else:
                i += 1

    def collect_sums(self, node):
        """
        Sums up the costs of paths with the highest values in a subtree from leaf to leaf
        :param node: a node of the tree
        :return: Appends to the global variable sums[]
        """
        if not node.children:
            node.cost += node.key
            return

        for idx in range(len(node.children)):
            child = node.children[idx]

            self.collect_sums(child)   # recursively calling the function

            if node.parent is None:    # when the node is root
                if len(node.children) == 1:  # and has only one child, then it is also and end point for the network
                    node.cost = node.key + child.cost
                    sums.append(node.cost)

            if len(node.children) == 1:
                node.cost = node.key + child.cost

            else:
                node.sums.append(child.cost)
                if idx == len(node.children)-1:
                    node.sums.sort(reverse=True)
                    sums.append(node.key + sum(node.sums[0:2]))  # only using the 2 biggest values to append only the biggest cost path
                node.cost = node.key + max(node.sums)


def solution(in_str):
    root = Node(int(in_str[1]))  # extracting the root of the tree
    tree = Tree(in_str)
    tree.build_tree(root)    # building the tree
    tree.collect_sums(root)


if __name__ == "__main__":
    # input_string = "(5(14(1(19)(2(10(8)))(3(5)(12(4)))(20))(4(17)(15)))(10(21(44)(13(35)(5(34)(4))(2(23)))(55(8)))(12(9)(10(6)(5(11))(4)))))"

    input_string = input()

    sums = []  # global variable to store sums of all the paths with maximum possible costs

    solution(input_string)

    print(max(sums))
