class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
   
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def sum_values(root):
    if root is None:
        return 0
    
    return root.val + sum_values(root.left) + sum_values(root.right)

root = Node(11)  
insert(root, 22)  
insert(root, 5)
insert(root, 55)
insert(root, 3)
insert(root, 12)
insert(root, 2)

total_sum = sum_values(root)

print("Total sum of all values in the binary tree:", total_sum)