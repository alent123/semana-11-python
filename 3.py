# Clase Node: Representa un nodo en un árbol binario
class Node:
    def __init__(self, val):
        # Valor almacenado en el nodo
        self.val = val
        # Referencia al hijo izquierdo (subárbol con valores menores)
        self.left = None
        # Referencia al hijo derecho (subárbol con valores mayores)
        self.right = None

# Función para construir un BST desde una lista de valores
def build_bst(vals):
    # Función auxiliar para insertar un valor en el árbol respetando la propiedad BST
    def insert(root, val):
        # Caso base: Si el nodo es None, crea un nuevo nodo con el valor dado
        if not root:
            return Node(val)
        # Si el valor es menor que el valor actual, se inserta en el subárbol izquierdo
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            # Si el valor es mayor o igual, se inserta en el subárbol derecho
            root.right = insert(root.right, val)
        # Retorna el nodo raíz actualizado
        return root

    root = None
    # Insertar cada valor de la lista en el BST
    for v in vals:
        root = insert(root, v)
    return root

# Función para construir un árbol inválido que viola la propiedad BST (izquierda mayor que nodo)
def build_invalid_tree1():
    root = Node(5)
    root.left = Node(6)  # Aquí la propiedad BST se rompe, ya que 6 > 5
    root.right = Node(7)
    return root

# Función para construir otro árbol inválido que viola la propiedad BST (derecha menor que nodo)
def build_invalid_tree2():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(4)  # Aquí la propiedad BST se rompe, ya que 4 < 5
    return root

# Función para validar si un árbol binario es un BST
def is_valid_bst(node, min_val=float('-inf'), max_val=float('inf')):
    """
    Verifica recursivamente que cada nodo respete los límites de min y max.
    La propiedad BST exige:
    - Todos los valores en el subárbol izquierdo < nodo actual
    - Todos los valores en el subárbol derecho > nodo actual
    """
    # Caso base: árbol vacío es válido
    if not node:
        return True

    # Verifica si el valor actual está fuera del rango válido
    if not (min_val < node.val < max_val):
        # Si el valor no cumple la restricción, retorna False
        return False

    # Recursivamente valida:
    # - Subárbol izquierdo con límite superior actualizado al valor actual
    # - Subárbol derecho con límite inferior actualizado al valor actual
    return (is_valid_bst(node.left, min_val, node.val) and
            is_valid_bst(node.right, node.val, max_val))

# Pruebas para verificar la función is_valid_bst

# Caso 1: Árbol válido (debe retornar True)
print(is_valid_bst(build_bst([5,3,7,2,4,6,8])) == True)

# Caso 2: Árbol inválido por violación en hijo izquierdo (debe retornar False)
print(is_valid_bst(build_invalid_tree1()) == False)

# Caso 3: Árbol inválido por violación en hijo derecho (debe retornar False)
print(is_valid_bst(build_invalid_tree2()) == False)

# Caso 4: Árbol con un solo nodo (válido)
print(is_valid_bst(build_bst([42])) == True)

# Caso 5: Árbol vacío (válido por definición)
print(is_valid_bst(None) == True)

