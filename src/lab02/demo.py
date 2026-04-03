from model import Patient
from collection import PatientCollection

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    print_separator("1. Создание пациентов")
    p1 = Patient("Иван Петров", 30, "ОРВИ")
    p2 = Patient("Мария Иванова", 25, "Ангина")
    p3 = Patient("Петр Сидоров", 70, "Гипертония", is_treated=False)
    p4 = Patient("Анна Климова", 45, "Диабет", is_treated=True)  # вылечена
    p5 = Patient("Сергей Орлов", 12, "Грипп")

    patients = [p1, p2, p3, p4, p5]
    for p in patients:
        print(p.name, p.age, p.diagnosis, "вылечен" if p.is_treated else "лечится")

    print_separator("2. Добавление в коллекцию")
    registry = PatientCollection()
    for p in patients:
        try:
            registry.add(p)
            print(f"Добавлен: {p.name}")
        except ValueError as e:
            print(f"Ошибка добавления {p.name}: {e}")

    print("\nПопытка добавить дубликат:")
    duplicate = Patient("Иван Петров", 31, "Грипп")
    try:
        registry.add(duplicate)
    except ValueError as e:
        print(f"Ошибка: {e}")

    print_separator("3. Вывод всех пациентов в коллекции")
    print(registry)

    print_separator("4. Поиск по атрибутам")
    print("Поиск по имени 'Мария Иванова':", registry.find_by_name("Мария Иванова"))
    print("Поиск по возрасту 70:", registry.find_by_age(70))
    print("Поиск по диагнозу 'Грипп':", registry.find_by_diagnosis("Грипп"))
    print("Поиск по статусу 'вылечен':", registry.find_by_status(True))

    print_separator("5. Длина коллекции и итерация")
    print(f"Количество пациентов: {len(registry)}")
    print("Перебор через for:")
    for patient in registry:
        print(f"  - {patient.name}, {patient.age} лет, {patient.diagnosis}")

    print_separator("6. Индексация")
    if len(registry) > 2:
        print(f"Первый пациент: {registry[0].name}")
        print(f"Третий пациент: {registry[2].name}")

    print_separator("7. Сортировка по имени")
    registry.sort_by_name()
    for p in registry:
        print(p.name)

    print("\nСортировка по возрасту (убывание)")
    registry.sort_by_age(reverse=True)
    for p in registry:
        print(f"{p.name}: {p.age}")

    print_separator("8. Фильтрация")
    treated = registry.get_treated()
    print("Вылеченные пациенты:")
    for p in treated:
        print(f"  {p.name}")

    untreated = registry.get_untreated()
    print("\nЛечащиеся пациенты:")
    for p in untreated:
        print(f"  {p.name}")

    seniors = registry.get_by_age_group("senior")
    print("\nПожилые пациенты (65+):")
    for p in seniors:
        print(f"  {p.name}, возраст {p.age}")

    print_separator("9. Удаление элемента")
    print("Удаляем пациента 'Петр Сидоров'")
    registry.remove(p3)
    print(f"После удаления осталось {len(registry)} пациентов:")
    for p in registry:
        print(p.name)

    print("\nУдаление по индексу (первого)")
    removed = registry.remove_at(0)
    print(f"Удалён: {removed.name}")
    print(f"Теперь в коллекции {len(registry)} пациентов:")
    for p in registry:
        print(p.name)

    print_separator("10. Три сценария работы")

    print("Сценарий А: Отобрать всех лечащихся пациентов старше 18 лет и отсортировать по возрасту")
    adults = registry.get_untreated()
    adult_list = [p for p in adults if p.age >= 18]
    adult_list.sort(key=lambda p: p.age)
    for p in adult_list:
        print(f"{p.name}, возраст {p.age}")

    print("\nСценарий Б: Найти пациентов с диагнозом 'ОРВИ' и выписать их")
    flu_patients = registry.find_by_diagnosis("ОРВИ")
    for p in flu_patients:
        if not p.is_treated:
            p.discharge()
            print(f"{p.name} выписан")

    print("\nСценарий В: Получить всех детей и взрослых")
    children = registry.get_by_age_group("child")
    adults_group = registry.get_by_age_group("adult")
    print(f"Детей: {len(children)}")
    for p in children:
        print(f"  {p.name} ({p.age})")
    print(f"Взрослых: {len(adults_group)}")
    for p in adults_group:
        print(f"  {p.name} ({p.age})")

if __name__ == "__main__":
    main()