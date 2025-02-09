# class Car:
#     def __init__(self, model, prod_year):
#         self.model = model
#         self.prod_year = prod_year

#     def opis(self):
#         print(f'{self.model} jest z {self.prod_year} roku')

# moje_auto = Car("Toyota", 2020)

# moje_auto.opis()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def is_adult(self):
        print(f'{True if self.age >= 18 else False}')

person1 = Person("JANUSZ", 10)
person2 = Person("KARYNA", 20)

person1.is_adult()
person2.is_adult()
