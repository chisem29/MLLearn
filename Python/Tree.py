from collections import deque
class Node :
    def __init__(self, val : int, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

tree = Node(1, Node(2, Node(4), Node(5)), Node(3, Node(6), Node(7)))

l = [4, 7, 2, 9, 6, 3, 1]


def dfs(tree : Node) :
    stack = []
    stack.append(tree)
    while len(stack) > 0 :
        node = stack.pop()
        if node :
            print(node.val)
            stack.append(node.right)
            stack.append(node.left)
    '''
        Позуй
        if not tree :
            return
        print(tree.val)
        dfs(tree.right)
        dfs(tree.left)
    '''

def bfs(tree : Node) :
    q = deque()
    q += [tree]
    while q :
        for _ in range(len(q)) :
            node = q.popleft()
            if node :
                print(node.val)
                q += [node.left]
                q += [node.right]

