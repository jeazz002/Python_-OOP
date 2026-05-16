import json
from typing import List, Dict, Any
from models import Patient

def save(collection: List[Patient], filepath: str = "patients.json") -> None:
    data = []
    for p in collection:
        data.append({
            "name": p.name,
            "age": p.age,
            "diagnosis": p.diagnosis,
            "is_treated": p.is_treated
        })
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def load(filepath: str = "patients.json") -> List[Patient]:
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

    patients = []
    for item in data:
        patients.append(Patient(
            name=item["name"],
            age=item["age"],
            diagnosis=item["diagnosis"],
            is_treated=item["is_treated"]
        ))
    return patients