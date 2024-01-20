# Validate a Binary Search Tree

```“You are given the root of a binary tree, you need to write an algorithm to determine if it is a valid binary search tree or not.”```

Validating a binary search tree means writing an algorithm to check whether a binary tree is a binary search tree or not.

-----

# Code Break:

```python
class BinaryTree:
    def __init__(self, val, leftnode=None, rightnode=None):
        self.val = val
        self.leftnode = leftnode
        self.rightnode = rightnode
```

Here, a class `BinaryTree` is defined to represent a node in a binary tree. Each node has a value (`val`), a left child node (`leftnode`), and a right child node (`rightnode`). The `__init__` method is a constructor that initializes the attributes of the class.

```python
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
```

Here, a class `BinarySearchTree` is defined, which contains a method `validate_BST` for checking whether a given binary tree is a valid Binary Search Tree (BST). The method takes the root of the binary tree (`root`) as an argument and returns a boolean indicating whether it is a valid BST. The `valid` method is a helper method that performs the actual validation recursively.

```python
# Example usage:
# Construct a binary search tree
tree = BinaryTree(2, BinaryTree(1), BinaryTree(3))
```

An example of constructing a binary search tree is provided. The root has a value of `2`, a left child with a value of `1`, and a right child with a value of `3`.

```python
# Validate the binary search tree
bst_validator = BinarySearchTree()
result = bst_validator.validate_BST(tree)
print(result)  # Output: True
```

An instance of `BinarySearchTree` is created (`bst_validator`). The `validate_BST` method is then called with the constructed tree as an argument, and the result is printed. In this case, the output is `True`, indicating that the provided binary tree is a valid Binary Search Tree.

-----