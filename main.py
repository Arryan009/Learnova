import streamlit as st

class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.courses = []
        self.attendance = {}
        self.grades = {}

    def enroll_course(self, course):
        self.courses.append(course)

    def mark_attendance(self, course, date, status):
        if course not in self.attendance:
            self.attendance[course] = []
        self.attendance[course].append({date: status})

    def submit_assignment(self, course, assignment, submission):
        if course in self.courses:
            assignment.submit(self, submission)
    
    def add_grade(self, course, assignment, grade):
        if course not in self.grades:
            self.grades[course] = {}
        self.grades[course][assignment] = grade


class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students = []
        self.assignments = []

    def enroll_student(self, student):
        self.students.append(student)
        student.enroll_course(self.course_name)

    def add_assignment(self, assignment_name):
        assignment = Assignment(assignment_name)
        self.assignments.append(assignment)
        return assignment

    def mark_attendance(self, student, date, status):
        student.mark_attendance(self.course_name, date, status)


class Assignment:
    def __init__(self, assignment_name):
        self.assignment_name = assignment_name
        self.submissions = {}

    def submit(self, student, submission):
        self.submissions[student.student_id] = submission


class Teacher:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def create_course(self, course_name):
        course = Course(course_name, self)
        self.courses.append(course)
        return course

    def assign_grades(self, student, course, assignment, grade):
        student.add_grade(course.course_name, assignment.assignment_name, grade)


teacher = Teacher("Mrs. Rashmi S")
student1 = Student(2343116, "Arryan")
student2 = Student(2343117, "Arth")
student3 = Student(2343139, "Lakshya")


course = teacher.create_course("DSA using C++")
course = teacher.create_course("Mobile Applications (MB)")
course = teacher.create_course("Full Stack Development")
course = teacher.create_course("Python Programming")
course = teacher.create_course("Environmental Studies (EVS)")
course.enroll_student(student1)
course.enroll_student(student2)
course.enroll_student(student3)

assignment = course.add_assignment("Assignment 1")
student1.submit_assignment(course, assignment, "Arryan's Submission")
student2.submit_assignment(course, assignment, "Arth's Submission")
student3.submit_assignment(course,assignment, "Lakshya's Submission")

teacher.assign_grades(student1, course, assignment, 100)
teacher.assign_grades(student2, course, assignment, 100)
teacher.assign_grades(student3, course, assignment, 100)


if 'login_status' not in st.session_state:
    st.session_state['login_status'] = False
    st.session_state['login_type'] = None
    st.session_state['username'] = None
    st.session_state['navigation'] = 'Home'


if not st.session_state['login_status']:
    st.title("Welcome to Learnova")
    

    st.subheader("Login")
    user_type = st.selectbox("Login as:", ["Teacher", "Student"])
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        if user_type == "Teacher":
            
            if username == "Mrs. Rashmi S" and password == "teacher123": 
                st.success("Logged in as Teacher!")
                st.session_state['login_status'] = True
                st.session_state['login_type'] = "Teacher"
                st.session_state['username'] = username 
                st.session_state['navigation'] = "Courses" 
            else:
                st.error("Invalid credentials for Teacher.")
        elif user_type == "Student":
           
            if username in [student1.name, student2.name, student3.name] and password == "student123": 
                st.success(f"Logged in as {username} (Student)!")
                st.session_state['login_status'] = True
                st.session_state['login_type'] = "Student"
                st.session_state['username'] = username 
            else:
                st.error("Invalid credentials for Student.")
else:

    st.sidebar.title("LMS Navigation")
    navigation = st.sidebar.selectbox("Go to", ["Courses", "Assignments", "Students", "Grades"], index=0)
    st.session_state['navigation'] = navigation

   
    if st.session_state['navigation'] == "Courses":
        if st.session_state['login_type'] == "Teacher":
            st.title("Courses Management (Teacher View)")
            
           
            course_name = st.selectbox("Select a Course", [course.course_name for course in teacher.courses])

            selected_course = next(course for course in teacher.courses if course.course_name == course_name)
            
            
            new_assignment = st.text_input("Add New Assignment")
            if st.button("Add Assignment"):
                selected_course.add_assignment(new_assignment)
                st.success(f"Assignment '{new_assignment}' added to {course_name}")

            
            st.subheader("Students Enrolled")
            for student in selected_course.students:
                st.write(f"Student ID: {student.student_id}, Name: {student.name}")
                grade = st.number_input(f"Assign Grade for {student.name}", min_value=0, max_value=100)
                if st.button(f"Submit Grade for {student.name}"):
                    teacher.assign_grades(student, selected_course, selected_course.assignments[-1], grade)
                    st.success(f"Grade {grade} assigned to {student.name}")

        elif st.session_state['login_type'] == "Student":
            st.title("Courses Overview (Student View)")
            
        
            username = st.session_state['username']
            student = student1 if username == student1.name else student2 if username == student2.name else student3
            
            st.subheader("Enrolled Courses")
            for course in student.courses:
                st.write(f"Course: {course}")
                
                st.subheader("Assignments and Grades")
                if course in student.grades:
                    for assignment, grade in student.grades[course].items():
                        st.write(f"{assignment}: {grade}")

    elif st.session_state['navigation'] == "Students":
        st.title("Students List")
        st.subheader("All Students Enrolled")
        for student in [student1, student2, student3]:
            st.write(f"Student ID: {student.student_id}, Name: {student.name}")

    elif st.session_state['navigation'] == "Assignments":
        if st.session_state['login_type'] == "Teacher":
            st.title("Assignments Management (Teacher View)")
            st.write("Here, teachers can manage assignments for their courses.")
        elif st.session_state['login_type'] == "Student":
            st.title("Assignments (Student View)")
            st.write("Here, students can view and submit their assignments.")

    elif st.session_state['navigation'] == "Grades":
        if st.session_state['login_type'] == "Teacher":
            st.title("Grades Management (Teacher View)")
            st.write("Here, teachers can assign and manage grades.")
        elif st.session_state['login_type'] == "Student":
            st.title("Grades (Student View)")
            st.write("Here, students can view their grades.")
