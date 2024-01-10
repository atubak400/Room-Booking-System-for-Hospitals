class Invoice:
    def __init__(self, room_id, price, patient_name, date):
        self.room_id = room_id
        self.price = price
        self.patient_name = patient_name
        self.date = date

    def generate_invoice(self):
        print("---------------------------")
        print("---------------------------")
        print("Invoice:")
        print("Room ID: ", self.room_id)
        print("Patient Name: ", self.patient_name)
        print("Date: ", self.date)
        print("Price: $", self.price)
        print("Total: $", self.price)
        print("---------------------------")
        print("---------------------------")

    def request_payment(self):
        while True:
            payment = input(
                "Make your payment here by entering your payment amount: $")
            try:
                payment = float(payment)
                if payment >= self.price:
                    print("Payment successful! Thank you!")
                    break
                else:
                    print("Payment amount is less than the total.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def print_receipt(self):
        print("---------------------------")
        print("---------------------------")
        print("Receipt:")
        print("Room ID: ", self.room_id)
        print("Patient Name: ", self.patient_name)
        print("Date: ", self.date)
        print("Amount Paid: $", self.price)
        print("Thank you for your payment!")
        print("---------------------------")
        print("---------------------------")
