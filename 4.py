# Clase Node: representa un nodo individual en un árbol binario
class Node:
    def __init__(self, val):
        # Valor almacenado en el nodo
        self.val = val
        # Referencia al hijo izquierdo (menores que el nodo)
        self.left = None
        # Referencia al hijo derecho (mayores que el nodo)
        self.right = None


# Función para construir un BST a partir de una lista de valores
def build_bst(vals):
    """
    Recibe una lista de valores y construye un árbol binario de búsqueda (BST)
    insertando uno a uno los valores en el árbol.

    El BST tiene la propiedad: para cada nodo,
    - todos los valores en el subárbol izquierdo son menores que el nodo,
    - todos los valores en el subárbol derecho son mayores o iguales.
    """

    # Función auxiliar para insertar un valor en el árbol
    def insert(root, val):
        # Caso base: si el nodo actual es None, crea uno nuevo con el valor dado
        if root is None:
            return Node(val)

        # Si el valor es menor que el nodo actual, insertar en el subárbol izquierdo
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            # Si el valor es mayor o igual, insertar en el subárbol derecho
            root.right = insert(root.right, val)

        # Retorna la raíz del subárbol modificado
        return root

    root = None  # Empezamos con un árbol vacío

    # Insertamos cada valor de la lista en el árbol
    for v in vals:
        root = insert(root, v)

    # Finalmente, retornamos la raíz del árbol completo construido
    return root


# Función para encontrar el k-ésimo elemento más pequeño en el BST
def kth_smallest(root, k):
    """
    Se basa en la propiedad del recorrido inorden (left, node, right)
    que visita los nodos en orden ascendente.

    Se realiza un recorrido inorden y se guarda cada valor en una lista.
    El k-ésimo elemento en esta lista será el resultado.
    """

    # Lista donde guardaremos los valores en orden ascendente
    inorder_vals = []

    # Función recursiva para recorrer el árbol en orden inorden
    def inorder(node):
        if node is None:  # Caso base: si el nodo es None, termina la llamada
            return

        inorder(node.left)          # Primero recorrer el subárbol izquierdo (valores menores)
        inorder_vals.append(node.val)  # Luego visitar el nodo actual y guardar su valor
        inorder(node.right)         # Finalmente recorrer el subárbol derecho (valores mayores)

    # Ejecutamos el recorrido inorden a partir de la raíz
    inorder(root)

    # Retornamos el valor que está en la posición k-1 (porque lista es 0-indexada)
    return inorder_vals[k - 1]


# --- Pruebas unitarias para validar el correcto funcionamiento ---

# Caso 1: k=3 en árbol balanceado [5,3,7,2,4,6,8]
print(kth_smallest(build_bst([5, 3, 7, 2, 4, 6, 8]), 3) == 4)  # True

# Caso 2: k=1 (el mínimo)
print(kth_smallest(build_bst([1, 2, 3, 4, 5]), 1) == 1)  # True

# Caso 3: k=5 (el máximo)
print(kth_smallest(build_bst([5, 4, 3, 2, 1]), 5) == 5)  # True

# Caso 4: Un solo nodo, k=1
print(kth_smallest(build_bst([42]), 1) == 42)  # True

# Caso 5: k=6 en árbol [10,5,15,3,7,12,18]
print(kth_smallest(build_bst([10, 5, 15, 3, 7, 12, 18]), 6) == 15)  # True

