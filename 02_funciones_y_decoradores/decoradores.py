# def procesar_pago():
#     print("Procesando pago...")

def log_decorator(func):
    def wrapper():
        print("Iniciando log de la transacción...") # se ejecuta antes que la funcion procesar_pago()
        func()
        print("Log de la transacción terminado.") # se ejecuta despues que la funcion procesar_pago()
    return wrapper

@log_decorator
def procesar_pago():
    print("Procesando pago...")

procesar_pago()