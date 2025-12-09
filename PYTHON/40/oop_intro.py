class AbstractCar:
    pass


class Car(AbstractCar):
    ENGINE_TYPE = 'petrol'

    def __init__(self, brand, model):
        # init je inicializační funkce
        # zde nastavujeme atributy a nějaké inicializační činnosti
        # toto jsou instanční atributy
        self.brand = brand
        self.model = model
    
    def get_name(self):
        # instanční metoda
        return f'{self.brand} {self.model} ({self.ENGINE_TYPE})'
    
    @classmethod
    def test_method(cls):
        print('test class method')


class EletricCar(AbstractCar):
    ENGINE_TYPE = 'electric'

    def change_battery(self):
        pass


# instance
my_car = Car('Audi', 'A8')
jana_car = Car('BMW', 'X5')
petr_car = EletricCar('Porsche', '911')

print(Car.ENGINE_TYPE)
Car.test_method()

print(my_car.ENGINE_TYPE)

print(my_car.get_name())
print(jana_car.get_name())
print(petr_car.get_name())
