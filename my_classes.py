from datetime import datetime

class Person():
    def __init__(self, name):
        self.name = name
        

class Subject(Person):
    def __init__(self, name, last, sex, dateofbirth):
        super().__init__(name)
        self.first_name = name
        self.last = last
        self.sex = sex
        self.dateofbirth = datetime.strptime(dateofbirth, "%Y-%m-%d")
        

    def get_age(self):
        age = datetime.today().year - self.dateofbirth.year
        return age
        

    def estimate_max_hr(self):
        """A function that estimates the maximum heart rate of a subject"""
        age = self.get_age()
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
        

    def __str__(self):
        max_hr = self.estimate_max_hr()
        return f"{self.first_name} {self.last} ({self.sex}, {self.get_age()} y, {max_hr} bpm)"
        

class Supervisor():
    def __init__(self, first_name, last_name):
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name
        

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        

class Experiment():

    def __init__(self, name, date):
        self.name = name
        self.date = date
        

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor
        

    def __str__(self):
        return (f'Experiment "{self.name}" vom {self.date} mit:\n'
                f'Subject: {self.subject}\n'
                f'Supervisor: {self.supervisor}')
        