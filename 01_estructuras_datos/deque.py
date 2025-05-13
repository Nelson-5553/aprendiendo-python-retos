from collections import deque

def manejar_ordenes():
    ordenes = deque(['orden1', 'orden2', 'orden3'])
    ordenes.append('orden4')  # Añadir al final
    ordenes.appendleft('orden0')  # Añadir al inicio
    print(ordenes)  # Output: deque(['orden0', 'orden1', 'orden2', 'orden3', 'orden4'])
    ordenes.pop()  # Eliminar del final
    ordenes.popleft()  # Eliminar del inicio
    print(ordenes)  # Output: deque(['orden1', 'orden2', 'orden3'])

manejar_ordenes()