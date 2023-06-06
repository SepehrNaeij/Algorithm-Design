class Node:
    def __init__(self):
        self.data = 0
        self.child = []

def newNode(key):
    temp = Node()
    temp.data = key
    return temp

def nextLargerElementUtil(root, x):
    global res
    if root is None:
        return
    
    if root.data > x:
        if res is None or res.data > root.data:
            res = root
    
    numChildren = len(root.child)
    for i in range(numChildren):
        nextLargerElementUtil(root.child[i], x)

def nextLargerElement(root, x):
    global res
    res = None
    nextLargerElementUtil(root, x)
    return res

#Test the code with its desired test case! 
root = newNode(20)
root.child.append(newNode(9))
root.child.append(newNode(25))
root.child[0].child.append(newNode(5))
root.child[0].child.append(newNode(12))
root.child[1].child.append(newNode(11))
root.child[1].child.append(newNode(14))

x = 9
y = 14
print("The first larger element than", x, "is", nextLargerElement(root, x).data)
print("The first larger element than", y, "is", nextLargerElement(root, y).data)
