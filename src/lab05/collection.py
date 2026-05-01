import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab04'))

from model import Patient
from interfaces import Printable, Comparable 

class PatientCollection:

    def __init__(self):
        self._items = []

    def add(self, patient):
        if not isinstance(patient, Patient):
            raise TypeError("Можно добавлять только объекты Patient")
        if any(p.name == patient.name for p in self._items):
            raise ValueError(f"Пациент с именем '{patient.name}' уже существует в коллекции")
        self._items.append(patient)

    def remove(self, patient):
        if patient not in self._items:
            raise ValueError("Пациент не найден в коллекции")
        self._items.remove(patient)

    def remove_at(self, index):
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def get_all(self):
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        return self._items[index]

    def __str__(self):
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(p) for p in self._items)

    def sort_by(self, key_func, reverse=False):

        self._items.sort(key=key_func, reverse=reverse)
        return self

    def filter_by(self, predicate):
        new_collection = PatientCollection()
        for item in self._items:
            if predicate(item):
                new_collection.add(item)
        return new_collection

    def apply(self, func):
        for item in self._items:
            func(item)
        return self

    def sort_by_name(self, reverse=False):
        return self.sort_by(key_func=lambda p: p.name, reverse=reverse)

    def sort_by_age(self, reverse=False):
        return self.sort_by(key_func=lambda p: p.age, reverse=reverse)