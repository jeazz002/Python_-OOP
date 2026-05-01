def by_name(obj):
    return obj.name


def by_age(obj):
    return obj.age


def by_diagnosis(obj):
    return obj.diagnosis


def by_years(obj):
    return obj.years


def by_age_then_name(obj):
    return (obj.age, obj.name)


def is_adult(patient):
    return patient.age >= 18


def is_child(patient):
    return patient.age < 18


def is_senior(patient):
    return patient.age >= 65


def is_treated(patient):
    return patient.is_treated


def is_untreated(patient):
    return not patient.is_treated


def is_doctor(obj):
    from models import Doctor 

    return isinstance(obj, Doctor)


def is_patient(obj):
    from model import Patient

    return isinstance(obj, Patient)


# функции-фильтры
def make_age_filter(min_age=0, max_age=150):

    def age_filter(obj):
        return hasattr(obj, "age") and (min_age <= obj.age <= max_age)

    return age_filter


class DischargeStrategy:
   
    def __call__(self, patient):
        if hasattr(patient, "discharge"):
            patient.discharge()
        return patient


class IncrementAgeStrategy:

    def __call__(self, patient):
        if hasattr(patient, "age"):
            patient.age += 1
        return patient


class AddPrefixToDiagnosis:

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, patient):
        if hasattr(patient, "diagnosis") and patient.diagnosis:
            patient.diagnosis = f"{self.prefix}{patient.diagnosis}"
        return patient


def extract_name(obj):
    return obj.name


def apply_discount(patient):
    if hasattr(patient, "diagnosis"):
        patient.diagnosis = f"{patient.diagnosis} (со скидкой)"
    return patient
