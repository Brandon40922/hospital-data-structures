
class DoctorNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class DoctorTree:
    def __init__(self):
        self.root = None

    def find_node(self, node, name):
        if node is None:
            return None

        if node.name == name:
            return node

        left_result = self.find_node(node.left, name)
        if left_result is not None:
            return left_result

        return self.find_node(node.right, name)

    def insert(self, parent_name, doctor_name, side):
        if side not in ("left", "right"):
            print("Error: Side must be 'left' or 'right'.")
            return

        parent = self.find_node(self.root, parent_name)

        if parent is None:
            print(f"Error: Parent doctor '{parent_name}' not found.")
            return

        if getattr(parent, side) is not None:
            print(f"Error: {parent_name} already has a {side} report.")
            return

        if self.find_node(self.root, doctor_name) is not None:
            print(f"Error: Doctor '{doctor_name}' already exists.")
            return

        new_node = DoctorNode(doctor_name)
        setattr(parent, side, new_node)

    def preorder(self, node):
        if node is None:
            return []

        return (
            [node.name]
            + self.preorder(node.left)
            + self.preorder(node.right)
        )

    def inorder(self, node):
        if node is None:
            return []

        return (
            self.inorder(node.left)
            + [node.name]
            + self.inorder(node.right)
        )

    def postorder(self, node):
        if node is None:
            return []

        return (
            self.postorder(node.left)
            + self.postorder(node.right)
            + [node.name]
        )


def main():
    tree = DoctorTree()
    tree.root = DoctorNode("Dr. Croft")

    tree.insert("Dr. Croft", "Dr. Goldsmith", "right")
    tree.insert("Dr. Croft", "Dr. Phan", "left")
    tree.insert("Dr. Phan", "Dr. Carson", "right")
    tree.insert("Dr. Phan", "Dr. Morgan", "left")

    print("--- Doctor Reporting Tree ---")

    print("Preorder:")
    print(tree.preorder(tree.root))

    print("\nInorder:")
    print(tree.inorder(tree.root))

    print("\nPostorder:")
    print(tree.postorder(tree.root))

    print("\n--- Edge Case Tests ---")

    tree.insert("Dr. Unknown", "Dr. Smith", "left")
    tree.insert("Dr. Croft", "Dr. James", "middle")
    tree.insert("Dr. Croft", "Dr. Lee", "left")
    tree.insert("Dr. Croft", "Dr. Phan", "right")

    empty_tree = DoctorTree()
    print("Empty tree preorder:", empty_tree.preorder(empty_tree.root))

    assert tree.preorder(tree.root) == [
        "Dr. Croft", "Dr. Phan", "Dr. Morgan",
        "Dr. Carson", "Dr. Goldsmith"
    ]

    assert tree.inorder(tree.root) == [
        "Dr. Morgan", "Dr. Phan", "Dr. Carson",
        "Dr. Croft", "Dr. Goldsmith"
    ]

    assert tree.postorder(tree.root) == [
        "Dr. Morgan", "Dr. Carson", "Dr. Phan",
        "Dr. Goldsmith", "Dr. Croft"
    ]

    print("\nAll doctor tree tests passed!")


if __name__ == "__main__":
    main()
