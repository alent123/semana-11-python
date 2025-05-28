class NodoArbol: # Clase que representa un nodo del árbol
    def __init__(self, valor):
        self.valor = valor  # valor almacenado 
        self.izquierda = None # hijo izquierdo 
        self.derecha = None # Hijo derecho

def build_bst(valores): # Función que construye un Árbol Binario de Búsqueda 
    """Construye un Árbol Binario de Búsqueda (BST) a partir de una lista de valores"""
    raiz = None # inicialmente no hay raiz 
    for valor in valores: # Se inserta cada valor uno por uno
        raiz = insertar_nodo(raiz, valor)
    return raiz # se devuelve la raiz del arbol construido 

def insertar_nodo(raiz, valor):
    """Inserta un valor en el BST"""
    if raiz is None:# Si el nodo actual está vacío, se crea uno nuevo
        return NodoArbol(valor)
    if valor < raiz.valor: # Si el valor es menor, va a la izquierda
        raiz.izquierda = insertar_nodo(raiz.izquierda, valor)
    else: # Si es mayor o igual, va a la derecha
        raiz.derecha = insertar_nodo(raiz.derecha, valor)
    return raiz # Se devuelve la raíz actualizada

def consulta_rango(raiz, minimo, maximo):
    """Devuelve todos los valores dentro del rango [mínimo, máximo] en un BST"""
    resultado = [] # Lista para almacenar los valores encontrados

    def recorrido_inorden(nodo):
        if nodo is None:# Caso base: nodo nulo
            return
        # Visitar subárbol izquierdo solo si hay posibilidad de encontrar valores dentro del rango
        if nodo.valor > minimo:# Solo recorremos izquierda si hay posibilidad de encontrar valores válidos
            recorrido_inorden(nodo.izquierda)
        if minimo <= nodo.valor <= maximo: # Si el valor está dentro del rango, lo agregamos
            resultado.append(nodo.valor)
        if nodo.valor < maximo:# Solo recorremos derecha si hay posibilidad de encontrar valores válidos
            recorrido_inorden(nodo.derecha)

    recorrido_inorden(raiz)  # Iniciamos el recorrido desde la raíz
    return resultado   # Retornamos la lista de resultados
def range_query(root, min_val, max_val):
    return consulta_rango(root, min_val, max_val)
    """Find all values in BST within given range"""
    # Your solution here 🛠️
    pass

# Test 1:
print(range_query(build_bst([7, 3, 11, 1, 5, 9, 13]), 5, 10) == [5, 7, 9])  # 🎯 Normal range
# Test 2: 
print(range_query(build_bst([6, 4, 8, 2]), 1, 10) == [2, 4, 6, 8])  # 📊 Full coverage
# Test 3:
print(range_query(build_bst([20, 10, 30]), 1, 5) == [])  # 📭 Empty result
# Test 4:
print(range_query(build_bst([15]), 10, 20) == [15])  # 🌱 Single node
# Test 5:
print(range_query(build_bst([15, 10, 20, 5, 25]), 10, 20) == [10, 15, 20])  # 🔗 Include boundaries

