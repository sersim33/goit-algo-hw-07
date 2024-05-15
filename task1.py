class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\\t" * level + prefix + str(self.val) + "\\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None or root.val == key:
        return root
    if key < root.val:
        return search(root.left, key)
    return search(root.right, key)


def find_max_value(root):
    if root is None:
        return None
    
    current = root
    while current.right:
        current = current.right
    
    return current.val

root = Node(11)  
root = insert(root,22)  
root = insert(root,5)
root = insert(root,55)
root = insert(root,3)
root = insert(root,12)
max_value = find_max_value(root)


print(root)
print("max value is:", max_value)