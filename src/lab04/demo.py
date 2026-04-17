import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab01'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'lab02'))

from model import Patient
from collection import PatientCollection
from models import Doctor
from interfaces import Printable, Comparable

def print_all(items: list[Printable]):
    for item in items:
        print(item.to_string())

def sort_comparable(items: list[Comparable]):
    n = len(items)
    for i in range(n):
        for j in range(0, n - i - 1):
            if items[j].compare_to(items[j+1]) > 0:
                items[j], items[j+1] = items[j+1], items[j]
    return items

def main():
    p1 = Patient("Иван Петров", 30, "ОРВИ")
    p2 = Patient("Анна Смирнова", 25, "Грипп", is_treated=True)
    p3 = Patient("Сергей Орлов", 12, "Грипп")
    d1 = Doctor("Елена Малышева", "Терапевт", 20)
    d2 = Doctor("Алексей Иванов", "Хирург", 15)

    mixed_list = [p1, d1, p2, d2, p3]

    # 1. Printable
    print("=== 1. Все объекты (Printable) ===")
    print_all(mixed_list)

    # 2. Сортировка через Comparable (раздельно)
    print("\n=== 2. Сортировка через Comparable ===")
    patients = [p1, p2, p3]
    print("Пациенты до сортировки:")
    for p in patients:
        print(f"  {p.to_string()}")
    sort_comparable(patients)
    print("Пациенты после сортировки (по возрасту):")
    for p in patients:
        print(f"  {p.to_string()}")

    doctors = [d1, d2]
    print("\nДоктора до сортировки:")
    for d in doctors:
        print(f"  {d.to_string()}")
    sort_comparable(doctors)
    print("Доктора после сортировки (по стажу):")
    for d in doctors:
        print(f"  {d.to_string()}")

    # 3. isinstance и множественная реализация
    print("\n=== 3. Проверка isinstance ===")
    for obj in mixed_list:
        print(f"{obj.to_string()}:")
        if isinstance(obj, Printable):
            print("  - является Printable")
        if isinstance(obj, Comparable):
            print("  - является Comparable")
        print("  ---")

    # 4. Работа с коллекцией PatientCollection
    print("\n=== 4. Работа с PatientCollection ===")
    registry = PatientCollection()          # <-- здесь создаётся registry
    registry.add(p1)
    registry.add(p2)
    registry.add(p3)

    print("Все пациенты в коллекции:")
    for p in registry.get_all():
        print(p.to_string())

    printable_in_collection = [p for p in registry.get_all() if isinstance(p, Printable)]
    print("\nПациенты, реализующие Printable (все):")
    for p in printable_in_collection:
        print(p.to_string())

    # 5. Три сценария
    print("\n=== 5. Три сценария работы ===")
    # Сценарий А
    print("\nСценарий А: Только Printable из mixed_list")
    only_printable = [obj for obj in mixed_list if isinstance(obj, Printable)]
    for obj in only_printable:
        print(obj.to_string())

    # Сценарий Б
    print("\nСценарий Б: Вызов print_all для докторов")
    print_all([d1, d2])

    # Сценарий В
    print("\nСценарий В: Все Comparable, сортировка раздельно")
    all_comp = [obj for obj in mixed_list if isinstance(obj, Comparable)]
    pats = [obj for obj in all_comp if isinstance(obj, Patient)]
    docs = [obj for obj in all_comp if isinstance(obj, Doctor)]
    sort_comparable(pats)
    sort_comparable(docs)
    print("Отсортированные пациенты:")
    for p in pats:
        print(f"  {p.to_string()}")
    print("Отсортированные доктора:")
    for d in docs:
        print(f"  {d.to_string()}")

if __name__ == "__main__":
    main()