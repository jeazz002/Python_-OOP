import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
from validators import validate_name
from interfaces import Printable, Comparable

class Doctor(Printable, Comparable):
    def __init__(self, name, specialty, years_of_experience):
        validate_name(name)
        self.__name = name
        self.__specialty = specialty
        self.__years = years_of_experience

    @property
    def name(self):
        return self.__name

    @property
    def specialty(self):
        return self.__specialty

    @property
    def years(self):
        return self.__years

    def to_string(self) -> str:
        return f"Доктор {self.name}, {self.specialty} (стаж {self.years} лет)"

    def compare_to(self, other) -> int:
        if not isinstance(other, Doctor):
            raise TypeError("Можно сравнивать только с Doctor")
        return self.years - other.years

    def __str__(self):
        return self.to_string()