class Patient:
    total_patients = 0
    MAX_AGE = 150

    @staticmethod
    def _validate_name(name):
        if not isinstance(name, str):
            raise TypeError("Имя должно быть строкой")
        if not name.strip():
            raise ValueError("Имя не может быть пустым")

    @staticmethod
    def _validate_age(age):
        if not isinstance(age, int):
            raise TypeError("Возраст должен быть целым числом")
        if age < 0 or age > Patient.MAX_AGE:
            raise ValueError(f"Возраст должен быть от 0 до {Patient.MAX_AGE}")

    @staticmethod
    def _validate_diagnosis(diagnosis):
        if not isinstance(diagnosis, str):
            raise TypeError("Диагноз должен быть строкой")
        if not diagnosis.strip():
            raise ValueError("Диагноз не может быть пустым")

    @staticmethod
    def _validate_is_treated(is_treated):
        if not isinstance(is_treated, bool):
            raise TypeError("Статус лечения должен быть булевым")

    def __init__(self, name, age, diagnosis, is_treated=False):
        self._validate_name(name)
        self._validate_age(age)
        self._validate_diagnosis(diagnosis)
        self._validate_is_treated(is_treated)

        self.__name = name
        self.__age = age
        self.__diagnosis = diagnosis
        self.__is_treated = is_treated

        Patient.total_patients += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self._validate_name(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self._validate_age(value)
        self.__age = value

    @property
    def diagnosis(self):
        return self.__diagnosis

    @diagnosis.setter
    def diagnosis(self, value):
        self._validate_diagnosis(value)
        self.__diagnosis = value

    @property
    def is_treated(self):
        return self.__is_treated

    @is_treated.setter
    def is_treated(self, value):
        self._validate_is_treated(value)
        self.__is_treated = value

    def admit(self):
        self.is_treated = False
        return f"Пациент {self.name} поступил на лечение."

    def discharge(self):
        self.is_treated = True
        return f"Пациент {self.name} выписан."

    def set_diagnosis(self, new_diagnosis):
        if self.is_treated:
            raise ValueError("Нельзя изменить диагноз вылеченному пациенту.")
        self._validate_diagnosis(new_diagnosis)
        self.__diagnosis = new_diagnosis
        return f"Диагноз пациента {self.name} изменён на '{new_diagnosis}'."

    def get_age_group(self):
        if self.age < 18:
            return "child"
        elif self.age < 65:
            return "adult"
        else:
            return "senior"

    def get_treatment_plan(self):
        return f"Общий план лечения для {self.name}: регулярный осмотр."

    def __str__(self):
        status = "лечится" if not self.is_treated else "вылечен"
        return (f"Пациент: {self.name}\n"
                f"Возраст: {self.age} ({self.get_age_group()})\n"
                f"Диагноз: {self.diagnosis}\n"
                f"Статус: {status}")

    def __repr__(self):
        return f"Patient(name='{self.name}', age={self.age}, diagnosis='{self.diagnosis}', is_treated={self.is_treated})"

    def __eq__(self, other):
        if not isinstance(other, Patient):
            return False
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)