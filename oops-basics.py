class Patient:
    def __init__(self, name, age, diagnose):
        self.name = name
        self.age = age
        self.diagnose = diagnose
    def display(self):
        print(f"{self.name} is {self.age} years old and has been diagnosed with {self.diagnose}")
Patient1=Patient("Ali", 45, "Flu")  
Patient2=Patient("Sara", 30, "Diabetes")
Patient3=Patient("John", 60, "Hypertension")  
Patient1.display()
Patient2.display()
Patient3.display()

