# Student Management System

## Overview

Student Management System is a simple Python-based console application that allows users to manage student records through a menu-driven interface.

The project demonstrates the use of Python dictionaries, functions, loops, exception handling, and CRUD (Create, Read, Delete) operations.

---

## Features

* Add Student
* Search Student
* Delete Student
* Display All Students
* Prevent Duplicate Entries
* Handle Invalid Inputs
* Menu-Driven Interface

---

## Technologies Used

* Python
* Dictionaries
* Functions
* Loops
* Conditional Statements
* Exception Handling

---

## Project Structure

```text
StudentManagementSystem/
│
├── student_management.py
└── README.md
```

---

## How It Works

The program stores student records in a dictionary:

```python
students = {
    "Ansh": 12345,
    "Rahul": 67890
}
```

* Key → Student Name
* Value → Enrollment Number

---

## Menu Options

```text
1. Add Student
2. Search Student
3. Delete Student
4. Display Students
5. Exit Program
```

---

## Example Output

```text
====== Student Management System ======

1. Add Student
2. Search Student
3. Delete Student
4. Display Students
5. Exit Program

Enter your choice: 1

Name of the student: Ansh
Enrollment no.: 12345

Ansh added successfully
```

---

## Complexity Analysis

| Operation        | Time Complexity |
| ---------------- | --------------- |
| Add Student      | O(1)            |
| Search Student   | O(1)            |
| Delete Student   | O(1)            |
| Display Students | O(n)            |

where n is the number of students.

---

## Concepts Practiced

* Dictionaries (Hash Maps)
* Functions
* CRUD Operations
* User Input Handling
* Exception Handling
* Menu-Driven Programming

---

## Learning Outcomes

Through this project, I learned:

* How to organize code using functions
* How to store and retrieve data using dictionaries
* How to handle invalid user input with try-except
* How CRUD operations work in real-world applications
* How to build a complete console-based Python application

---

## Future Improvements

* Update Student Details
* Store Multiple Student Attributes
* Save Data to File
* Load Data from File
* Sort Students Alphabetically

---

### Author

Ansh Rawat

B.Tech CSE (Applied Mathematics)

Vivekananda Institute of Professional Studies
