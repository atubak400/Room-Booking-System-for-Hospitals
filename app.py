from controllers.patient import Patient
from controllers.room import Room
from controllers.invoice import Invoice
from controllers.authentication import Authentication
from controllers.receptionist import Receptionist
from controllers.appointment import Appointment
from controllers.booking import Booking
from controllers.hospital import Hospital
import csv


# Create hospital
hospital = Hospital(name="University of Derby Hospital", address="One Friar Gate Square Agard Street DE11DZ", contact_info="hospital@derby.ac.uk")

def check_available_rooms():
    # List available rooms in the hospital
    available_rooms = hospital.list_available_rooms()
    print(f"Available Rooms at {hospital.name}:")
    for room in available_rooms:
        print(f"Room {room.room_id}: {room.room_type} room with a capacity of {room.capacity} for £{room.price} is {room.status}")

# Create 20 available rooms and add them to the hospital
for room_id in range(1, 21):
    if room_id <= 15:
        room = Room(room_id=room_id, room_type="Standard", capacity=2, price=80)
        room.update_status("Available")
    else:
        room = Room(room_id=room_id, room_type="ICU", capacity=1, price=160)
        room.update_status("Available")
    hospital.add_room(room)

def manage_appointments():
    while True:
        print("\nAppointment Management:")
        print("1: Schedule an appointment")
        print("2: Update an appointment")
        print("3: Cancel an appointment")
        print("4: View all appointments")
        print("0: Return to the main menu")
        choice = input("Enter your choice (1/2/3/4/0): ")

        if choice == "1":
            patient = input("Enter patient name: ")
            medical_staff = input("Enter medical staff name: ")
            date = input("Enter appointment date (YYYY-MM-DD): ")
            new_appointment = Appointment(patient, medical_staff, date)
            new_appointment.schedule_appointment()
            print("Appointment scheduled successfully.")
            
        elif choice == "2":
            appointment_id = int(input("Enter appointment ID to update: "))
            new_status = input("Enter new status (Scheduled/Completed/Cancelled/No Show): ")
            Appointment.update_status_by_id(appointment_id, new_status)
            print(f"Appointment ID {appointment_id} updated to {new_status}.")

        elif choice == "3":
            appointment_id = int(input("Enter appointment ID to cancel: "))
            Appointment.cancel_appointment_by_id(appointment_id)
            print(f"Appointment ID {appointment_id} cancelled.")

        elif choice == "4":
            Appointment.view_all_appointments()

        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_booking():
    file_path = "./booking.csv"
    booking = Booking(file_path)
    
    while True:
        print("\nBooking Management:")
        print("1: Book a room")
        print("2: Cancel a room booking")
        print("3: Check room availability")
        print("0: Return to the main menu")
        choice = input("Enter your choice (1/2/3/4/0): ")

        if choice == "1":
            patient_name = input("Enter your name: ")
            room_id = input("Enter room number: ")
            date = input("Enter booking date (YYYY-MM-DD): ")
            room = hospital.get_room_by_id(room_id)            

            if room and room.status == "Available":
                booking.book_room(patient_name, room_id, date)
                room.update_status("Occupied")
                # print("Room booked successfully.")
            else:
                print("Room not available.")  

        elif choice == "2":
            room_id = input("Enter room number: ")
            date = input("Enter booking date (YYYY-MM-DD) to cancel: ")
            room = hospital.get_room_by_id(room_id)

            if room:
                if booking.cancel_booking(room_id, date):
                    room.update_status("Available")
                else:
                    print("Room booking could not be found or was not cancelled.")
            else:
                print("Room not found.")

        elif choice == "3":
            check_available_rooms()
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

def manage_invoices():
    name = input("Enter your name: ")
    
    # Read the bookings from the CSV file
    file_path = "./booking.csv"
    with open(file_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        bookings = list(reader)

    # Find the latest booking for the given name
    latest_booking = None
    for booking in reversed(bookings):
        if booking[0] == name:
            latest_booking = booking
            break

    if latest_booking:
        room_id = int(latest_booking[1])
        date = latest_booking[2]
        room_price = hospital.get_room_price_by_id(room_id)

        if room_price is not None:
            invoice = Invoice(room_id, room_price, name, date)
            invoice.generate_invoice()
            invoice.request_payment()
            invoice.print_receipt()
        else:
            print(f"No room found with the ID {room_id}.")
    else:
        print(f"No booking found for {name}.")

def main():
    auth = Authentication(filepath="users.csv")

    while True:
        action = input("Do you want to 'login' or 'register'? ")
        if action == 'register':
            username = input("Choose a username: ")
            password = input("Choose a password: ")
            role = input("Are you a 'patient' or 'receptionist'? ")
            auth.register_user(username, password, role)
        elif action == 'login':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if auth.login_user(username, password):
                print(f"Welcome to the {hospital.name} Room Booking System!")

                while True:  # This loop will keep the menu prompt active.
                    print("\nPlease select an action:")
                    print("1: Check available rooms")
                    print("2: Book a room")
                    print("3: Make Payments")
                    print("4: Manage appointments")
                    print("0: Log out")
                    user_choice = input("Enter your choice (1/2/3/4/0): ")

                    if user_choice == "1":
                        check_available_rooms()
                    elif user_choice == "2":
                        manage_booking()
                    elif user_choice == "3":
                        manage_invoices()
                    elif user_choice == "4":
                        manage_appointments()
                    elif user_choice == "0":
                        print("Logging out...")
                        break  # This will exit the inner while loop
                    else:
                        print("Invalid choice. Please try again.")

                break  # This will exit the outer while loop after logging out
            else:
                print("Invalid username or password. Please try again.")
        else:
            print("Invalid input. Please type 'login' or 'register'.")

if __name__ == "__main__":
    main()