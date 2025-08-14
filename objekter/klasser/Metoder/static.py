# static method = a method that belongs to the class, not to any specific instance of the class.

class Employee:
    def __init__(self, name, posistion):
        self.name = name
        self.posistion = posistion

    def get_info(self): # dette er en instansmetode, den må kalles på et objekt
        return f'Employee Name: {self.name}, Position: {self.posistion}'
    
    @staticmethod
    def is_valid_position(position):
        valid_positions = ['Manager', 'Cashier', 'Cook', 'Janitor']
        return position in valid_positions

print(Employee.is_valid_position('Manager')) # statisk metoder kan kalles uten å opprette et objekt

employee1 = Employee('John Doe', 'Manager') # må opprette et objekt for å bruke instansmetoder
employee2 = Employee('Jane Smith', 'Cashier')
employee3 = Employee('Alice Johnson', 'Cook')

print(employee1.get_info())