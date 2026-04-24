# -*- coding: utf-8 -*-
"""
Pruebas unitarias para las estructuras definidas en listas.py

Ejecución:
    python -m unittest test_listas.py
    o simplemente:
    python test_listas.py
"""

import unittest
from listas import LinkedList, DoublyLinkedList, CircularLinkedList


# ==============================================================
# Pruebas de LinkedList
# ==============================================================
class TestLinkedList(unittest.TestCase):

    def setUp(self):
        self.lista = LinkedList()

    def test_lista_vacia(self):
        self.assertTrue(self.lista.is_empty())
        self.assertEqual(self.lista.size(), 0)

    def test_insert_front(self):
        self.lista.insert_front(10)
        self.lista.insert_front(20)
        self.assertEqual(self.lista.head.data, 20)
        self.assertEqual(self.lista.head.next.data, 10)
        self.assertEqual(self.lista.size(), 2)

    def test_insert_end(self):
        self.lista.insert_end(1)
        self.lista.insert_end(2)
        self.lista.insert_end(3)
        self.assertEqual(self.lista.head.data, 1)
        self.assertEqual(self.lista.head.next.next.data, 3)
        self.assertEqual(self.lista.size(), 3)

    def test_search(self):
        for n in [1, 2, 3, 4]:
            self.lista.insert_end(n)
        self.assertTrue(self.lista.search(3))
        self.assertFalse(self.lista.search(100))

    def test_delete_existente(self):
        for n in [1, 2, 3]:
            self.lista.insert_end(n)
        self.assertTrue(self.lista.delete(2))
        self.assertFalse(self.lista.search(2))
        self.assertEqual(self.lista.size(), 2)

    def test_delete_cabeza(self):
        for n in [1, 2, 3]:
            self.lista.insert_end(n)
        self.assertTrue(self.lista.delete(1))
        self.assertEqual(self.lista.head.data, 2)

    def test_delete_inexistente(self):
        self.lista.insert_end(1)
        self.assertFalse(self.lista.delete(99))


# ==============================================================
# Pruebas de DoublyLinkedList
# ==============================================================
class TestDoublyLinkedList(unittest.TestCase):

    def setUp(self):
        self.dl = DoublyLinkedList()

    def test_lista_vacia(self):
        self.assertTrue(self.dl.is_empty())
        self.assertEqual(self.dl.size(), 0)

    def test_insert_front(self):
        self.dl.insert_front(10)
        self.dl.insert_front(20)
        self.assertEqual(self.dl.head.data, 20)
        self.assertIsNone(self.dl.head.prev)
        self.assertEqual(self.dl.head.next.data, 10)
        self.assertEqual(self.dl.head.next.prev.data, 20)

    def test_insert_end(self):
        self.dl.insert_end(1)
        self.dl.insert_end(2)
        self.dl.insert_end(3)
        self.assertEqual(self.dl.size(), 3)
        # comprobar enlaces prev
        self.assertEqual(self.dl.head.next.prev.data, 1)
        self.assertEqual(self.dl.head.next.next.prev.data, 2)

    def test_delete_medio(self):
        for n in [1, 2, 3]:
            self.dl.insert_end(n)
        self.assertTrue(self.dl.delete(2))
        # el nodo 3 ahora debería tener como prev al nodo 1
        self.assertEqual(self.dl.head.next.data, 3)
        self.assertEqual(self.dl.head.next.prev.data, 1)

    def test_delete_cabeza(self):
        for n in [1, 2, 3]:
            self.dl.insert_end(n)
        self.assertTrue(self.dl.delete(1))
        self.assertEqual(self.dl.head.data, 2)
        self.assertIsNone(self.dl.head.prev)

    def test_search(self):
        self.dl.insert_end("a")
        self.dl.insert_end("b")
        self.assertTrue(self.dl.search("a"))
        self.assertFalse(self.dl.search("z"))


# ==============================================================
# Pruebas de CircularLinkedList
# ==============================================================
class TestCircularLinkedList(unittest.TestCase):

    def test_circularidad(self):
        cl = CircularLinkedList()
        cl.insert_end(1)
        cl.insert_end(2)
        cl.insert_end(3)
        # El último nodo debe apuntar a la cabeza
        current = cl.head
        while current.next is not cl.head:
            current = current.next
        self.assertIs(current.next, cl.head)

    def test_un_solo_nodo(self):
        cl = CircularLinkedList()
        cl.insert_end("X")
        # Un solo nodo debe apuntarse a sí mismo
        self.assertIs(cl.head.next, cl.head)


if __name__ == "__main__":
    unittest.main(verbosity=2)
