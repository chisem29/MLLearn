from typing import Any
from dataclasses import dataclass
from collections import namedtuple

class TypingText :

    """def __init__(self, attr_name) : НЕ ИСПОЛЬЗОВАТЬ
        self.attr_name = f'_{attr_name}'
        self.l = [] """
    
    def __set_name__(self, owner, name : str) -> None : # WELL WELL WELL
        self.attr_name = f'_{name}'
        self.l = []
        print(name, owner)

    def __get__(self, intance, owner=None) -> Any : # срабатывает при вызове класса
        return getattr(intance, self.attr_name)
    
    def __set__(self, intance, value : Any) -> None : # срабатывает при изменении 
        self.l.append(value)
        setattr(intance, self.attr_name, self.l)
        
    def __delete__(self, intance) -> None : # срабатывает при удалении класса
        self.l = []
        delattr(intance, self.attr_name)

class MyTypingText :
    x = TypingText()

cl = MyTypingText()
text = 'I ll catch the world'
for c in text :
    cl.x = c
print(cl.x)
del cl.x

class Obj :
    __slots__ = ['name', 'age', '_surname']
    def __init__(self) -> None:
        self._surname = None
    @property
    def surname(self) :
        return self._surname
    @surname.setter
    def surname(self, value) :
        self._surname = f'{value} Jopa'
    @surname.getter
    def surname(self) :
        return self._surname

person = Obj()
person.name = 'Jhon'
person.age = 23
person.surname = 'Banditov'

print(person.surname)

try :
    person.loc = 'Mexixco'
except AttributeError :
    print('Нельзя создать т.к заданы ограничения у атрибутов с помощью __slots__!!!!')

@dataclass
class Actor :
    name:str
    age:int
    country:str=None

@dataclass(frozen=True)
class Film :
    title:str
    actors:list[Actor]
    year:int

opengaymer = Film(
    title='Opengaymer', 
    actors=[
        Actor(name=name, age=age, country=country) 
        for name, age, country in [["Bob", 21, 'US'], ["Pidor", 43, 'US'], ['Jack', 19, 'US']]
    ], 
    year=2023
)

print(opengaymer.actors)

Book = namedtuple('Book', ['title', 'author'])

MathBook = Book(title='Math', author='Sigma')

class Cat :
    c = 0
    def __init__(self) -> None:
        Cat.c = Cat.c+1
    
    @classmethod
    def count(cls) :
        print(cls.c)
        
    @staticmethod
    def who() :
        return 'I am cat'
    
for i in range(4) :
    Cat()
    
Cat.count()
