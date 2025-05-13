# Uso de args

def sum_numbers(*args):
    return sum(args)

# print (sum_numbers(1, 2, 3, 4, 5))
# print (sum_numbers(1, 2))
# print (sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#Uso de Kwargs

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


# print_info(name='Carlos', age=30, city='Bogota', country="Colombia" )

class Employee:

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.skill = args
        self.details = kwargs

    def show_employee(self):
        print(f'Employee: {self.name}')
        print('Employee:', self.skill)
        print('Details:', self.details)

employee = Employee('Carlos', 'python', 'Java', 'PHP', age=20, country="Colombia")
print(employee.show_employee())