from model import Patient

class PatientCollection:
    """Контейнер для хранения объектов Patient с уникальными именами."""

    def __init__(self):
        self._items = []

    def add(self, patient):
        """Добавляет пациента в коллекцию. Запрещает дубликаты по имени."""
        if not isinstance(patient, Patient):
            raise TypeError("Можно добавлять только объекты Patient")
        # Проверка на дубликат имени
        if any(p.name == patient.name for p in self._items):
            raise ValueError(f"Пациент с именем '{patient.name}' уже существует в коллекции")
        self._items.append(patient)

    def remove(self, patient):
        """Удаляет пациента из коллекции (по объекту)."""
        if patient not in self._items:
            raise ValueError("Пациент не найден в коллекции")
        self._items.remove(patient)

    def remove_at(self, index):
        """Удаляет пациента по индексу."""
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index >= len(self._items):
            raise IndexError("Индекс вне диапазона")
        return self._items.pop(index)

    def get_all(self):
        """Возвращает список всех пациентов."""
        return self._items.copy()

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        """Поддержка индексации collection[i]."""
        return self._items[index]

    # ----- Поиск -----
    def find_by_name(self, name):
        """Возвращает список пациентов с точным совпадением имени."""
        return [p for p in self._items if p.name == name]

    def find_by_age(self, age):
        """Возвращает список пациентов с указанным возрастом."""
        return [p for p in self._items if p.age == age]

    def find_by_diagnosis(self, diagnosis):
        """Возвращает список пациентов с указанным диагнозом."""
        return [p for p in self._items if p.diagnosis == diagnosis]

    def find_by_status(self, is_treated):
        """Возвращает список пациентов с заданным статусом лечения."""
        return [p for p in self._items if p.is_treated == is_treated]

    # ----- Сортировка -----
    def sort(self, key=None, reverse=False):
        """Сортирует коллекцию in-place по заданному ключу."""
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

    # ----- Фильтрация (логические операции) -----
    def get_treated(self):
        """Возвращает новую коллекцию с вылеченными пациентами."""
        new_coll = PatientCollection()
        for p in self._items:
            if p.is_treated:
                new_coll.add(p)
        return new_coll

    def get_untreated(self):
        """Возвращает новую коллекцию с пациентами, которые ещё лечатся."""
        new_coll = PatientCollection()
        for p in self._items:
            if not p.is_treated:
                new_coll.add(p)
        return new_coll

    def get_by_age_group(self, group):
        """group: 'child', 'adult', 'senior'."""
        groups = {'child': lambda p: p.age < 18,
                  'adult': lambda p: 18 <= p.age < 65,
                  'senior': lambda p: p.age >= 65}
        if group not in groups:
            raise ValueError("Группа должна быть 'child', 'adult' или 'senior'")
        new_coll = PatientCollection()
        for p in self._items:
            if groups[group](p):
                new_coll.add(p)
        return new_coll

    def __str__(self):
        if not self._items:
            return "Коллекция пуста"
        return "\n".join(str(p) for p in self._items)