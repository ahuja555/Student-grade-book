import array

# ----------------------------------------------------
# Data Structures Setup
# ----------------------------------------------------
# 1. LIST: Holds all student records (dynamically scalable)
student_records = []

# 2. SET: Holds unique subjects taught across the grade book
unique_subjects = {"Math", "Science", "History", "English"}


# ----------------------------------------------------
# Core Functions
# ----------------------------------------------------
def add_student(student_id: int, name: str, grades_list: list):
    """
    Adds a new student record.
    Uses a TUPLE for personal info and an ARRAY for numeric grades.
    """
    # 3. TUPLE: Immutable pairing of ID and Name
    student_info = (student_id, name)
    
    # 4. ARRAY: Efficiently stores numeric grades ('i' for integers)
    grades_array = array.array('i', grades_list)
    
    # Bundle them together inside our main list
    student_records.append({
        "info": student_info,
        "grades": grades_array
    })
    print(f"Successfully added student: {name}")


def search_student_by_name(search_name: str):
    """
    Searches for a student by their name (case-insensitive)
    and prints their details if found.
    """
    print(f"\n--- Searching for '{search_name}' ---")
    found = False
    
    for record in student_records:
        # Accessing data from the tuple
        student_id, name = record["info"]
        
        if name.lower() == search_name.lower():
            found = True
            # Accessing data from the array
            grades = record["grades"].tolist()  # Convert array back to list for easy printing
            average = sum(grades) / len(grades) if grades else 0
            
            print(f"ID: {student_id}")
            print(f"Name: {name}")
            print(f"Grades: {grades}")
            print(f"Average Grade: {average:.2f}")
            break
            
    if not found:
        print(f"No student found with the name '{search_name}'.")


def display_all_subjects():
    """
    Displays the current unique subjects tracked in the system.
    """
    print("\n--- Tracked Subjects ---")
    # Set item iteration
    for subject in unique_subjects:
        print(f"- {subject}")


# ----------------------------------------------------
# Populate Sample Data
# ----------------------------------------------------
# Adding students with an ID, Name, and a list of 4 grades corresponding to our 4 subjects
add_student(101, "Alice Smith", [85, 92, 78, 90])
add_student(102, "Bob Jones", [70, 65, 80, 75])
add_student(103, "Charlie Brown", [95, 88, 91, 89])


# ----------------------------------------------------
# User Interactive Loop
# ----------------------------------------------------
def main():
    display_all_subjects()
    
    while True:
        print("\n=== Grade Book Options ===")
        print("1. Search for a student")
        print("2. Exit")
        
        choice = input("Enter your choice (1 or 2): ").strip()
        
        if choice == "1":
            user_input = input("Enter the student's full name to search: ").strip()
            search_student_by_name(user_input)
        elif choice == "2":
            print("Exiting Grade Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

# Run the program
if __name__ == "__main__":
    main()
