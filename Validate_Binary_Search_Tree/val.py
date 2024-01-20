class BinaryTree:
    def __init__(self, val, leftnode=None, rightnode=None):
        self.val = val
        self.leftnode = leftnode
        self.rightnode = rightnode


class BinarySearchTree:
    def validate_BST(self, root: BinaryTree) -> bool:
        return self.valid(root, float("inf"), float("-inf"))

    def valid(self, root, max_val, min_val):
        if root is None:
            return True

        if not (min_val < root.val < max_val):
            return False

        return self.valid(root.leftnode, root.val, min_val) and self.valid(
            root.rightnode, max_val, root.val
        )


# Example usage:
# Construct a binary search tree
tree = BinaryTree(2, BinaryTree(1), BinaryTree(3))

# Validate the binary search tree
bst_validator = BinarySearchTree()
result = bst_validator.validate_BST(tree)
print(result)  # Output: True
