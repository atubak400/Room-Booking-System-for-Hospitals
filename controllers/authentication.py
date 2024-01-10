import csv
import os

class Authentication:
    def __init__(self, filepath):
        self.filepath = filepath

    def user_exists(self, username):
        with open(self.filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and username == row[0]:
                    return True
        return False

    def register_user(self, username, password, role):
        if self.user_exists(username):
            print(f"{username} already exists. Please choose a different username.")
            return False
        else:
            with open(self.filepath, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([username, password, role])
            print("Registration Successfull.")
            return True

    def login_user(self, username, password):
        with open(self.filepath, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and username == row[0] and password == row[1]:
                    print("Login Successfull")
                    return True
        print("Invalid username or password. Login failed.")
        return False

 
