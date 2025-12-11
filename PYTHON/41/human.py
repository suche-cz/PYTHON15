import datetime as dt


class Human:
    def __init__(self, name, birth_year, height, weight):
        self.name = name
        self.birth_year = birth_year
        self.height = height
        self._weight = weight
    
    def __str__(self):
        return f'{self.name} {self.age}'
    
    def __repr__(self):
        return str(self)
    
    def __len__(self):
        return 10
    
    def __add__(self, other):
        return [self, other]
    
    def speak(self, text):
        print(self.name, 'říká', text)
    
    def speak_multiple(self, *args):
        for item in args:
            self.speak(item)
        
    def introduce(self):
        print(f'Jsem {self.name} a narodil jsem se v roce {self.birth_year}')

    def set_weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError('Invalid value')
    
    @property
    def age(self):
        """ dynamicky vypočítaná vlastnost """
        return get_age(self.birth_year)
    
    @classmethod
    def create_human(cls, name, birth_year, height, weight):
        """ toto je tzv faktory metoda, která má na starosti tvorbu nových instancí """
        age = get_age(birth_year)
        if age > 17:
            return AdultHuman(name, birth_year, height, weight)
        else:
            return ChildHuman(name, birth_year, height, weight)


def get_age(birth_year):
    today = dt.date.today()
    age = today.year - birth_year
    return age

class AdultHuman(Human):
    def drive_car(self):
        print('I am driving a car')


class ChildHuman(Human):
    def drive_car(self):
        raise TypeError('Child cannot drive a car')


jana = Human.create_human('Jana', 1996, 170, 58)
print(jana)
print(len(jana))

jan = AdultHuman('Jan', 2000, 174, 80)
nika = ChildHuman('Nika', 2020, 100, 30)

xyz = jana + jan
print(xyz)

jan.drive_car()
# nika.drive_car() # toto je potřeba ošetřit pomocí try except
    

suche = Human('Suche', 1990, 170, 60)
pavel = Human('Pavel', 1950, 180, 70)

suche.speak('Hello Python!')
pavel.speak('Nice code here')

suche.speak_multiple('Ahoj', 'Good Bye', 'Python', 'Nice try!')
suche.introduce()

print(suche._weight)

suche._weight = 100 # přístup k privátní proměnné
