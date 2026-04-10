from base import Patient
from models import Inpatient, Outpatient
from collection import PatientCollection   # ← теперь из текущей папки

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    print_separator("1. Создание пациентов (базовый и наследники)")
    p1 = Patient("Иван Общий", 45, "ОРВИ")
    p2 = Inpatient("Петр Стационарный", 70, "Перелом шейки бедра",
                   ward_number=101, admission_date="2025-04-01")
    p3 = Outpatient("Мария Амбулаторная", 30, "Аллергия",
                    next_appointment="2025-04-15", clinic_address="ул. Ленина, 5")
    p4 = Inpatient("Сергей Травматолог", 25, "Вывих плеча",
                   ward_number=205, admission_date="2025-04-02", is_treated=True)
    p5 = Outpatient("Елена Кардиолог", 60, "Гипертония",
                    next_appointment="2025-04-10", clinic_address="пр. Мира, 12")

    for p in [p1, p2, p3, p4, p5]:
        print(p.name, "-", type(p).__name__)

    print_separator("2. Добавление в коллекцию")
    registry = PatientCollection()
    for p in [p1, p2, p3, p4, p5]:
        try:
            registry.add(p)
            print(f"Добавлен: {p.name}")
        except ValueError as e:
            print(f"Ошибка: {e}")

    print_separator("3. Содержимое коллекции (__str__ полиморфизм)")
    print(registry)

    print_separator("4. Полиморфный вызов get_treatment_plan()")
    for patient in registry:
        print(f"{patient.name}: {patient.get_treatment_plan()}")

    print_separator("5. Проверка типов через isinstance()")
    for patient in registry:
        if isinstance(patient, Inpatient):
            print(f"{patient.name} - стационарный, палата {patient.ward_number}")
        elif isinstance(patient, Outpatient):
            print(f"{patient.name} - амбулаторный, приём {patient.next_appointment}")
        else:
            print(f"{patient.name} - обычный пациент")

    print_separator("6. Фильтрация: только стационарные пациенты")
    inpatients = [p for p in registry if isinstance(p, Inpatient)]
    print(f"Найдено стационарных: {len(inpatients)}")
    for p in inpatients:
        print(p.name, "-", p.discharge_planned_date())

    print_separator("7. Фильтрация: только амбулаторные")
    outpatients = [p for p in registry if isinstance(p, Outpatient)]
    print(f"Найдено амбулаторных: {len(outpatients)}")
    for p in outpatients:
        print(p.name, "- напоминание:", p.reminder())

    print_separator("8. Три сценария работы")

    print("Сценарий А: Выписка всех лечащихся стационарных пациентов")
    for p in inpatients:
        if not p.is_treated:
            p.discharge()
            print(f"{p.name} выписан. Новый статус: {p.is_treated}")

    print("\nСценарий Б: Отправка напоминаний амбулаторным пациентам")
    for p in outpatients:
        print(p.reminder())

    print("\nСценарий В: Пациенты с диагнозом 'Гипертония'")
    hyper_patients = [p for p in registry if p.diagnosis.lower() == "гипертония"]
    for p in hyper_patients:
        print(f"{p.name} ({type(p).__name__}) - {p.get_treatment_plan()}")

if __name__ == "__main__":
    main()