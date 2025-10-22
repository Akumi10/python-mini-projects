
student_number = int(input("Enter the number of students: "))

students = []

for i in range(student_number):
    name = input(f"Enter name of student {i+1}: ")
    degree = int(input(f"Enter degree of {name}: "))
    students.append([name, degree])  


print("\nList of students:")
for student in students:
    print(f"{student[0]} - {student[1]}")
