students = {"yogesh":"A", "rohit":"B", "tushar":"C"}

# Add a new student and grade
name = "rohan"
grade = "D"
students[name] = grade

# Update an existing student's grade
students["tushar"] = grade

# Print all students and their grades
for name, grade in students.items():
 print(f"{name}: {grade}")
