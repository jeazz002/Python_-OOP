from base import Patient

class Inpatient(Patient):
    """Стационарный пациент (лежит в больнице)."""
    def __init__(self, name, age, diagnosis, ward_number, admission_date, is_treated=False):
        super().__init__(name, age, diagnosis, is_treated)
        self.ward_number = ward_number          # новый атрибут
        self.admission_date = admission_date    # новый атрибут

    def discharge_planned_date(self, days=7):
        return f"Плановая выписка: через {days} дней от {self.admission_date}"

    def get_treatment_plan(self):
        return (f"Стационарное лечение для {self.name}: палата {self.ward_number}, "
                f"ежедневный осмотр, выписка ориентировочно через 7 дней.")

    def __str__(self):
        base_str = super().__str__()
        return (base_str + f"\nТип: стационарный\n"
                f"Палата: {self.ward_number}\n"
                f"Дата поступления: {self.admission_date}")

class Outpatient(Patient):
    """Амбулаторный пациент (посещает поликлинику)."""
    def __init__(self, name, age, diagnosis, next_appointment, clinic_address, is_treated=False):
        super().__init__(name, age, diagnosis, is_treated)
        self.next_appointment = next_appointment   # новый атрибут
        self.clinic_address = clinic_address       # новый атрибут

    def reminder(self):
        return f"Напоминание: {self.name}, ваш следующий приём {self.next_appointment} в {self.clinic_address}."

    def get_treatment_plan(self):
        return (f"Амбулаторное лечение для {self.name}: приходите на приём {self.next_appointment}, "
                f"следуйте рекомендациям.")

    def __str__(self):
        base_str = super().__str__()
        return (base_str + f"\nТип: амбулаторный\n"
                f"Следующий приём: {self.next_appointment}\n"
                f"Адрес клиники: {self.clinic_address}")