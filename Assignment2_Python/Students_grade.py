students = {}

while True:
    print("\n1.Add Studnt")
    print("2.Update Student Grade")
    print("3.Print All Student")
    print("4.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("Student added successfully")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updatd successfully")
        else:
            print("Student not found")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        break

    else:
        print("Choose from the given options(1,2,3,4)")