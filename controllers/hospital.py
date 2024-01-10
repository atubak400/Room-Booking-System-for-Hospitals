class Hospital:
    def __init__(self, name, address, contact_info):
        self.name = name
        self.address = address
        self.contact_info = contact_info
        self.rooms = []  # List to store available rooms in the hospital

    def __str__(self):
        return f"Hospital Name: {self.name}, Address: {self.address}, Contact: {self.contact_info}"
    
    def get_room_price_by_id(self, room_id):
        for room in self.rooms:
            if room.room_id == room_id:
                return room.price
        return None  # If no room with the given id is found

    def get_room_by_id(self, room_id):
        for room in self.rooms:
            if str(room.room_id) == str(room_id):
                return room
        print(f"No room found with ID: {room_id}")
        return None

    def add_room(self, room):
        self.rooms.append(room)

    def list_available_rooms(self):
        # List all available rooms in the hospital
        available_rooms = [room for room in self.rooms]
        return available_rooms
    
    def list_occupied_rooms(self):
        # List all occupied rooms in the hospital
        occupied_rooms = [room for room in self.rooms if room.status == "Occupied"]
        return occupied_rooms