records = [
    {"id": "S01", "name": "Aarav", "course": "BCA", "year": 2},
    {"id": "S02", "name": "Meera", "course": "BTech", "year": 1},
    {"id": "S03", "name": "Kabir", "course": "BCA", "year": 2},
    {"id": "S04", "name": "Tara", "course": "MCA", "year": 1},
    {"id": "S05", "name": "Ishaan", "course": "BTech", "year": 1}
]

grouped = {}

for student in records:
    course = student["course"]
    year = student["year"]
    sid = student["id"]

    grouped.setdefault(course, {}).setdefault(year, []).append(sid)

print("Grouped:", grouped)

max_course = None
max_year = None
max_count = 0

for course, years in grouped.items():
    for year, students in years.items():
        if len(students) > max_count:
            max_count = len(students)
            max_course = course
            max_year = year

print("Maximum Group:",
      max_course, max_year, grouped[max_course][max_year])

search_id = input("Enter student ID: ")

found = False

for student in records:
    if student["id"] == search_id:
        print("Course:", student["course"])
        print("Year:", student["year"])
        found = True
        break

if not found:
    print("Student not found")