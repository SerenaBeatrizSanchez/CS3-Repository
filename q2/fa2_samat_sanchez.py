#Parent class
class Patient:
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount
    #getter and setter methods for name
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    #getter and setter methods for bill amount
    def get_bill_amount(self):
        return self.__ill_amount
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
    #calculation
    def calculate_bill(self):
        return self._bill_amount*1
    #display information
    def display_info(self):
        print("Patient Name: ",self._name)
        print("Original Bill: ₱",self._bill_amount)
        print("Final Bill: ₱",self.calculate_bill())

#Child class no. 1
class Senior_Patient(Patient):
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount
    #getter and setter methods for name
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    #getter and setter methods for bill amount
    def get_bill_amount(self):
        return self._bill_amount
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
    #calculation
    def calculate_bill(self):
        return self._bill_amount*0.80
    #display information
    def display_info(self):
        super().display_info()

#Child class no. 2
class PhilHealth_Patient(Patient):
    def __init__(self, name, bill_amount):
        self._name = name
        self._bill_amount = bill_amount
    #getter and setter methods for name
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    #getter and setter methods for bill amount
    def get_bill_amount(self):
        return self.__bill_amount
    def set_bill_amount(self, bill_amount):
        self._bill_amount = bill_amount
    #calculation
    def calculate_bill(self):
        return self._bill_amount*0.85
    #display information
    def display_info(self):
        super().display_info()

regular_patient = Patient("Juan Dela Cruz", 15000)
sen_patient = Senior_Patient("Maria Santos", 15000)
ph_patient = PhilHealth_Patient("Pedro Reyes", 15000)

print("Hospital Billing System")
print("-----------------------")
regular_patient.display_info()
print("")
sen_patient.display_info()
print("")
ph_patient.display_info()
