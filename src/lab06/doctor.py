from typing import Any


class Doctor:
    def __init__(self, name: str, specialty: str, years_of_experience: int) -> None:
        self.__name: str = name
        self.__specialty: str = specialty
        self.__years: int = years_of_experience

    @property
    def name(self) -> str:
        return self.__name

    @property
    def specialty(self) -> str:
        return self.__specialty

    @property
    def years(self) -> int:
        return self.__years

    def display(self) -> str:
        return f"Doctor: {self.name}, {self.specialty}, experience {self.years} years"

    def score(self) -> float:
        return self.years / 10.0

    def __str__(self) -> str:
        return self.display()

    def __repr__(self) -> str:
        return f"Doctor(name='{self.name}', specialty='{self.specialty}', years={self.years})"

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Doctor):
            return False
        return self.name == other.name