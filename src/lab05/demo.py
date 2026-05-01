import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab04'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'lab05')) 

from model import Patient
from collection import PatientCollection
from models import Doctor         
from strategies import (
    by_name, by_age, by_diagnosis, by_years, by_age_then_name,
    is_adult, is_child, is_senior, is_treated, is_untreated,
    is_doctor, is_patient,
    make_age_filter,
    DischargeStrategy, IncrementAgeStrategy, AddPrefixToDiagnosis,
    extract_name, apply_discount
)

def print_separator(title):
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def main():
    print_separator("1. Создание пациентов и докторов")
    p1 = Patient("Иван Петров", 30, "ОРВИ")
    p2 = Patient("Анна Смирнова", 25, "Грипп", is_treated=True)
    p3 = Patient("Сергей Орлов", 12, "Грипп")
    p4 = Patient("Елена Васнецова", 68, "Гипертония", is_treated=False)
    p5 = Patient("Дмитрий Козлов", 45, "Диабет")
    d1 = Doctor("Елена Малышева", "Терапевт", 20)
    d2 = Doctor("Алексей Иванов", "Хирург", 15)

    registry = PatientCollection()
    for p in [p1, p2, p3, p4, p5]:
        registry.add(p)
    print("Создана коллекция пациентов:")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    #Сортировка тремя разными стратегиями
    print_separator("2. Сортировка тремя стратегиями (через метод sort_by)")

    # Стратегия 1: по имени
    registry.sort_by(by_name)
    print("Сортировка по имени:")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    # Стратегия 2: по возрасту
    registry.sort_by(by_age)
    print("\nСортировка по возрасту:")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    # Стратегия 3: по диагнозу, а затем по возраст
    registry.sort_by(by_diagnosis) 
    registry.sort_by(by_age_then_name)
    print("\nСортировка по (возраст, имя):")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    #Фильтрация двумя разными функциями-фильтрами
    print_separator("3. Фильтрация коллекции")

    adults = registry.filter_by(is_adult)
    print("Взрослые пациенты (>=18 лет):")
    for p in adults.get_all():
        print(f"  {p.to_string()}")

    treated = registry.filter_by(is_treated)
    print("\nВылеченные пациенты:")
    for p in treated.get_all():
        print(f"  {p.to_string()}")

    print_separator("4. Применение map (извлечение имён, применение скидки)")

    names = list(map(extract_name, registry.get_all()))
    print("Имена пациентов:", names)

    discounted = list(map(apply_discount, registry.get_all()))
    print("После применения map (скидка к диагнозу):")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    print_separator("5. Фабрика функций (make_age_filter)")

    age_filter_18_65 = make_age_filter(18, 65)
    middle_age_patients = registry.filter_by(age_filter_18_65)
    print("Пациенты в возрасте от 18 до 65 лет:")
    for p in middle_age_patients.get_all():
        print(f"  {p.to_string()}")

    print_separator("6. Паттерн Стратегия (callable-объекты)")

    # Стратегия выписки
    discharge_strategy = DischargeStrategy()
    registry.apply(discharge_strategy)
    print("После применения стратегии выписки (все вылечены):")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    # Стратегия увеличения возраста
    inc_age_strategy = IncrementAgeStrategy()
    registry.apply(inc_age_strategy)
    print("\nПосле увеличения возраста на 1:")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    prefix_strategy = AddPrefixToDiagnosis("[Обработан] ")
    registry.apply(prefix_strategy)
    print("\nПосле добавления префикса к диагнозу:")
    for p in registry.get_all():
        print(f"  {p.to_string()}")

    print_separator("7. Цепочка операций (filter_by -> sort_by -> apply)")

    # Создаём новую коллекцию
    fresh_registry = PatientCollection()
    fresh_registry.add(p1)
    fresh_registry.add(p2)
    fresh_registry.add(p3)
    fresh_registry.add(p4)
    fresh_registry.add(p5)

    result = (fresh_registry
              .filter_by(is_adult)
              .sort_by(by_age)
              .apply(IncrementAgeStrategy()))
    print("Результат цепочки (взрослые, отсортированы по возрасту, возраст увеличен на 1):")
    for p in result.get_all():
        print(f"  {p.to_string()}")

    print_separator("8. Три сценария работы")

    # Сценарий А: Полная цепочка filter -> sort -> apply с выводом на каждом шаге
    print("\nСценарий А: цепочка filter (невылеченные) -> sort (по возрасту) -> apply (выписка)")
    coll = PatientCollection()
    coll.add(p1)
    coll.add(p2)  # p2 уже вылечен
    coll.add(p4)  # p4 не вылечен
    print("Исходная коллекция:")
    for p in coll.get_all():
        print(f"  {p.to_string()}")
    step1 = coll.filter_by(is_untreated)
    print("После фильтрации (только невылеченные):")
    for p in step1.get_all():
        print(f"  {p.to_string()}")
    step2 = step1.sort_by(by_age)
    print("После сортировки по возрасту:")
    for p in step2.get_all():
        print(f"  {p.to_string()}")
    step3 = step2.apply(DischargeStrategy())
    print("После выписки:")
    for p in step3.get_all():
        print(f"  {p.to_string()}")

    # Сценарий Б: замена стратегии без изменения кода коллекции
    print("\nСценарий Б: замена стратегии сортировки (по имени -> по возрасту)")
    test_coll = PatientCollection()
    test_coll.add(p1)
    test_coll.add(p4)
    test_coll.add(p5)
    print("Исходный порядок (по добавлению):")
    for p in test_coll.get_all():
        print(f"  {p.to_string()}")
    test_coll.sort_by(by_name)
    print("После сортировки по имени:")
    for p in test_coll.get_all():
        print(f"  {p.to_string()}")
    test_coll.sort_by(by_age)
    print("После замены стратегии на сортировку по возрасту:")
    for p in test_coll.get_all():
        print(f"  {p.to_string()}")

    # Сценарий В: демонстрация callable-объекта как стратегии
    print("\nСценарий В: callable-объект (стратегия добавления префикса)")
    demo_coll = PatientCollection()
    demo_coll.add(p1)
    demo_coll.add(p5)
    print("До применения:")
    for p in demo_coll.get_all():
        print(f"  {p.to_string()}")
    strategy = AddPrefixToDiagnosis("ВИП-")
    demo_coll.apply(strategy)
    print("После применения стратегии:")
    for p in demo_coll.get_all():
        print(f"  {p.to_string()}")

    print_separator("9. Дополнительно: функции высшего порядка с разными типами")
    mixed_list = [p1, d1, p2, d2]
    print("Смешанный список (Patient и Doctor):")
    for obj in mixed_list:
        print(f"  {obj.to_string()}")

    # filter по типу
    doctors_only = list(filter(is_doctor, mixed_list))
    print("\nТолько доктора (filter + is_doctor):")
    for d in doctors_only:
        print(f"  {d.to_string()}")

    # sorted с ключом
    sorted_by_name = sorted(mixed_list, key=lambda x: x.name)
    print("\nСортировка смешанного списка по имени (lambda):")
    for obj in sorted_by_name:
        print(f"  {obj.to_string()}")

    # map с извлечением имён
    names = list(map(lambda x: x.name, mixed_list))
    print(f"\nИмена из смешанного списка (map + lambda): {names}")

if __name__ == "__main__":
    main()