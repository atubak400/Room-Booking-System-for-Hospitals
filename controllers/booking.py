import csv
import os

class Booking:
    def __init__(self, filepath):
        self.filepath = filepath

    def _read_bookings(self):
        if not os.path.exists(self.filepath):
            return []
        with open(self.filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            return list(reader)

    def _write_bookings(self, bookings):
        with open(self.filepath, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(bookings)

    def book_room(self, patient_name, room, date):
        bookings = self._read_bookings()
        for booking in bookings:
            if booking[0] == str(room) and booking[1] == date:
                print("Room is already booked for that date.")
                return False

        bookings.append([patient_name, room, date])
        self._write_bookings(bookings)
        print(f"Room {room} has been booked successfully.")
        return True

    def cancel_booking(self, room, date):
        bookings = self._read_bookings()
        new_bookings = [booking for booking in bookings if not (booking[0] == str(room) and booking[1] == date)]

        if len(bookings) == len(new_bookings):
            print("No booking found for the specified date.")
            return False

        self._write_bookings(new_bookings)
        print("Room booking cancelled.")
        return True

    def check_availability(self, room, date):
        bookings = self._read_bookings()
        return not any(booking[0] == str(room) and booking[1] == date for booking in bookings)
