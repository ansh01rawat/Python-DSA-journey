📒 Mini Projects — Study Notes

1. 🏦 Bank Account System
Concepts Practiced:

Classes & Objects (OOP)
Instance variables (balance, account_holder, account_number)
Methods: deposit(), withdraw(), check_balance()
Conditional logic (can't withdraw more than balance)

Key Things to Remember:

__init__ sets up the account when created
Always validate before withdrawing (if amount > self.balance)
Use self to access variables inside class methods

What it teaches: Encapsulation — keeping data (balance) safe inside a class

2. 📒 Contact Book
Concepts Practiced:

Dictionaries ({name: phone_number})
CRUD operations — Create, Read, Update, Delete
Loops and user input
String methods (.strip(), .lower() for search)

Key Things to Remember:

Dictionary is perfect for contacts: contacts["Ansh"] = "9876543210"
Searching should be case-insensitive (use .lower())
Always handle "contact not found" case

What it teaches: Dictionary manipulation + basic data management

3. ❓ MCQ Quiz
Concepts Practiced:

Lists of dictionaries to store questions
Loops to iterate through questions
Score tracking with a counter variable
User input validation

Key Things to Remember:

Store each question as a dict: {"question": "...", "options": [...], "answer": "A"}
Compare user input carefully (input().strip().upper())
Display final score at the end

What it teaches: Lists of dictionaries + control flow + input handling

4. 📋 Menu Function
Concepts Practiced:

while True loop for continuous menu
if-elif-else for option selection
Functions for each menu option
break to exit the loop

Key Things to Remember:

Always include an "Exit" option with break
Each menu option should call a separate function (clean code habit)
Validate invalid inputs with an else clause

What it teaches: Program flow control + structuring code with functions

5. 📦 Inventory Management System
Concepts Practiced:

Nested dictionaries ({item_name: {"price": x, "quantity": y}})
Adding, updating, deleting items
Calculating total inventory value (price × quantity)
Loops + formatted output

Key Things to Remember:

Total value = sum of price * quantity for all items
Check if item exists before updating/deleting
Good use case for f-strings for clean output

What it teaches: Nested data structures + real-world logic

6. 📊 Student Marks Analyzer
Concepts Practiced:

Lists to store marks
Built-in functions: sum(), max(), min(), len()
Average calculation
Grade logic using if-elif

Key Things to Remember:

Average = sum(marks) / len(marks)
Grade boundaries: 90+ → A, 80+ → B, 70+ → C, etc.
Can use a dictionary to store {student_name: [marks]}

What it teaches: List operations + mathematical logic + conditionals

🔗 What All 6 Projects Have in Common
ConceptProjects Using ItFunctionsAll 6LoopsAll 6DictionariesContact Book, Inventory, Quiz, BankOOP / ClassesBank Account SystemUser InputAll 6ConditionalsAll 6
