from base import Patient   # ← правильный импорт

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

    def find_by_name(self, name):
        return [p for p in self._items if p.name == name]

    def find_by_age(self, age):
        return [p for p in self._items if p.age == age]

    def find_by_diagnosis(self, diagnosis):
        return [p for p in self._items if p.diagnosis == diagnosis]

    def find_by_status(self, is_treated):
        return [p for p in self._items if p.is_treated == is_treated]

    def sort(self, key=None, reverse=False):
        if key is None:
            self._items.sort(key=lambda p: p.name, reverse=reverse)
        else:
            self._items.sort(key=key, reverse=reverse)

    def sort_by_name(self, reverse=False):
        self.sort(key=lambda p: p.name, reverse=reverse)

    def sort_by_age(self, reverse=False):
        self.sort(key=lambda p: p.age, reverse=reverse)

    def sort_by_diagnosis(self, reverse=False):
        self.sort(key=lambda p: p.diagnosis, reverse=reverse)

    def __str__(self):
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(p) for p in self._items)