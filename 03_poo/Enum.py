from enum import Enum

class EstadoOrden(Enum):
    PENDIENTE = 1
    ENVIADO = 2
    ENTREGADO = 3

def verificar_estado_orden(status):
    if status == EstadoOrden.PENDIENTE:
        return "La orden está pendiente."
    elif status == EstadoOrden.ENVIADO:
        return "La orden ha sido enviada."
    elif status == EstadoOrden.ENTREGADO:
        return "La orden ha sido entregada."

estado_actual = EstadoOrden.ENVIADO
print(verificar_estado_orden(estado_actual))  # Output: La orden ha sido enviada. 