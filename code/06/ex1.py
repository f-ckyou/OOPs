class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Doctor(Person):
    def diagnose(self, patient):
        print(f"Dr. {self.name} diagnosed {patient.name}")

class Patient(Person):
    def book_appointment(self, doctor):
        print(f"{self.name} booked an appointment with Dr. {doctor.name}")


doctor = Doctor("Zoro", 19)
patient = Patient("xyz", 30)

patient.book_appointment(doctor) 
doctor.diagnose(patient)