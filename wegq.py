import datetime
from abc import ABC, abstractmethod
from typing import List, Dict


class Patient:
    VALID_BLOOD_TYPES = ('О', 'А', 'В', 'АВ')  

    def __init__(self, full_name: str, age: int, blood_type: str):
        if not full_name or not isinstance(full_name, str):
            raise ValueError('имя')
        if not isinstance(age, int) or age < 0 or age > 150:
            raise ValueError('возраст')
        if blood_type not in self.VALID_BLOOD_TYPES:
            raise ValueError('группа крови')
        self._full_name = full_name
        self._age = age
        self._blood_type = blood_type
        self._diagnoses = []
        self._allergies = []

    @property
    def full_name(self):
        return self._full_name

    @property
    def age(self):
        return self._age

    @property
    def blood_type(self):
        return self._blood_type

    def is_minor(self) -> bool:
        return self._age < 18

    def add_diagnosis(self, diagnosis: str):
        if diagnosis:
            self._diagnoses.append(diagnosis)

    def add_allergy(self, allergy: str):
        if allergy:
            self._allergies.append(allergy)

    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return self._full_name == other._full_name and self._age == other._age



class Appointment:
    def __init__(self, patient: Patient, doctor_name: str, specialty: str,
                 services: List[str], date: datetime.date, is_emergency: bool = False):
        self.patient = patient
        self.doctor_name = doctor_name
        self.specialty = specialty
        self.services = services
        self.date = date
        self.is_emergency = is_emergency

    def __str__(self):
        services_str = ", ".join(self.services)
        emergency_str = " (срочно)" if self.is_emergency else ""
        return (f"Приём: {self.patient.full_name} → {self.doctor_name} ({self.specialty}), "
                f"{self.date}, услуги: [{services_str}]{emergency_str}")



class AppointmentBuilder:
    def __init__(self):
        self._patient = None
        self._doctor_name = None
        self._specialty = None
        self._services = []
        self._date = None
        self._is_emergency = False

    def for_patient(self, patient: Patient):
        self._patient = patient
        return self

    def with_doctor(self, doctor_name: str, specialty: str):
        self._doctor_name = doctor_name
        self._specialty = specialty
        return self

    def add_service(self, service_name: str):
        self._services.append(service_name)
        return self

    def on_date(self, date: datetime.date):
        if date < datetime.date.today():
            raise ValueError("Дата не может быть в прошлом")
        self._date = date
        return self

    def as_emergency(self):
        self._is_emergency = True
        return self

    def build(self) -> Appointment:
        if self._patient is None:
            raise ValueError("Не указан пациент")
        if self._doctor_name is None or self._specialty is None:
            raise ValueError("Не указан врач")
        if self._date is None:
            raise ValueError("Не указана дата")
        return Appointment(
            patient=self._patient,
            doctor_name=self._doctor_name,
            specialty=self._specialty,
            services=self._services.copy(),
            date=self._date,
            is_emergency=self._is_emergency
        )



class PricingStrategy(ABC):
    @abstractmethod
    def calculate(self, appointment: Appointment) -> float:
        pass


class FlatPricing(PricingStrategy):
    def __init__(self, price_per_service: float):
        self.price_per_service = price_per_service

    def calculate(self, appointment: Appointment) -> float:
        return self.price_per_service * len(appointment.services)


class SpecialtyPricing(PricingStrategy):
    def __init__(self, prices: Dict[str, float]):
        self.prices = prices

    def calculate(self, appointment: Appointment) -> float:
        price_per_service = self.prices[appointment.specialty]
        return price_per_service * len(appointment.services)


class EmergencyPricing(PricingStrategy):
    def __init__(self, base_strategy: PricingStrategy, multiplier: float):
        self.base_strategy = base_strategy
        self.multiplier = multiplier

    def calculate(self, appointment: Appointment) -> float:
        base_cost = self.base_strategy.calculate(appointment)
        if appointment.is_emergency:
            return base_cost * self.multiplier
        return base_cost


class MinorDiscountPricing(PricingStrategy):
    def __init__(self, base_strategy: PricingStrategy, discount_percent: float):
        self.base_strategy = base_strategy
        self.discount_percent = discount_percent

    def calculate(self, appointment: Appointment) -> float:
        base_cost = self.base_strategy.calculate(appointment)
        if appointment.patient.is_minor():
            return base_cost * (100 - self.discount_percent) / 100.0
        return base_cost



class Clinic:
    def __init__(self):
        self._appointments = []
        self._pricing_strategy = None

    def add_appointment(self, appointment: Appointment):
        self._appointments.append(appointment)

    def set_pricing(self, strategy: PricingStrategy):
        self._pricing_strategy = strategy

    def total_revenue(self) -> float:
        if self._pricing_strategy is None:
            return 0.0
        total = 0.0
        for app in self._appointments:
            total += self._pricing_strategy.calculate(app)
        return total

    def appointments_for(self, patient: Patient) -> List[Appointment]:
        return [app for app in self._appointments if app.patient == patient]



if __name__ == "__main__":
    from datetime import date

    kid = Patient('Иванов Ваня', 10, 'О')    
    adult = Patient('Петров П.П.', 40, 'А')  

    app1 = (AppointmentBuilder()
        .for_patient(adult)
        .with_doctor('Сидорова А.С.', 'терапевт')
        .add_service('осмотр').add_service('анализы')
        .on_date(date(2026, 6, 1))   
        .build())

    app2 = (AppointmentBuilder()
        .for_patient(kid)
        .with_doctor('Иванова О.П.', 'педиатр')
        .add_service('осмотр')
        .on_date(date(2026, 6, 2))  
        .as_emergency()
        .build())

    clinic = Clinic()
    clinic.add_appointment(app1)
    clinic.add_appointment(app2)

    clinic.set_pricing(FlatPricing(1500))
    print(clinic.total_revenue())    

    clinic.set_pricing(SpecialtyPricing({'терапевт': 1500, 'педиатр': 2000}))
    print(clinic.total_revenue())    

    clinic.set_pricing(EmergencyPricing(FlatPricing(1500), multiplier=2))
    print(clinic.total_revenue())    

    clinic.set_pricing(MinorDiscountPricing(FlatPricing(1500), discount_percent=30))
    print(clinic.total_revenue())    

    try:
        (AppointmentBuilder().with_doctor('Х', 'Х').build())
    except ValueError as e:
        print(e)   