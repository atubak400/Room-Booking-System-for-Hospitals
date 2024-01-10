import csv
from datetime import datetime

class Appointment:
    filepath = "appointments.csv"  # Path to the appointments CSV file

    def __init__(self, patient, medical_staff, date, status="Scheduled"):
        self.appointment_id = self.get_next_appointment_id()
        self.patient = patient
        self.medical_staff = medical_staff
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.status = status

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Patient: {self.patient}, Medical Staff: {self.medical_staff}, Date: {self.date.strftime('%Y-%m-%d')}, Status: {self.status}"
    
    @classmethod
    def cancel_appointment_by_id(cls, appointment_id):
        appointments = cls.load_from_csv()
        updated_appointments = []
        for appointment in appointments:
            if appointment.appointment_id == appointment_id:
                appointment.status = "Cancelled"
            updated_appointments.append(appointment)
        cls.write_to_csv(updated_appointments)
        print(f"Appointment with ID {appointment_id} has been cancelled.")

    @classmethod
    def update_status_by_id(cls, appointment_id, new_status):
        valid_statuses = ["Scheduled", "Completed", "Cancelled", "No Show"]
        if new_status not in valid_statuses:
            print(f"Invalid status. Status must be one of: {valid_statuses}")
            return

        appointments = cls.load_from_csv()
        updated_appointments = []
        for appointment in appointments:
            if appointment.appointment_id == appointment_id:
                appointment.status = new_status
            updated_appointments.append(appointment)
        cls.write_to_csv(updated_appointments)
        print(f"Appointment with ID {appointment_id} has been {new_status}.")

    @classmethod
    def write_to_csv(cls, appointments):
        with open(cls.filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            for appointment in appointments:
                writer.writerow([appointment.appointment_id, appointment.patient, appointment.medical_staff, appointment.date.strftime('%Y-%m-%d'), appointment.status])

    @classmethod
    def get_next_appointment_id(cls):
        try:
            with open(cls.filepath, mode='r', newline='') as file:
                reader = csv.reader(file)
                existing_ids = [int(row[0]) for row in reader if row and row[0].isdigit()]
                return max(existing_ids) + 1 if existing_ids else 1
        except FileNotFoundError:
            return 1

    def schedule_appointment(self):
        with open(self.filepath, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.appointment_id, self.patient, self.medical_staff, self.date.strftime('%Y-%m-%d'), self.status])

    @classmethod
    def load_from_csv(cls):
        appointments = []
        with open(cls.filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    appointment = cls(patient=row[1], medical_staff=row[2], date=row[3], status=row[4])
                    appointment.appointment_id = int(row[0]) 
                    appointments.append(appointment)
        return appointments

    @classmethod
    def view_all_appointments(cls):
        appointments = cls.load_from_csv()
        for appointment in appointments:
            print(appointment)


