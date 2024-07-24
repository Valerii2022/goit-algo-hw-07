import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

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
root = Node(5)
root = insert(root, 13)
root = insert(root, 2)
root = insert(root, 12)
root = insert(root, 7)
root = insert(root, 6)
root = insert(root, 8)
root = insert(root, 1)
root = insert(root, 16)

# Пошук найбільшого значення
print(f"Найбільше значення: {find_maximum(root)}") 

# Пошук найменшого значення
print(f"Найменше значення: {find_minimum(root)}") 

# Пошук суми всіх значень
print(f"Сума всіх значень: {find_sum(root)}") 

