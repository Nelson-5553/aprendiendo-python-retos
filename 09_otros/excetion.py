def print_exception_hierarchy(exception_class, indent=0):
    print(' ' * indent + exception_class.__name__)
    for subclass in exception_class.__subclasses__():
        print_exception_hierarchy(subclass, indent + 4)

# print_exception_hierarchy(Exception) 

def division(a: int, b: int) -> float:
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError ("ambos parametros deben ser enteros o flotantes")

    if b == 0:
        raise ValueError("el divisor numero no puede ser 0")
        
    return print(a / b)

# division(10, 2)
# division(10, 0)
# division(10, "2")

# Excepciones de tipo
try: 
    res =  division(10, "2")
    print(res)

except TypeError as e:
    print(f"Error: {e}")

# Excepciones de valor
try: 
    res =  division(10, 0)
    print(res)

except ValueError as e:
    print(f"Error: {e}")

# Excepciones de ambos
try: 
    res =  division(10, 0)
    print(res)

except (ValueError, TypeError) as e:
    print(f"Error: {e}")
