from patient import Patient
from doctor import Doctor
from container import TypedCollection, Displayable, Scorable

def print_separator(title: str) -> None:
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)

def main() -> None:
    print_separator("1. Создание типизированной коллекции (TypedCollection[Patient])")
    registry = TypedCollection[Patient](Patient)  
    p1 = Patient("Иван Петров", 30, "ОРВИ")
    p2 = Patient("Анна Смирнова", 25, "Грипп")
    p3 = Patient("Сергей Орлов", 12, "Грипп")
    p4 = Patient("Елена Васнецова", 68, "Гипертония")
    for p in [p1, p2, p3, p4]:
        registry.add(p)
        print(f"Добавлен: {p.to_string()}")
    print(f"Всего пациентов: {len(registry)}")

    print_separator("2. Проверка валидации типов")
    try:
        registry.add("строка")
    except TypeError as e:
        print(f"Ошибка при добавлении: {e}")

    print_separator("3. Все элементы коллекции (через get_all)")
    for p in registry.get_all():
        print(p.to_string())

    print_separator("4. Поиск элемента find()")
    found = registry.find(lambda p: p.name == "Анна Смирнова")
    print(f"Найден пациент: {found.to_string() if found else 'None'}")
    not_found = registry.find(lambda p: p.name == "Неизвестный")
    print(f"Поиск неизвестного имени: {not_found}")

    print_separator("5. Фильтрация filter() – только взрослые")
    adults = registry.filter(lambda p: p.age >= 18)
    for p in adults:
        print(p.to_string())

    print_separator("6. Преобразование map() – извлечение имён и возрастов")
    names = registry.map(lambda p: p.name)
    ages = registry.map(lambda p: p.age)
    print(f"Имена (list[str]): {names}")
    print(f"Возраста (list[int]): {ages}")

    print_separator("7. Сценарий 1: TypedCollection[Displayable] (Patient и Doctor)")
    display_coll = TypedCollection[Displayable](
        object
    ) 
    display_coll = TypedCollection[Displayable](object)
    display_coll.add(p1)
    display_coll.add(p2)
    display_coll.add(Doctor("Елена Малышева", "Терапевт", 20))
    print("Вызов display() для каждого элемента (разные типы):")
    for item in display_coll.get_all():
        print(f"  {item.display()}")

    print_separator("8. Сценарий 2: TypedCollection[Scorable] (Patient и Doctor)")
    score_coll = TypedCollection[Scorable](object)
    score_coll.add(p1)
    score_coll.add(p2)
    score_coll.add(p3)
    score_coll.add(p4)
    score_coll.add(Doctor("Алексей Иванов", "Хирург", 15))
    print("Вызов score() для каждого элемента:")
    for item in score_coll.get_all():
        print(f"  {item.display()} -> score = {item.score()}")


if __name__ == "__main__":
    main()
