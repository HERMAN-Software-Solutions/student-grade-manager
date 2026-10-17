# STUDENT GRADE MANAGER
# 1. Show menu
# 2. Get choice
# 3. if 1 - add student
# 4. if 2 - view students
# 5. if 3 - quit
# Repeat until quit

    

    
def menu():
    print()
    print("=== Student Grade Manager ===")
    print("1. Add Student")
    print("2. View all students")
    print("3. search students")
    print("4. Quit")
    choice = input("choose an option : ")
    return choice

def view_students(students):
    if not students:
        print("No students yet. ")
        return
    print()
    print("---All Students---")
    for student in students:
        print(f"{student['name']} : {student['grade']}")
        
def search_student_grade(students):
    student = input("enter the name of the student : ")
    if student in students:
        print(f"{student['name']} : {student['grade']}")
        
def add_student(students):
    name = input("Student name : ")
    try:
        grade = int(input("Student grade : "))
    except ValueError:
        
        print("only integers are allowed1")
    student = {"name": name, "grade": grade}
    students.append(student)
    print(f"Added {name} with grade {grade}. ")
    
def main():
    students = []
    while True:
        choice = menu()
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student_grade(students)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("invalid choice. Try again. ")
            

            
if __name__ == "__main__":
    main()    