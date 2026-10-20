import json
import os

DATA_FILE = "students.json"

def save_students(students):
    """Saves the current list of students to the JSON file. """
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)
    print("Data saved.")
    
def load_students():
    """Loads the list of students from JSON file. """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)