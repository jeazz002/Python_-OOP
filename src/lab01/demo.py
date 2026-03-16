#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Демонстрационный скрипт для класса Patient.
Использует валидацию из отдельного модуля validators.
"""

from model import Patient

def print_separator(title):
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)

def main():
    # 1. Создание объекта и вывод
    print_separator("1. Создание объекта и вывод __str__")
    try:
        p1 = Patient("Иван Петров", 30, "ОРВИ")
        print(p1)
    except Exception as e:
        print(f"Ошибка: {e}")

    # 2. Сравнение объектов
    print_separator("2. Сравнение объектов (__eq__)")
    p2 = Patient("Мария Иванова", 25, "Ангина")
    p3 = Patient("Мария Иванова", 30, "Грипп")   
    p4 = Patient("Пётр Сидоров", 40, "Диабет")
    print(f"p2 == p3? {'Да' if p2 == p3 else 'Нет'}")  
    print(f"p2 == p4? {'Да' if p2 == p4 else 'Нет'}")  

    # 3. Некорректное создание
    print_separator("3. Некорректное создание (try/except)")
    test_cases = [
        ("", 25, "ОРВИ", "пустое имя"),
        ("Анна", -5, "Грипп", "отрицательный возраст"),
        ("Анна", 200, "Грипп", "возраст > MAX_AGE"),
        ("Анна", 30, "", "пустой диагноз"),
        ("Анна", 30, "Грипп", "не булев статус", "active"),
    ]
    for args in test_cases:
        try:
            if len(args) == 5:
                name, age, diag, desc, status = args
                p = Patient(name, age, diag, is_treated=status)
            else:
                name, age, diag, desc = args
                p = Patient(name, age, diag)
        except (TypeError, ValueError) as e:
            print(f"Ошибка ({desc}): {e}")

    # 4. Изменение свойства через setter
    print_separator("4. Изменение свойства через setter")
    try:
        p = Patient("Ольга", 28, "Аллергия")
        print("Исходный возраст:", p.age)
        p.age = 29
        print("После изменения:", p.age)
        p.age = -1
    except (TypeError, ValueError) as e:
        print(f"Ошибка при установке возраста: {e}")

    # 5. Доступ к атрибуту класса
    print_separator("5. Доступ к атрибуту класса")
    print(f"Patient.MAX_AGE = {Patient.MAX_AGE}")
    print(f"Patient.total_patients = {Patient.total_patients}")

    # 6. Бизнес-методы и состояние
    print_separator("6. Бизнес-методы и состояние")
    try:
        p = Patient("Сергей", 45, "Гипертония")
        print(p)
        print("\n>>> Меняем диагноз на 'Гипертония 2 степени'")
        print(p.set_diagnosis("Гипертония 2 степени"))
        print(p)
        print("\n>>> Выписываем пациента")
        print(p.discharge())
        print(p)
        print("\n>>> Пытаемся изменить диагноз после выписки")
        try:
            print(p.set_diagnosis("Хроническая гипертония"))
        except ValueError as e:
            print(f"Ошибка: {e}")
        print("\n>>> Пациент поступает снова")
        print(p.admit())
        print(p)
        print(f"Возрастная группа: {p.get_age_group()}")
    except Exception as e:
        print(f"Неожиданная ошибка: {e}")

    # 7. Три сценария работы
    print_separator("7. Три сценария работы")
    # Сценарий А
    print("Сценарий А: Стандартный цикл")
    a = Patient("Анна", 20, "Ангина")
    print(a)
    print(a.set_diagnosis("Тонзиллит"))
    print(a.discharge())
    print("Статус после выписки:", "вылечен" if a.is_treated else "лечится")

    # Сценарий Б
    print("\nСценарий Б: Ошибка при изменении диагноза после выписки")
    b = Patient("Борис", 60, "Диабет")
    print(b.discharge())
    try:
        b.set_diagnosis("Диабет 2 типа")
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")

    # Сценарий В
    print("\nСценарий В: Возрастная группа пожилого пациента")
    c = Patient("Клавдия", 72, "Артрит")
    print(c)
    print(f"Возрастная группа: {c.get_age_group()}")
    print(c.admit())
    print("После повторного поступления:", "лечится" if not c.is_treated else "вылечен")

if __name__ == "__main__":
    main()