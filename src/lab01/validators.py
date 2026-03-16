"""
Модуль с функциями валидации для класса Patient.
Каждая функция принимает значение и выбрасывает исключение, если оно некорректно.
"""

def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("Имя должно быть строкой")
    if not name.strip():
        raise ValueError("Имя не может быть пустым")

def validate_age(age, max_age=150):
    if not isinstance(age, int):
        raise TypeError("Возраст должен быть целым числом")
    if age < 0 or age > max_age:
        raise ValueError(f"Возраст должен быть от 0 до {max_age}")

def validate_diagnosis(diagnosis):
    if not isinstance(diagnosis, str):
        raise TypeError("Диагноз должен быть строкой")
    if not diagnosis.strip():
        raise ValueError("Диагноз не может быть пустым")

def validate_is_treated(is_treated):
    if not isinstance(is_treated, bool):
        raise TypeError("Статус лечения должен быть булевым")