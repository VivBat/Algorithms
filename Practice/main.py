class Node:
    def __init__(self, key, coin_used=None, child_node1=None, child_node2=None, child_node3=None):
        self.key = key
        self.coin_used = coin_used
        self.child_node1 = child_node1
        self.child_node2 = child_node2
        self.child_node3 = child_node3


class Tree:
    def __init__(self, root, coin_used=None):
        self.root = Node(root, coin_used)

    def build_tree(self, node):
        global coins, coins_used
        if node is not None:
            if node.key <= 0:
                return
        else:
            return

        if node.coin_used is not None:
            if coins[0] <= node.coin_used and node.key - coins[0] >= 0:
                node.child_node1 = Node(key=node.key - coins[0], coin_used=coins[0])
            if coins[1] <= node.coin_used and node.key - coins[1] >= 0:
                node.child_node2 = Node(key=node.key - coins[1], coin_used=coins[1])
            if coins[2] <= node.coin_used and node.key - coins[2] >= 0:
                node.child_node3 = Node(key=node.key - coins[2], coin_used=coins[2])

        else:
            node.child_node1 = Node(key=node.key - coins[0], coin_used=coins[0])
            node.child_node2 = Node(key=node.key - coins[1], coin_used=coins[1])
            node.child_node3 = Node(key=node.key - coins[2], coin_used=coins[2])

        self.build_tree(node.child_node1)
        self.build_tree(node.child_node2)
        self.build_tree(node.child_node3)

        return node

    def find_coins(self, node):
        global local_coins

        if node is not None:
            if node.key == 0:
                local_coins.append(node.coin_used)
                coins_used.append(list(local_coins))
                local_coins.pop()
                return
        else:
            return

        if node.coin_used is not None:
            local_coins.append(node.coin_used)

        if node.child_node1 is not None:
            self.find_coins(node.child_node1)

        if node.child_node2 is not None:
            self.find_coins(node.child_node2)

        if node.child_node3 is not None:
            self.find_coins(node.child_node3)

        if len(local_coins) > 0:
            local_coins.pop()


if __name__ == "__main__":
    coins = [5, 2, 1]
    local_coins = []
    coins_used = []
    child_count_on_node = len(coins)
    monetary_val = 7
    tree = Tree(monetary_val)
    tree.build_tree(tree.root)
    tree.find_coins(tree.root)

    print(coins_used)
