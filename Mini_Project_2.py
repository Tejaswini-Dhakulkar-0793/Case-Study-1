# Tejaswini Surendra Dhakulkar
#Roll no.37
# Student Database Management System Using Hashing

students = {}

def insert_student():
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Student Name: ")
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    students[student_id] = {
        "name": name,
        "course": course,
        "marks": marks
    }

    print("Student record inserted successfully!")


def search_student():
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        print("\nStudent Record Found")
        print("Student ID:", student_id)
        print("Name:", students[student_id]["name"])
        print("Course:", students[student_id]["course"])
        print("Marks:", students[student_id]["marks"])
    else:
        print("Student record not found!")


def update_student():
    student_id = input("Enter Student ID to update: ")

    if student_id in students:
        students[student_id]["name"] = input("Enter New Name: ")
        students[student_id]["course"] = input("Enter New Course: ")
        students[student_id]["marks"] = float(
            input("Enter New Marks: ")
        )

        print("Student record updated successfully!")
    else:
        print("Student record not found!")


def delete_student():
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        print("Student record deleted successfully!")
    else:
        print("Student record not found!")


def display_students():
    if not students:
        print("No student records available.")
        return

    print("\n----- STUDENT DATABASE -----")

    for student_id, details in students.items():
        print("\nStudent ID:", student_id)
        print("Name:", details["name"])
        print("Course:", details["course"])
        print("Marks:", details["marks"])


while True:
    print("\n===== STUDENT DATABASE MANAGEMENT =====")
    print("1. Insert Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_students()
    elif choice == "6":
        print("Thank you for using Student Database!")
        break
    else:
        print("Invalid choice! Please try again.")
