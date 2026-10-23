
from storage import load_students
from actions import add_student, view_students, search_student_grade, delete_student, show_average, sort_students

DATA_FILE = "students.json"

def menu():
    """Displays the menu and returns the user's choice. """
    
    print()    
    print("------ Student Grade Manager -------")
    print("1. Add student")
    print("2. view all students")
    print("3. search all students")
    print("4. show class average")
    print("5. sort students by grade")
    print("6. Delete student")
    print("7. Quit")
    choice = input("Choose an option : ")
    return choice


        
def main():
    """The main loop of the application. """
    students = []
    students = load_students()
    while True:
        choice = menu()
        if choice == "1":
            add_student(students)
            
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student_grade(students)
        elif choice == "4":
            show_average(students)
        elif choice == "5":
            sort_students(students)
        elif choice == "6":
            delete_student(students)
        elif choice == "7":
            print("Goodbye")
            break
        else:
            print("invalid choice. Try again. ")
            

            

            
if __name__ == "__main__":
    main()    