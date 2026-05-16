from typing import List, Optional
from models import Patient
from collection import TypedCollection
from exceptions import ItemNotFoundError, DuplicateItemError
import storage

class PatientApp:

    def __init__(self, filepath: str = "patients.json") -> None:   
        self.filepath = filepath
        self.collection = TypedCollection[Patient]()
        self._load_from_file()

    def _load_from_file(self) -> None:
        patients = storage.load(self.filepath)
        for p in patients:
            self.collection.add(p)

    def save_to_file(self) -> None:
        storage.save(self.collection.get_all(), self.filepath)

    def add_patient(self, name: str, age: int, diagnosis: str, is_treated: bool = False) -> None:
        if self.collection.find(lambda p: p.name == name) is not None:
            raise DuplicateItemError(f"Пациент с именем '{name}' уже существует.")
        patient = Patient(name, age, diagnosis, is_treated)
        self.collection.add(patient)

    def remove_patient_by_name(self, name: str) -> None:
        patient = self.collection.find(lambda p: p.name == name)
        if patient is None:
            raise ItemNotFoundError(f"Пациент '{name}' не найден.")
        self.collection.remove(patient)

    def edit_patient_diagnosis(self, name: str, new_diagnosis: str) -> None:
        patient = self.collection.find(lambda p: p.name == name)
        if patient is None:
            raise ItemNotFoundError(f"Пациент '{name}' не найден.")
        patient.set_diagnosis(new_diagnosis)

    def get_all_patients(self) -> List[Patient]:
        return self.collection.get_all()

    def find_patient_by_name(self, name: str) -> Optional[Patient]:
        return self.collection.find(lambda p: p.name == name)

    def filter_by_diagnosis(self, diagnosis: str) -> List[Patient]:
        return self.collection.filter(lambda p: p.diagnosis.lower() == diagnosis.lower())

    def filter_by_age_range(self, min_age: int, max_age: int) -> List[Patient]:
        return self.collection.filter(lambda p: min_age <= p.age <= max_age)

    def sort_patients(self, key: str, reverse: bool = False) -> None:
        key_map = {
            'name': lambda p: p.name,
            'age': lambda p: p.age,
            'diagnosis': lambda p: p.diagnosis
        }
        if key not in key_map:
            raise ValueError("Недопустимый ключ сортировки")
        self.collection.sort_by(key_map[key], reverse=reverse)