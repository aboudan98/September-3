class Node:
    def __init__(self, d):
        self.data = d
        self.l = None
        self.r = None


def arrayToBST(array):
    if not array:
        return None

    mid = (len(array)) // 2

    root = Node(array[mid])

    root.l = arrayToBST(array[:mid])

    root.r = arrayToBST(array[mid + 1:])
    return root
def preOrder(node):
    if not node:
        return
    print(node.data, " ", end="")
    preOrder(node.l)
    preOrder(node.r)


arr = [35, 40, 45, 50, 55, 60, 65]
root = arrayToBST(arr)
print("PreOrder Traversal of constructed BST \n", end="")
preOrder(root)