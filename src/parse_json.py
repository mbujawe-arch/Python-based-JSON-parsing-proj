import json

with open('data/students.json', 'r') as file:
    data = json.load(file)

# Access students list
students = data["students"]

# Display student information

for student in students:
    print("Student ID:", student["student_id"])
    print("Name:", student["name"])
    print("Program:", student["program"])

    total_units = 0

    print("\nEnrolled Courses:")

    for course in student["courses"]:
        print("-", course["course_code"])
        print("  Title:", course["course_title"])
        print("  Units:", course["units"])
        print("  Instructor:", course["instructor"])

        total_units += course["units"]

    print("\nTotal Units:", total_units)
    print("-" * 40)