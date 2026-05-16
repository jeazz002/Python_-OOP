from typing import NoReturn
from app import PatientApp
from exceptions import DuplicateItemError, ItemNotFoundError, InvalidDataError

def print_table(patients: list) -> None:
    if not patients:
        print("Нет пациентов.")
        return
    print("\n" + "-" * 80)
    print(f"{'Имя':<20} {'Возраст':<8} {'Диагноз':<25} {'Статус':<15}")
    print("-" * 80)
    for p in patients:
        status = "Вылечен" if p.is_treated else "Лечится"
        print(f"{p.name:<20} {p.age:<8} {p.diagnosis:<25} {status:<15}")
    print("-" * 80 + "\n")

def get_int_input(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число.")

def get_yes_no(prompt: str) -> bool:
    while True:
        answer = input(prompt).strip().lower()
        if answer in ('y', 'yes', 'д', 'да'):
            return True
        if answer in ('n', 'no', 'н', 'нет'):
            return False
        print("Пожалуйста, ответьте y/n (да/нет).")

def run_cli() -> NoReturn:
    app = PatientApp()
    print("Добро пожаловать в систему управления пациентами!")
    while True:
        print("\n=== МЕНЮ ===")
        print("1. Добавить пациента")
        print("2. Показать всех пациентов")
        print("3. Найти пациента по имени")
        print("4. Фильтровать по диагнозу")
        print("5. Сортировать пациентов")
        print("6. Удалить пациента по имени")
        print("7. Сохранить и выйти")

        choice = input("Выберите пункт: ").strip()
        if choice == '1':
            try:
                name = input("Имя: ").strip()
                if not name:
                    raise InvalidDataError("Имя не может быть пустым.")
                age = get_int_input("Возраст: ")
                if age < 0 or age > 150:
                    raise InvalidDataError("Возраст должен быть от 0 до 150.")
                diagnosis = input("Диагноз: ").strip()
                if not diagnosis:
                    raise InvalidDataError("Диагноз не может быть пустым.")
                is_treated = get_yes_no("Пациент уже вылечен? (y/n): ")
                app.add_patient(name, age, diagnosis, is_treated)
                print(f"Пациент '{name}' успешно добавлен.")
            except (DuplicateItemError, InvalidDataError) as e:
                print(f"Ошибка: {e}")
            except Exception as e:
                print(f"Непредвиденная ошибка: {e}")

        elif choice == '2':
            patients = app.get_all_patients()
            print_table(patients)

        elif choice == '3':
            name = input("Введите имя пациента для поиска: ").strip()
            patient = app.find_patient_by_name(name)
            if patient:
                print("\nНайден пациент:")
                print_table([patient])
            else:
                print(f"Пациент с именем '{name}' не найден.")

        elif choice == '4':
            diagnosis = input("Введите диагноз для фильтрации: ").strip()
            filtered = app.filter_by_diagnosis(diagnosis)
            print(f"\nПациенты с диагнозом '{diagnosis}':")
            print_table(filtered)

        elif choice == '5':
            print("\nСортировать по:")
            print("1. Имени")
            print("2. Возрасту")
            print("3. Диагнозу")
            sub = input("Выберите критерий: ").strip()
            reverse = get_yes_no("По убыванию? (y/n): ")
            key_map = {'1': 'name', '2': 'age', '3': 'diagnosis'}
            if sub not in key_map:
                print("Неверный выбор.")
                continue
            try:
                app.sort_patients(key_map[sub], reverse)
                print("Сортировка выполнена. Показываю обновлённый список:")
                print_table(app.get_all_patients())
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == '6':
            name = input("Введите имя пациента для удаления: ").strip()
            patient = app.find_patient_by_name(name)
            if not patient:
                print(f"Пациент '{name}' не найден.")
                continue
            print_table([patient])
            if get_yes_no(f"Удалить пациента '{name}'? (y/n): "):
                try:
                    app.remove_patient_by_name(name)
                    print(f"Пациент '{name}' удалён.")
                except ItemNotFoundError as e:
                    print(f"Ошибка: {e}")

        elif choice == '7':
            app.save_to_file()
            print("Данные сохранены. До свидания!")
            break
        else:
            print("Неверный пункт меню. Введите число от 1 до 7.")