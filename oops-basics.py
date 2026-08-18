"""class Patient:
    def __init__(self, name, age, diagnose):
        self.name = name
        self.age = age
        self.diagnose = diagnose
    def display(self):
        print(f"{self.name} is {self.age} years old and has been diagnosed with {self.diagnose}")
class CancerPatient(Patient):
    def __init__(self, name, age, diagnose, stage):
        super().__init__(name, age, diagnose)
        self.stage = stage
    def display(self):
        print(f"{self.name} is {self.age} years old and has been diagnosed with {self.diagnose} and stage is {self.stage}")
#Patient1=Patient("Ali", 45, "Flu")  
#Patient2=CancerPatient("Sara", 30, "Diabetes", "stage2")
#Patient3=Patient("John", 60, "Hypertension")  
#Patient1.display()
#Patient2.display()p
#Patient3.display()
Patients=[Patient("Ali",45,"Flu"),CancerPatient("Sara",30, "Lymphoma","Stage 2")]
for Patient in Patients:
    Patient.display()"""
"""class Patient:
    def __init__(self, name, age, diagnose):
        self.__name=name
        self.__age=age
        self.__diagnose=diagnose
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_diagnose(self):
        return self.__diagnose
Patient1=Patient("Ali", 45, "Flu")
"""
"""print(Patient1.get_name())
print(Patient1.get_age())  
print (Patient1.get_diagnose())"""
#print(Patient1.__name)
from abc import ABC, abstractmethod
class Hospital(ABC):
    @abstractmethod
    def treat_patient(self):
        pass
class LymphomaCenter(Hospital):
    def treat_patient(self):
        print("Administering lymphoma center treatment")
center=LymphomaCenter() 
center.treat_patient()       
h=Hospital()