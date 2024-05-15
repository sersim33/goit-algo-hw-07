class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_max_value(root):
    if root is None:
        return None
    
    current_max = root.val
    left_max = find_max_value(root.left)
    right_max = find_max_value(root.right)
    
    if left_max is not None and left_max > current_max:
        current_max = left_max
    if right_max is not None and right_max > current_max:
        current_max = right_max
    
    return current_max

# Приклад створення дерева
root = Node(11)  
root.left = Node(22)  
root.right = Node(5)
root.left.left = Node(55)
root.left.right = Node(3)
root.right.left = Node(12)

max_value = find_max_value(root)
print("Найбільше значення в дереві:", max_value)
