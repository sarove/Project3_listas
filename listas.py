# -*- coding: utf-8 -*-
"""
Parte C — Listas Enlazadas
Implementación de estructuras de datos lineales basadas en nodos.

Contiene:
    - LinkedList         : Lista enlazada simple
    - DoublyLinkedList   : Lista doblemente enlazada
    - CircularLinkedList : Lista circular simple (extra, según presentación)

Autor: Salvador Rodriguez V -UAO — Estructuras de Datos y Algoritmos 1
"""


# ==============================================================
# Nodo para lista simple
# ==============================================================
class Node:
    """Nodo de una lista enlazada simple.

    Atributos:
        data: valor almacenado en el nodo.
        next: referencia al siguiente nodo (None si es el último).
    """

    def __init__(self, data):
        self.data = data
        self.next = None


# ==============================================================
# TODO 5: Lista enlazada simple
# ==============================================================
class LinkedList:
    """Lista enlazada simple.

    Operaciones soportadas:
        - insert_front(data): inserta al inicio       -> O(1)
        - insert_end(data)  : inserta al final        -> O(n)
        - delete(data)      : elimina la 1ª ocurrencia-> O(n)
        - search(data)      : busca un valor          -> O(n)
        - traverse()        : imprime la lista        -> O(n)
        - size()            : cantidad de nodos       -> O(n)
        - is_empty()        : indica si está vacía    -> O(1)
    """

    def __init__(self):
        self.head = None

    # ---------- Inserciones ----------
    def insert_front(self, data):
        """Inserta un nuevo nodo al inicio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        """Inserta un nuevo nodo al final de la lista."""
        new_node = Node(data)
        # Caso 1: lista vacía -> el nuevo nodo es la cabeza
        if self.head is None:
            self.head = new_node
            return
        # Caso 2: recorrer hasta el último nodo
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node

    # ---------- Eliminación ----------
    def delete(self, data):
        """Elimina la primera ocurrencia del valor 'data'.

        Retorna True si se eliminó, False si no se encontró.
        """
        if self.head is None:
            return False

        # Caso 1: el valor está en la cabeza
        if self.head.data == data:
            self.head = self.head.next
            return True

        # Caso 2: buscar en el resto de la lista
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next

        if current.next is None:
            return False  # No se encontró

        current.next = current.next.next
        return True

    # ---------- Búsqueda ----------
    def search(self, data):
        """Retorna True si 'data' está presente en la lista."""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    # ---------- Utilidades ----------
    def size(self):
        """Retorna la cantidad de nodos de la lista."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Retorna True si la lista está vacía."""
        return self.head is None

    # ---------- Recorrido ----------
    def traverse(self):
        """Recorre la lista e imprime cada dato en formato:
        d1 -> d2 -> d3 -> None
        """
        if self.head is None:
            print("Lista vacía -> None")
            return

        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# ==============================================================
# Nodo para lista doblemente enlazada
# ==============================================================
class DNode:
    """Nodo de una lista doblemente enlazada.

    Atributos:
        data: valor almacenado.
        prev: referencia al nodo anterior (None si es el primero).
        next: referencia al nodo siguiente (None si es el último).
    """

    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# ==============================================================
# TODO 6: Lista doblemente enlazada
# ==============================================================
class DoublyLinkedList:
    """Lista doblemente enlazada.

    Operaciones soportadas:
        - insert_front(data)   : inserta al inicio              -> O(1)
        - insert_end(data)     : inserta al final               -> O(n)
        - delete(data)         : elimina la 1ª ocurrencia       -> O(n)
        - search(data)         : busca un valor                 -> O(n)
        - traverse_forward()   : recorre de inicio a fin        -> O(n)
        - traverse_backward()  : recorre de fin a inicio        -> O(n)
        - size()               : cantidad de nodos              -> O(n)
        - is_empty()           : indica si está vacía           -> O(1)
    """

    def __init__(self):
        self.head = None

    # ---------- Inserciones ----------
    def insert_front(self, data):
        """Inserta un nuevo nodo al inicio."""
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        """Inserta un nuevo nodo al final."""
        new_node = DNode(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current

    # ---------- Eliminación ----------
    def delete(self, data):
        """Elimina la primera ocurrencia de 'data'.

        Retorna True si se eliminó, False si no se encontró.
        """
        current = self.head
        while current is not None and current.data != data:
            current = current.next

        if current is None:
            return False  # No encontrado

        # Reconectar el nodo anterior
        if current.prev is not None:
            current.prev.next = current.next
        else:
            # Si no tiene anterior, es la cabeza
            self.head = current.next

        # Reconectar el nodo siguiente
        if current.next is not None:
            current.next.prev = current.prev

        return True

    # ---------- Búsqueda ----------
    def search(self, data):
        """Retorna True si 'data' está presente en la lista."""
        current = self.head
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False

    # ---------- Utilidades ----------
    def size(self):
        """Retorna la cantidad de nodos."""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Retorna True si la lista está vacía."""
        return self.head is None

    # ---------- Recorridos ----------
    def traverse_forward(self):
        """Recorre la lista de inicio a fin.
        Formato: None <- d1 <-> d2 <-> d3 -> None
        """
        if self.head is None:
            print("Lista vacía -> None")
            return

        print("None <- ", end="")
        current = self.head
        while current is not None:
            print(current.data, end="")
            if current.next is not None:
                print(" <-> ", end="")
            current = current.next
        print(" -> None")

    def traverse_backward(self):
        """Recorre la lista de fin a inicio.
        Formato: None <- dn <-> ... <-> d1 -> None
        """
        if self.head is None:
            print("Lista vacía -> None")
            return

        # Avanzar hasta el último nodo
        current = self.head
        while current.next is not None:
            current = current.next

        # Recorrer hacia atrás
        print("None <- ", end="")
        while current is not None:
            print(current.data, end="")
            if current.prev is not None:
                print(" <-> ", end="")
            current = current.prev
        print(" -> None")


# ==============================================================
# EXTRA: Lista Circular (según la presentación, pág. "Lista circular")
# ==============================================================
class CircularLinkedList:
    """Lista circular simple: el último nodo apunta al primero.

    Útil para aplicaciones cíclicas como buffers, juegos por turnos,
    planificadores Round-Robin, etc.
    """

    def __init__(self):
        self.head = None

    def insert_end(self, data):
        """Inserta un nodo al final manteniendo la circularidad."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # apunta a sí mismo
            return
        current = self.head
        while current.next is not self.head:
            current = current.next
        current.next = new_node
        new_node.next = self.head

    def traverse(self, max_vueltas=1):
        """Recorre la lista circular el número de vueltas indicado."""
        if self.head is None:
            print("Lista vacía")
            return

        for _ in range(max_vueltas):
            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current is self.head:
                    break
        print("(head)")


# ==============================================================
# Programa principal (demostración)
# ==============================================================
if __name__ == "__main__":
    print("=" * 55)
    print("  DEMOSTRACIÓN - LISTAS ENLAZADAS (Semana 5)")
    print("=" * 55)

    # -------- Lista enlazada simple --------
    print("\n[1] Lista enlazada simple:")
    l = LinkedList()
    l.insert_front(10)     # 10
    l.insert_end(20)       # 10 -> 20
    l.insert_end(30)       # 10 -> 20 -> 30
    l.insert_front(5)      # 5 -> 10 -> 20 -> 30
    print("  Contenido:    ", end="")
    l.traverse()
    print(f"  Tamaño:        {l.size()}")
    print(f"  ¿Contiene 20?: {l.search(20)}")
    print(f"  ¿Contiene 99?: {l.search(99)}")

    print("  Eliminando 20...")
    l.delete(20)
    print("  Contenido:    ", end="")
    l.traverse()

    # -------- Lista doblemente enlazada --------
    print("\n[2] Lista doblemente enlazada:")
    dl = DoublyLinkedList()
    dl.insert_front(1)
    dl.insert_end(2)
    dl.insert_end(3)
    dl.insert_front(0)     # 0 <-> 1 <-> 2 <-> 3
    print("  Adelante:  ", end="")
    dl.traverse_forward()
    print("  Atrás:     ", end="")
    dl.traverse_backward()
    print(f"  Tamaño:     {dl.size()}")

    print("  Eliminando 2...")
    dl.delete(2)
    print("  Adelante:  ", end="")
    dl.traverse_forward()

    # -------- Lista circular --------
    print("\n[3] Lista circular (extra):")
    cl = CircularLinkedList()
    cl.insert_end("A")
    cl.insert_end("B")
    cl.insert_end("C")
    print("  Una vuelta:    ", end="")
    cl.traverse(max_vueltas=1)
    print("  Dos vueltas:   ", end="")
    cl.traverse(max_vueltas=2)

    print("\n" + "=" * 55)
    print("  FIN DE LA DEMOSTRACIÓN")
    print("=" * 55)
