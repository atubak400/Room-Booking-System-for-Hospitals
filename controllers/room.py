class Room:
    def __init__(self, room_id, room_type, capacity, price, status="Available"):
        self.room_id = room_id
        self.room_type = room_type
        self.capacity = capacity
        self.status = status
        self.price = price

    def __str__(self):
        return f"Room {self.room_id}: Type {self.room_type}, Capacity {self.capacity}, Price £{self.price}, Status {self.status}"

    def check_availability(self):
        return self.status == "Available"

    def update_status(self, new_status):
        self.status = new_status


