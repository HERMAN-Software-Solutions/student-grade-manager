
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
    student = input("enter the name of the student : ")
    if student in students:
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
            search_student_grade(students)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("invalid choice. Try again. ")
            

            
if __name__ == "__main__":
    main()    