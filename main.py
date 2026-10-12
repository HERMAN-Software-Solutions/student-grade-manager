# STUDENT GRADE MANAGER
# 1. Show menu
# 2. Get choice
# 3. if 1 - add student
# 4. if 2 - view students
# 5. if 3 - quit
# Repeat until quit

def main():
    print("Student Grade Manager - starting up")
    
if __name__ == "__main__":
    main()
    
def menu():
    print()
    print("=== Student Grade Manager ===")
    print("1. Add Student")
    print("2. View all students")
    print("3. Quit")
    choice = input("choose an option : ")
    return choice

def add_student(students):
    name = input("Student name : ")
    grade = int(input("Student grade : "))
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
        
def main():
    students = []
    while True:
        choice = menu()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            print("Goodbye")
            break
        else:
            print("invalid choice. Try again. ")