class Node:
    def __init__(self, data):
        
        self.data = data
        self.color = "red"  
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    def __init__(self):
        
        self.TNULL = Node(0)
        self.TNULL.color = "black"
        self.root = self.TNULL

    def left_rotate(self, x):
        
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, data):
        
        node = Node(data)
        node.left = node.right = self.TNULL

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            x = x.left if node.data < x.data else x.right

        node.parent = y
        if y is None:
            self.root = node
        elif node.data < y.data:
            y.left = node
        else:
            y.right = node

        if node.parent is None:
            node.color = "black"
            return
        if node.parent.parent is None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        
        while k.parent and k.parent.color == "red":
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == "red":
                    u.color = "black"
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = "black"
                    k.parent.parent.color = "red"
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = "black"

    def search_tree(self, node, key):
        
        if node == self.TNULL or key == node.data:
            return node
        
        if key < node.data:
            return self.search_tree(node.left, key)
        return self.search_tree(node.right, key)

    def search(self, key):
        
        return self.search_tree(self.root, key)