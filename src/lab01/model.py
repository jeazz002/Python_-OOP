"""
Модуль с классом Patient, использующим валидацию из validators.py.
"""

from validators import validate_name, validate_age, validate_diagnosis, validate_is_treated
class Patient:
    # Атрибуты класса
    total_patients = 0       # счётчик созданных пациентов
    MAX_AGE = 150            # максимальный допустимый возраст

    def __init__(self, name, age, diagnosis, is_treated=False):
        """
        Конструктор пациента.
        Выполняет проверку переданных данных через функции валидации.
        """
        validate_name(name)
        validate_age(age, self.MAX_AGE)
        validate_diagnosis(diagnosis)
        validate_is_treated(is_treated)

        self.__name = name
        self.__age = age
        self.__diagnosis = diagnosis
        self.__is_treated = is_treated   # False - лечится, True - вылечен

        Patient.total_patients += 1

    # ---- Свойства (getters/setters) ----
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        validate_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        validate_age(value, self.MAX_AGE)
        self.__age = value

    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        validate_diagnosis(value)
        self.__diagnosis = value

    @property
    def is_treated(self):
        return self.__is_treated

    @is_treated.setter
    def is_treated(self, value):
        validate_is_treated(value)
        self.__is_treated = value

    # ---- Бизнес-методы ----
    def admit(self):
        """
        Перевести пациента в статус "лечится".
        """
        self.is_treated = False
        return f" Пациент {self.name} поступил на лечение."

    def discharge(self):
        """
        Выписать пациента (статус "вылечен").
        """
        self.is_treated = True
        return f" Пациент {self.name} выписан."

    def set_diagnosis(self, new_diagnosis):
        """
        Изменить диагноз. Запрещено, если пациент уже вылечен.
        """
        if self.is_treated:
            raise ValueError("Нельзя изменить диагноз вылеченному пациенту.")
        validate_diagnosis(new_diagnosis)
        self.__diagnosis = new_diagnosis
        return f" Диагноз пациента {self.name} изменён на '{new_diagnosis}'."

    def get_age_group(self):
        """
        Возвращает возрастную группу: child (0-17), adult (18-64), senior (65+).
        """
        if self.age < 18:
            return "child"
        elif self.age < 65:
            return "adult"
        else:
            return "senior"

    # ---- Специальные методы ----
    def __str__(self):
        status = "лечится" if not self.is_treated else "вылечен"
        return (f"Пациент: {self.name}\n"
                f"Возраст: {self.age} ({self.get_age_group()})\n"
                f"Диагноз: {self.diagnosis}\n"
                f"Статус: {status}")

    def __repr__(self):
        return f"Patient(name='{self.name}', age={self.age}, diagnosis='{self.diagnosis}', is_treated={self.is_treated})"

    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return self.name == other.name