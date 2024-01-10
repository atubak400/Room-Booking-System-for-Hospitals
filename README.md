# Hospital Room Booking System with Python Flask (OOP)

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Usage](#usage)
   - [Configuration](#configuration)
   - [Running the Application](#running-the-application)
5. [Folder Structure](#folder-structure)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)



## Introduction

Welcome to the Hospital Room Booking System, a robust solution designed to streamline and simplify the process of managing room bookings within a medical facility. This system leverages the power of Python and Flask to provide an efficient and user-friendly interface for both patients and receptionists.

### Purpose

The primary purpose of this system is to facilitate the seamless booking of rooms within a hospital, ensuring optimal utilization of resources. Patients can conveniently schedule appointments, book rooms, and manage their bookings, while receptionists can efficiently oversee and coordinate these activities. The system aims to enhance the overall experience for both patients and medical staff by automating the room booking process and reducing administrative overhead.

Whether you are a patient looking to book a room for a medical appointment or a receptionist responsible for managing room allocations, this Hospital Room Booking System is designed to meet your needs, offering a reliable and organized platform for hospital room management.

## Features

Discover the comprehensive features offered by the Hospital Room Booking System, designed to optimize the management of medical appointments and room bookings:

1. **User Authentication:**
   - Secure registration and login system for patients and receptionists.

2. **Appointment Management:**
   - Schedule, update, and cancel medical appointments with ease.
   - View a list of all appointments for better coordination.

3. **Room Booking:**
   - Effortlessly book hospital rooms for medical appointments.
   - Check room availability to make informed booking decisions.

4. **Room Management:**
   - Differentiate between Standard and ICU rooms.
   - Monitor and update room statuses to reflect availability.

5. **Invoice Generation:**
   - Automatically generate invoices for room bookings.
   - Request payments from patients for booked services.

6. **Payment Handling:**
   - Provide a seamless payment process for confirmed room bookings.
   - Generate and print receipts for completed transactions.

7. **User-Friendly Interface:**
   - Intuitive menu-driven system for easy navigation.
   - Clear prompts and feedback for a user-friendly experience.

8. **Data Persistence:**
   - Utilize CSV files to store and retrieve booking information.
   - Ensure data integrity for reliable and consistent records.

9. **Flexible Configuration:**
   - Easily configure the system settings, including hospital information.

10. **Informative Outputs:**
    - Display available rooms, appointment details, and invoices.
    - Keep users informed with relevant and timely information.

Explore these features to make the most of the Hospital Room Booking System, simplifying the workflow for both medical staff and patients.


## Prerequisites

Before running the Hospital Room Booking System, ensure that you have the following software, tools, and dependencies installed on your system:

1. **Python:**
   - The system is built using Python, so ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

2. **Flask:**
   - Install the Flask web framework using the following command:
     ```bash
     pip install Flask
     ```

3. **CSV Module:**
   - The system uses CSV files for data persistence. Python includes a built-in `csv` module, so no additional installation is required.

4. **Dependencies:**
   - Ensure that you have all the dependencies specified in the project. You can install them using the following command:
     ```bash
     pip install -r requirements.txt
     ```

5. **Text Editor or IDE:**
   - Use a text editor or integrated development environment (IDE) of your choice to view and modify the source code. Popular choices include Visual Studio Code, PyCharm, or Sublime Text.

6. **Command Line Interface (CLI):**
   - A command-line interface is needed to run the application. Ensure that you have a functional CLI for executing Python scripts.

7. **Web Browser:**
   - To interact with the system, use a modern web browser such as Google Chrome, Mozilla Firefox, or Microsoft Edge.

8. **Git (Optional):**
   - If you want to clone the repository, manage version control, or contribute to the project, install Git from [git-scm.com](https://git-scm.com/).

Ensure that all prerequisites are met before proceeding with the installation and execution of the Hospital Room Booking System.

## Usage

### Configuration

Before running the Hospital Room Booking System, you may want to configure certain options and settings:

1. **Hospital Information:**
   - Open the `main.py` file and locate the initialization of the `Hospital` class (e.g., `hospital = Hospital(...)`).
   - Modify the parameters such as `name`, `address`, and `contact_info` to match the information of your hospital.

2. **CSV File Path:**
   - In the `main.py` file, check and update the `file_path` variable in the `manage_booking()` and `manage_invoices()` functions if your CSV file is located in a different directory.

3. **User Authentication Configuration (Optional):**
   - Open the `users.csv` file to add or modify user credentials for testing purposes.
   - Customize the usernames, passwords, and roles as needed.

### Running the Application

Follow these steps to run the Flask application of the Hospital Room Booking System:

1. **Activate the Virtual Environment (if not already activated):**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

2. **Run the Flask Application:**
   ```bash
   python main.py


## Technologies Used

Explore the technologies and frameworks that power the Hospital Room Booking System, contributing to its robust functionality and user-friendly experience:

1. **Python:**
   - The primary programming language used for the backend logic and server-side development.

2. **Flask:**
   - A lightweight and modular web framework for Python, utilized to build the web application.

3. **CSV Module:**
   - Python's built-in `csv` module for reading and writing CSV files, employed for data persistence.

4. **HTML:**
   - The standard markup language for creating the structure of web pages.
  
5. **Jinja2 Templating Engine:**
   - Integrated with Flask, Jinja2 is used for dynamic content rendering in HTML templates.

6. **Git:**
   - A distributed version control system for tracking changes in the source code and collaboration.

7. **GitHub:**
   - A web-based platform for version control using Git, facilitating collaboration and project management.

8. **Virtual Environment (venv):**
   - Python's built-in tool for creating isolated Python environments, enhancing dependency management.

9. **Text Editor or IDE:**
   - A text editor or integrated development environment used for writing, editing, and managing the source code.

10. **Command Line Interface (CLI):**
    - The command-line interface is utilized for executing Python scripts and managing the application.

11. **Web Browsers:**
    - Modern web browsers such as Google Chrome, Mozilla Firefox, or Microsoft Edge for accessing and interacting with the web-based application.

These technologies collectively contribute to the development, functionality, and deployment of the Hospital Room Booking System, ensuring a reliable and efficient solution for managing hospital room bookings.



## Contributing

Thank you for considering contributing to the Hospital Room Booking System! Your involvement helps enhance the functionality and reliability of the system. Please take a moment to review the following guidelines:

### How to Contribute

1. **Fork the Repository:**
   - Fork the repository to your own GitHub account.

2. **Clone the Repository:**
   - Clone the forked repository to your local machine:
     ```bash
     git clone https://github.com/atubak400/Room-Booking-System-for-Hospitals.git
     ```

3. **Create a Branch:**
   - Create a new branch for your contributions:
     ```bash
     git checkout -b feature/new-feature
     ```

4. **Make Changes:**
   - Implement your changes or add new features.

5. **Commit Changes:**
   - Commit your changes with a clear and concise commit message:
     ```bash
     git commit -m "Add new feature: XYZ"
     ```

6. **Push Changes:**
   - Push your changes to your forked repository:
     ```bash
     git push origin feature/new-feature
     ```

7. **Submit a Pull Request:**
   - Open a pull request from your forked repository to the original repository.

8. **Code Review:**
   - Participate in the code review process, addressing any feedback.

### Development Guidelines

- Follow the [PEP 8 style guide](https://www.python.org/dev/peps/pep-0008/) for Python code.
- Ensure that your code is well-documented, including clear comments where necessary.
- Test your changes thoroughly to avoid introducing bugs.
- If you're introducing new features, consider updating the documentation accordingly.

### Issues and Bug Reports

- Report any issues or bugs by creating a new [issue](https://github.com/your-username/hospital-room-booking-system/issues).
- Clearly describe the problem, provide steps to reproduce, and include any relevant information.

Your contributions, whether big or small, are highly valued. Thank you for helping make the Hospital Room Booking System a better solution for everyone!

# Room-Booking-System-for-Hospitals
