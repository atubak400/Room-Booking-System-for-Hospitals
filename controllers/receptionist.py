from controllers.appointment import Appointment

class Receptionist:
    def __init__(self, name):
        self.name = name

    def schedule_appointment(self, patient, medical_staff, date, status="Scheduled"):
        # Schedule an appointment for a patient
        appointment = Appointment(appointment_id=Appointment.generate_appointment_id(), patient=patient, medical_staff=medical_staff, date=date, status=status)
        return appointment

    def check_in_patient(self, patient, appointment):
        # Perform patient check-in for a scheduled appointment
        if appointment.status == "Scheduled":
            appointment.status = "Checked-In"
            print(f"Patient {patient} checked in for the appointment.")
        else:
            print("Patient cannot check in. Appointment status is not 'Scheduled'.")
    
    def check_out_patient(self, patient, appointment):
        # Perform patient check-out for a checked-in appointment
        if appointment.status == "Checked-In":
            appointment.status = "Completed"
            print(f"Patient {patient} checked out after the appointment.")
        else:
            print("Patient cannot check out. Appointment status is not 'Checked-In'.")
    
    def cancel_appointment(self, appointment):
        # Cancel an appointment
        if appointment.status == "Scheduled":
            appointment.status = "Cancelled"
            print(f"Appointment {appointment.appointment_id} has been cancelled.")
        else:
            print("Appointment cannot be cancelled. Status is not 'Scheduled.")


    def reschedule_appointment(self, appointment, new_date):
        # Reschedule an existing appointment to a new date
        appointment.schedule_appointment(new_date)
        print(f"Appointment {appointment.appointment_id} rescheduled to {new_date}.")





