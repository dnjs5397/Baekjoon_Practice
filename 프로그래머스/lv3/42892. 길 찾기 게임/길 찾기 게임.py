import sys
sys.setrecursionlimit(10**5)

def solution(nodeinfo):
    class Node(object):
        def __init__(self, info):
            self.num = info[2]
            self.x = info[0]
            self.y = info[1]
            self.left = None
            self.right = None


    def add_node(parent, info):
        if parent.x > info[0]:
            if parent.left:
                add_node(parent.left, info)
            else:
                parent.left = Node(info)
        else:
            if parent.right:
                add_node(parent.right, info)
            else:
                parent.right = Node(info)


    def preorder(t):
        v = [t.num]
        if t.left:
            v += preorder(t.left)
        if t.right:
            v += preorder(t.right)
        return v


    def postorder(t):
        v = []
        if t.left:
            v += postorder(t.left)
        if t.right:
            v += postorder(t.right)
        v.append(t.num)
        return v


    for i in range(len(nodeinfo)):
        nodeinfo[i].append(i+1)
    nodeinfo.sort(key=lambda x: x[0])
    nodeinfo.sort(key=lambda x: x[1], reverse=True)

    tree = Node(nodeinfo[0])

    for nod in nodeinfo[1:]:
        add_node(tree, nod)

    return ([preorder(tree), postorder(tree)])
