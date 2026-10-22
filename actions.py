from storage import save_students

def add_student(students):
    """Prompts the user to add a new student and saves the data. """
    
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
    
    save_students(students)
   
    
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
    
def delete_student(students):
    """Delete a student from thr list by name. """
    if not students:
        print("No students to delete.")
        return
    
    name_to_delete = input("Enter the name of the students to delete:").lower()
    for i, student in enumerate(students):
        if student["name"].lower() == name_to_delete:
            students.pop(i)
            print(f"Deleted {student['name']}")
            save_students(students)
            return
    print(f"No student found with the name '{name_to_delete}'.")
    
def show_average(students):
    """Calculates and displays the class average"""
    if not students:
        print("No students to calculate an average for. ")
        return
    
    total = 0
    for student in students:
        total += student["grade"]
        
    average = total / len(students)
    print(f"The calss average is : {average:.2f}")
    
def sort_stduents(students):
    """SOrt the students list by grade from highest to lowest."""
    if not students:
        print("No students to sort.")
        return
    
    students.sort(key=lambda x: x["grade"], reverse=True)
    print("Students sorted by highest grade")
    view_students(students)