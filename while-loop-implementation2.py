toContinue = "Y"
students = []

while toContinue.upper() != "N":

    studentNo = input("Student No: ")
    studentName = input("Student Name: ")
    studentSurname = input("Student Surname: ")

    students.append({
        "studentNo": studentNo,
        "studentName": studentName,  
        "studentSurname": studentSurname
    })

    toContinue = input("Continue? (Y/N): ").strip()

for student in students:
    print(f"{student["studentNo"]} numaralı öğrencinin adı {student["studentName"]} {student["studentSurname"]}")