class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.value) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.value:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_maximum(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.value

def find_minimum(root):
    if root is None:
        return None
    current = root
    while current.left is not None:
        current = current.left
    return current.value

def find_sum(root):
    if root is None:
        return 0
    return root.value + find_sum(root.left) + find_sum(root.right)

# Тест
root = Node(12)
root = insert(root, 4)
root = insert(root, 15)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 28)
root = insert(root, 16)
root = insert(root, 11)
root = insert(root, 9)
root = insert(root, 19)
root = insert(root, 5)

# Візуалізація двійкового дерева пошуку
print(root)

# Пошук найбільшого значення
print(f"Найбільше значення: {find_maximum(root)}") 

# Пошук найменшого значення
print(f"Найменше значення: {find_minimum(root)}") 

# Пошук суми всіх значень
print(f"Сума всіх значень: {find_sum(root)}") 

