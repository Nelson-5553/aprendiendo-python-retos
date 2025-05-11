
def check_access(func):
    def wrapper(employee):
        
        if employee.get("rol") == 'admin':
            return func(employee)
        else:
            print("ACCESO DENEGADO. Solo administradores pueden acceder")
    
    return wrapper

    #     print("Iniciando log de eliminacion ...") # se ejecuta antes que la funcion procesar_pago()
    #     func()
    #     print("Log de la eliminacion terminado.") # se ejecuta despues que la funcion procesar_pago()
    # return wrapper

@check_access
def delete_employee(employee):
    print(f"Empleado {employee["name"]} ha sido eliminado")

admin = {'name': 'Carlos', 'rol': 'admin'}
empleado = {'name': 'Ana', 'rol': 'empleado'}

# delete_employee(admin)
delete_employee(empleado)
