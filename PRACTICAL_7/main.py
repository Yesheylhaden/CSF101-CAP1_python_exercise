class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = self.Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = self.Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = self.Node(value)
            else:
                self._insert_recursive(node.right, value)
    
    # find max
    def find_max(self):
        if not self.root:
            return None # if tree is empty return none
        return self.find_max_recursive(self.root)

    def find_max_recursive(self, node):
        while node.right is not None:
            node = node.right 
        return node.value

    # count number of nodes
    def count_nodes(self):
        return self.count_nodes_recursive(self.root)

    def count_nodes_recursive(self, node):
        if node is None:
            return 0

        left_count = self.count_nodes_recursive(node.left) # count nodes in the left subtree
        right_count = self.count_nodes_recursive(node.right) # count nodes in the right

        return 1 + left_count + right_count # total count including top node

    # breadth-first search
    def breadth_first_search(self):
        if not self.root:
            return []
        
        queue = [self.root]
        result = []

        while queue:
            current = queue.pop(0) # remove first node
            result.append(current.value)

            if current.left: # enqueue left chld
                queue.append(current.left)
            if current.right: # enqueue right child
                queue.append(current.right)

        return result

    # find height of tree
    def find_height(self):
        return self.find_height_recursive(self.root)

    def find_height_recursive(self, node):
        if node is None:
            return 0
        
        left_height = self.find_height_recursive(node.left)
        right_height = self.find_height_recursive(node.right)

        return 1 + max(left_height, right_height)

    # check for validity 
    def valid_bst(self):
        return self.valid_bst_recursive(self.root, float("-inf"), float("inf"))

    def valid_bst_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.value < max_value):
            return False
        
        left_valid = self.valid_bst_recursive(node.left, min_value, node.value)
        right_value = self.valid_bst_recursive(node.right, node.value, max_value)

        return left_valid and right_value

bst = BinarySearchTree()
values =[10, 5, 15, 3, 7, 13, 20, 1, 4, 6, 8, 12, 14, 18, 25]
for i in values:
    bst.insert(i)

print("max value:", bst.find_max())
print("total number of nodes:", bst.count_nodes())
print("level-order traversal:", bst.breadth_first_search())
print("height of tree:", bst.find_height())
print("valid or not:", bst.valid_bst())  
