
class Node :
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

tree = Node(3, Node(9), Node(20, Node(15), Node(17)))
