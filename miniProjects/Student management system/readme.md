# Student Management System

## Overview

The **Student Management System** is a console-based Python application that allows users to manage student records efficiently through a menu-driven interface.

This project demonstrates the use of Python fundamentals such as dictionaries, functions, loops, exception handling, and CRUD operations.

---

## Features

* Add Student
* Search Student
* Update Student
* Delete Student
* Display All Students
* Prevent Duplicate Student Entries
* Handle Invalid User Input
* Save data in file
* Load data from file
* Menu-Driven Interface

---

## Technologies Used

* Python
* Dictionaries (Hash Maps)
* Functions
* Loops
* Conditional Statements
* Exception Handling
* File Handling

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

Student records are stored in a Python dictionary.

Example:

```python
students = {
    "Ansh": 12345,
    "Rahul": 67890
}
```

* **Key** → Student Name
* **Value** → Enrollment Number

---

## Menu Options

```text
====== Student Management System ======

1. Add Student
2. Search Student
3. Delete Student
4. Display Students
5. Update Student
6. Exit Program
```

---

## Functionalities

### Add Student

Allows users to add a new student record.

Example:

```text
Name of the student: Ansh
Enrollment no.: 12345

Ansh added successfully
```

---

### Search Student

Searches for a student by name.

Example:

```text
Name of the student: Ansh

Name = Ansh | Enrollment no. 12345
```

---

### Update Student

Updates an existing student's name while preserving the enrollment number.

Example:

```text
Enter name to update: Ansh
Enter new name: Rahul

Student updated successfully
```

---

### Delete Student

Removes a student record from the system.

Example:

```text
Enter name to delete: Rahul

Student deleted successfully
```

---

### Display Students

Displays all student records currently stored in the system.

Example:

```text
Name = Ansh | Enrollment no. 12345
Name = Rahul | Enrollment no. 67890
```

---

## Error Handling

The application handles:

* Invalid menu choices
* Non-integer enrollment numbers
* Duplicate student names
* Updating to an already existing student name
* Searching or deleting non-existing students

---

## Time Complexity Analysis

| Operation        | Time Complexity |
| ---------------- | --------------- |
| Add Student      | O(1)            |
| Search Student   | O(1)            |
| Update Student   | O(1)            |
| Delete Student   | O(1)            |
| Display Students | O(n)            |

where **n** is the number of students.

---

## Concepts Practiced

* Python Dictionaries
* Functions
* CRUD Operations
* Exception Handling
* User Input Validation
* Menu-Driven Programming

---

## Learning Outcomes

Through this project, I learned:

* How to organize code using functions.
* How to perform CRUD operations.
* How dictionaries provide efficient data storage and retrieval.
* How to validate user input using `try-except`.
* How to build a complete console-based Python application.

---

## Future Improvements

* Update Enrollment Number
* Store Additional Student Information (Course, Year, Email)
* Save Data to Files
* Load Data from Files
* Sort Students Alphabetically
* Use Nested Dictionaries

---

## Author

**Ansh Rawat**

B.Tech CSE (Applied Mathematics)

Vivekananda Institute of Professional Studies
