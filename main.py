
import json
import os

DATA_FILE = "students.json"

def menu():
    print()
    print("------ Student Grade Manager -------")
    print("1. Add student")
    print("2. view all students")
    print("3. search all students")
    print("4. Quit")
    choice = input("Choose an option : ")
    return choice

def add_student(students):
    name = input("Student name : ")
    
    while True:
        try:
            grade = int(input("Student grade : "))
            break
        except ValueError:
            
            print("Error : Grade must be a number. Try again.")
    student = {"name": name, "grade": grade}
    students.append(student)
    print(f"Added {name} with grade {grade}. ")
   
    
def view_students(students):
    if not students:
        print("No students yet. ")
        return
    print()
    print("---All Students---")
    for student in students:
        print(f"{student['name']} : {student['grade']}")
        
def search_student_grade(students):
    if not students:
        print("No students to search. ")
        return
    search_name = input("Enter the name of the student: ").lower()
    for student in students:
        if student["name"].lower() == search_name:
            print(f"Found : {student['name']} : {student['grade']}")
            return
        
    print(f"No student found with the name : {search_name}.")
        
def main():
    students = []
    students = load_students()
    while True:
        choice = menu()
        if choice == "1":
            add_student(students)
            save_students(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student_grade(students)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("invalid choice. Try again. ")
            
def save_students(students):
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)
    print("Data saved.")
    
def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)
            

            
if __name__ == "__main__":
    main()    