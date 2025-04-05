class Subject():
    def __init__(self, first_name, last, sex, age):
        self.first_name = first_name
        self.last = last
        self.sex = sex
        self.age = age
        pass

    def estimate_max_hr(self):
        """A function that estimates the maximum heart rate of a subject"""
        if self.sex == "male":
            max_hr_bpm =  223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 *  self.age
        else:
            # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm  = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
        pass

    def __str__(self):
        max_hr = self.estimate_max_hr()
        return f"{self.first_name} {self.last} ({self.sex}, {self.age} y, {max_hr} bpm)"
        pass

class Supervisor():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        pass

class Experiment():

    def __init__(self, name, date):
        self.name = name
        self.date = date
        pass

    def add_subject(self, subject):
        self.subject = subject

    def add_supervisor(self, supervisor):
        self.supervisor = supervisor
        pass

    def __str__(self):
        return (f'Experiment "{self.name}" vom {self.date} mit:\n'
                f'Subject: {self.subject}\n'
                f'Supervisor: {self.supervisor}')
        pass