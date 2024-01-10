from datetime import datetime

class Patient:
    def __init__(self, patient_id, name, dob, email, phone_number):
        self.patient_id = patient_id
        self.name = name
        self.dob = datetime.strptime(dob, '%Y-%m-%d')
        self.email = email
        self.phone_number = phone_number
        self.appointments = []

    def view_appointments(self):
        return self.appointments