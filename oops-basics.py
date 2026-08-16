class Patient:
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
        print(f"{self.name}is{self.age}years old has been diagnosed with{self.diagnose} and stage is {self.stage}")   
Patient1=Patient("Ali", 45, "Flu")  
Patient2=CancerPatient("Sara", 30, "Diabetes", "stage2")
#Patient3=Patient("John", 60, "Hypertension")  
Patient1.display()
Patient2.display()
#Patient3.display()

