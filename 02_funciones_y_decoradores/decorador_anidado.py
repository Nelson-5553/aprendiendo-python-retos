
def check_access(required_role):
    def decorator(func):
        def wrapper(employee):
            
            if employee.get("rol") == required_role:
                return func(employee)
            else:
                print(f"ACCESO DENEGADO. Solo {required_role} pueden reaclizar es accion")
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f"Registrando accion para el empleado {employee['name']}")
        return func(employee)
    return wrapper

@check_access('admin')
@log_action
def delete_employee(employe):
    print(f"El empleado {employe['name']}, ha sido eliminado")

admin = {'name': 'Carlos', 'rol': 'admin'}
empleado = {'name': 'Ana', 'rol': 'empleado'}

# delete_employee(admin)
delete_employee(empleado)