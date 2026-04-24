# Proyecto: Listas Enlazadas (Semana 5)

**Curso:** Estructuras de Datos y Algoritmos 1
**Tema:** Listas enlazadas — implementación en Python
**Docente:** Jack Marquez — UAO

---

## 📖 Descripción

Este proyecto implementa desde cero tres tipos de **listas enlazadas** en Python, basado en los temas vistos en la presentación de la Semana 5:

1. **Lista enlazada simple** (`LinkedList`)
2. **Lista doblemente enlazada** (`DoublyLinkedList`)
3. **Lista circular simple** (`CircularLinkedList`) — añadida como extensión, ya que aparece en la presentación.

Todas las estructuras se construyen utilizando **nodos** (`Node`, `DNode`), sin usar las estructuras integradas `list` de Python, para reforzar el concepto de estructura dinámica basada en enlaces.

---

## 📁 Estructura del proyecto

```
proyecto_listas/
├── listas.py              # Implementación principal (código fuente)
├── test_listas.py         # Pruebas unitarias (unittest)
└── README.md              # Este archivo
```

---

## ⚙️ Requisitos

- **Python 3.8** o superior
- No se requieren librerías externas (solo la biblioteca estándar)

Verifica tu versión de Python con:

```bash
python --version
```

---

## ▶️ Cómo ejecutar la aplicación

### 1. Ejecutar la demostración principal

Desde la carpeta del proyecto, ejecuta:

```bash
python listas.py
```

Verás una salida similar a:

```
=======================================================
  DEMOSTRACIÓN - LISTAS ENLAZADAS (Semana 5)
=======================================================

[1] Lista enlazada simple:
  Contenido:    5 -> 10 -> 20 -> 30 -> None
  Tamaño:        4
  ¿Contiene 20?: True
  ¿Contiene 99?: False
  Eliminando 20...
  Contenido:    5 -> 10 -> 30 -> None

[2] Lista doblemente enlazada:
  Adelante:  None <- 0 <-> 1 <-> 2 <-> 3 -> None
  Atrás:     None <- 3 <-> 2 <-> 1 <-> 0 -> None
  Tamaño:     4
  Eliminando 2...
  Adelante:  None <- 0 <-> 1 <-> 3 -> None

[3] Lista circular (extra):
  Una vuelta:    A -> B -> C -> (head)
  Dos vueltas:   A -> B -> C -> A -> B -> C -> (head)
```

### 2. Ejecutar las pruebas unitarias

```bash
python test_listas.py
```

O bien:

```bash
python -m unittest test_listas.py -v
```

---

## 🔧 Funcionalidades implementadas

### 🔹 `LinkedList` — Lista enlazada simple

| Método | Descripción | Complejidad |
|---|---|---|
| `insert_front(data)` | Inserta un elemento al inicio de la lista | O(1) |
| `insert_end(data)` | Inserta un elemento al final de la lista | O(n) |
| `delete(data)` | Elimina la primera ocurrencia del valor | O(n) |
| `search(data)` | Busca un valor, retorna `True`/`False` | O(n) |
| `size()` | Retorna la cantidad de nodos | O(n) |
| `is_empty()` | Indica si la lista está vacía | O(1) |
| `traverse()` | Imprime la lista en formato `d1 -> d2 -> None` | O(n) |

### 🔹 `DoublyLinkedList` — Lista doblemente enlazada

| Método | Descripción | Complejidad |
|---|---|---|
| `insert_front(data)` | Inserta al inicio | O(1) |
| `insert_end(data)` | Inserta al final | O(n) |
| `delete(data)` | Elimina la primera ocurrencia | O(n) |
| `search(data)` | Busca un valor | O(n) |
| `size()` | Cantidad de nodos | O(n) |
| `is_empty()` | Indica si está vacía | O(1) |
| `traverse_forward()` | Recorre de inicio a fin | O(n) |
| `traverse_backward()` | Recorre de fin a inicio | O(n) |

### 🔹 `CircularLinkedList` — Lista circular (extra)

| Método | Descripción |
|---|---|
| `insert_end(data)` | Inserta al final manteniendo la circularidad |
| `traverse(max_vueltas)` | Recorre la lista el número de vueltas indicado |

---

## 🧠 Conceptos clave (resumen de la presentación)

- Una **lista enlazada** es una estructura de datos **lineal** y **dinámica** formada por **nodos**.
- Cada nodo contiene un **dato** y una o más **referencias (enlaces)** a otros nodos.
- El primer nodo se llama **cabeza (`head`)** y el último apunta a `None` (en listas simples).
- **Ventajas:** inserciones y eliminaciones eficientes en cualquier posición.
- **Desventajas:** acceso secuencial (no se puede indexar en O(1)) y memoria adicional por los punteros.

### Tipos de listas

| Tipo | Enlaces | Característica |
|---|---|---|
| **Simple** | `next` | El último nodo apunta a `None` |
| **Doble** | `prev` + `next` | Se puede recorrer en ambas direcciones |
| **Circular** | `next` | El último nodo apunta al primero |

### Aplicaciones reales

- Implementación de **pilas** y **colas**
- **Gestión dinámica** de memoria
- **Listas de reproducción** de música (siguiente/anterior)
- **Historial** de navegadores (atrás/adelante)
- **Planificadores Round-Robin** (usando listas circulares)

---

## 📝 Ejemplo de uso desde otro script

Puedes importar las clases desde otro archivo Python:

```python
from listas import LinkedList, DoublyLinkedList

# Lista simple
mi_lista = LinkedList()
mi_lista.insert_end("Manzana")
mi_lista.insert_end("Banana")
mi_lista.insert_front("Aguacate")
mi_lista.traverse()
# Salida: Aguacate -> Manzana -> Banana -> None

# Lista doble
dl = DoublyLinkedList()
dl.insert_end(1)
dl.insert_end(2)
dl.insert_front(0)
dl.traverse_forward()
# Salida: None <- 0 <-> 1 <-> 2 -> None
```

---

## 🐛 Problemas comunes y soluciones

| Problema | Causa | Solución |
|---|---|---|
| `python: command not found` | Python no está en el PATH | Usa `python3` en vez de `python`, o instala Python |
| Caracteres raros en la consola (Windows) | Codificación diferente a UTF-8 | Ejecuta `chcp 65001` antes de correr el script |
| `ModuleNotFoundError: listas` al correr tests | Estás en otra carpeta | Ejecuta los tests desde `proyecto_listas/` |

---

## 👤 Autor

- **Curso:** Estructuras de Datos y Algoritmos 1
- **Semana:** 5 — Colas (Queues)
- **Estudiante:** Salvador Rodriguez —Jorge Luis Velasquez- Universidad Autónoma de Occidente (UAO)
- **Contacto:** salvador.rodriguez_v@uao.edu.co, Jorge_luis.velasquez@uao.edu.co

---
