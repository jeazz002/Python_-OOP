from typing import Any

class Patient:
    total_patients: int = 0

    def __init__(self, name: str, age: int, diagnosis: str, is_treated: bool = False) -> None:
        self._name: str = name
        self._age: int = age
        self._diagnosis: str = diagnosis
        self._is_treated: bool = is_treated
        Patient.total_patients += 1

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def diagnosis(self) -> str:
        return self._diagnosis

    @property
    def is_treated(self) -> bool:
        return self._is_treated

    def discharge(self) -> None:
        self._is_treated = True

    def __str__(self) -> str:
        status = "вылечен" if self._is_treated else "лечится"
        return f"{self._name} | {self._age} лет | {self._diagnosis} | {status}"

    def to_string(self) -> str:
        return f"{self._name} ({self._age} лет, {self._diagnosis})"

    def display(self) -> str:
        return f"Patient: {self._name}, {self._diagnosis}"

    def score(self) -> float:
        return 1.0

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Patient):
            return False
        return self.name == other.name

    def __hash__(self) -> int:
        return hash(self.name)


class Doctor:
    def __init__(self, name: str, specialty: str, years: int) -> None:
        self._name = name
        self._specialty = specialty
        self._years = years

    @property
    def name(self) -> str:
        return self._name

    @property
    def specialty(self) -> str:
        return self._specialty

    @property
    def years(self) -> int:
        return self._years

    def display(self) -> str:
        return f"Doctor: {self._name}, {self._specialty} (exp {self._years})"

    def __str__(self) -> str:
        return self.display()