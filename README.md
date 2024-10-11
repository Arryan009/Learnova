# Learnova

Overview
The Learning Management System (LMS) is a Python-based web application built using Streamlit, designed to facilitate the management of courses, students, assignments, and grades. The system supports both teachers and students, providing tailored views and functionalities for each user type.

Features
For Teachers:
Course Management: Create and manage courses, and enroll students.
Assignment Management: Add assignments to courses and view submissions.
Attendance Management: Mark attendance for enrolled students.
Grades Management: Assign and manage grades for assignments submitted by students.
For Students:
Course Overview: View all enrolled courses.
Assignment Submissions: Submit assignments for courses.
Grades Access: View grades for submitted assignments.
Technologies Used
Python: The primary programming language used for developing the application.
Streamlit: A framework used for creating the web interface, allowing for rapid development and deployment.
Structure
The code is organized into several classes that represent the core entities of the system:

Student Class:

Represents a student with attributes such as ID, name, courses enrolled, attendance records, and grades.
Methods to enroll in courses, mark attendance, submit assignments, and add grades.
Course Class:

Represents a course with attributes such as the course name, teacher, enrolled students, and assignments.
Methods to enroll students, add assignments, and mark attendance.
Assignment Class:

Represents an assignment within a course, tracking submissions from students.
Teacher Class:

Represents a teacher with methods to create courses and assign grades to students.

Usage
Login:

Users can log in as either a Teacher or Student using predefined credentials.
Example credentials:
Teacher:
Username: Mrs. Rashmi S
Password: teacher123
Students:
Username: Arryan, Arth, or Lakshya
Password: student123
Navigation:

Upon logging in, users will see a sidebar with navigation options to access different functionalities like Courses, Assignments, Students, and Grades.
Features:

Teachers can create courses, manage assignments, and assign grades.
Students can view their enrolled courses, submit assignments, and check their grades.
Future Enhancements
User Authentication: Implement a more secure user authentication system.
Database Integration: Use a database to persist data beyond application runtime.
User Interface Improvements: Enhance the UI for better user experience.
Additional Features: Implement notifications for upcoming assignments and deadlines.
Contributing
Contributions are welcome! Please follow these steps:

Fork the repository.
Create a new branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Streamlit for providing a powerful and easy-to-use framework for building web applications in Python.

HOW TO RUN:-

install streamlit 

pip install streamlit 

run the app - streamlit run main.py
