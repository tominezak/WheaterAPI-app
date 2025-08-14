class Car:
    def __init__(self, model, year, color, for_sale): # konstruktør, initialiserer objekter
        self.model = model # når vi får en model settes self.model til den verdien son representerer objektet
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f'You are driving the {self.color} {self.model}!')

    def stop(self):
        print(f'You have stopped the {self.color} {self.model}!')

    def describe(self):
        print(f'{self.year} {self.color} {self.model} - For Sale: {self.for_sale}')
    
