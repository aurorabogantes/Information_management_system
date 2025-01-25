# School Management System

## Description

The School Management System is a software solution designed to meet the information management needs of the educational institution. The system is built to handle user management, course management, grading, assignments, and academic history, providing functionalities for students, professors, and administrators. This project is intended to automate and streamline school operations through a user-friendly interface, ensuring efficient information handling and access control based on roles.

## Features

- **User Registration and Login**  
  Users can register by providing personal information, including name, email, password, ID, address, age, and role. The system supports three roles: Student, Teacher, and Administrator. Users can log in using their email and password credentials.

- **Role-based Access Control**  
  Depending on the role (Student, Teacher, Administrator), different options and controls are available for the users.

- **Main Menu**  
  Once logged in, the system displays a main menu with options specific to the user role. Professors and students have access to different functionalities.

- **Course Management**  
  Administrators can create, read, edit, and delete courses. Teachers and students can interact with courses through course registration and modification.

- **Grading and Evaluation**  
  Professors can assign grades and evaluations to students. Students can view their grades and add comments to their evaluations.

- **Assignments and Tasks**  
  Professors can assign tasks, while students can submit completed assignments. Task statuses are tracked, and feedback is provided.

- **Academic History**  
  Students can view their academic history, including the courses they have taken, the grades they have received, and a breakdown of their academic performance.

## Installation

1. Clone the repository to your local machine:
git clone https://github.com/aurorabogantes/Information_management_system.git


2. Install the necessary dependencies (e.g., pandas and pickle) if they are not already installed:
pip install pandas


3. Run the program:
python main.py


## Usage

Once the system is running, follow the on-screen prompts to:

1. **Register** as a new user by providing the required information.
2. **Login** using your credentials.
3. Access the **Main Menu** and choose actions based on your role (Student, Teacher, or Administrator).

## Contributing

Feel free to fork the repository, make changes, and create a pull request. If you find any issues or want to suggest improvements, please open an issue on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The project was developed using Python and relies on libraries such as Pandas and Pickle for data storage and management.
- Special thanks to the Python Documentation for the helpful resources and code examples.
