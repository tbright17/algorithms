class Node:

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorder(root):
    res = []
    if not root:
        return res
    stack1 = [root]
    stack2 = []
    while stack1:
        cur = stack1.pop()
        stack2.append(cur)
        if cur.left:
            stack1.append(cur.left)
        if cur.right:
            stack1.append(cur.right)

    while stack2:
        res.append(stack2.pop().val)
    return res

if __name__ == '__main__':
    n1 = Node(100)
    n2 = Node(50)
    n3 = Node(150)
    n4 = Node(25)
    n5 = Node(75)
    n6 = Node(125)
    n7 = Node(175)
    n1.left, n1.right = n2, n3
    n2.left, n2.right = n4, n5
    n3.left, n3.right = n6, n7
    print(postorder(n1))
