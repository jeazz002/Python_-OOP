from typing import Any

class Patient:
    total_patients: int = 0
    MAX_AGE: int = 150

    def __init__(self, name: str, age: int, diagnosis: str, is_treated: bool = False) -> None:
        self.__name: str = name
        self.__age: int = age
        self.__diagnosis: str = diagnosis
        self.__is_treated: bool = is_treated
        Patient.total_patients += 1

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @property
    def age(self) -> int:
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        self.__age = value

    @property
    def diagnosis(self) -> str:
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, value: str) -> None:
        self.__diagnosis = value

    @property
    def is_treated(self) -> bool:
        return self.__is_treated

    @is_treated.setter
    def is_treated(self, value: bool) -> None:
        self.__is_treated = value

    def admit(self) -> str:
        self.is_treated = False
        return f"Пациент {self.name} поступил на лечение."

    def discharge(self) -> str:
        self.is_treated = True
        return f"Пациент {self.name} выписан."

    def set_diagnosis(self, new_diagnosis: str) -> str:
        if self.is_treated:
            raise ValueError("Нельзя изменить диагноз вылеченному пациенту.")
        self.__diagnosis = new_diagnosis
        return f"Диагноз пациента {self.name} изменён на '{new_diagnosis}'."

    def get_age_group(self) -> str:
        if self.age < 18:
            return "child"
        elif self.age < 65:
            return "adult"
        else:
            return "senior"

    def display(self) -> str:
        return f"Patient: {self.name}, {self.diagnosis}"

    def score(self) -> float:
        return 1.0

    def __str__(self) -> str:
        status = "лечится" if not self.is_treated else "вылечен"
        return (f"Пациент: {self.name}\n"
                f"Возраст: {self.age} ({self.get_age_group()})\n"
                f"Диагноз: {self.diagnosis}\n"
                f"Статус: {status}")

    def __repr__(self) -> str:
        return (f"Patient(name='{self.name}', age={self.age}, "
                f"diagnosis='{self.diagnosis}', is_treated={self.is_treated})")

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Patient):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)

    def to_string(self) -> str:
        return f"{self.name} ({self.age} лет, {self.diagnosis})"

    def compare_to(self, other: 'Patient') -> int:
        if not isinstance(other, Patient):
            raise TypeError("Можно сравнивать только с Patient")
        return self.age - other.age