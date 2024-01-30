time = 0


class Student:
    def __init__(self, age, name, address, grade, salary, job):
        self.age = age
        self.name = name
        self.address = address
        self.grade = grade
        self.salary = salary
        self.job = job


Student_1 = Student(24, "Jim", "London", 4, 1250, "programmer")
while True:
    a = input("Choose what to do: relax,study,work? ").lower()

    if a == "relax":
        print("Relaxing", )
        print("Your salary is:", Student_1.salary - 250, "and your grade is:", Student_1.grade - 1)
        print("1 month left")
        time = time + 1
        Student_1.salary = Student_1.salary - 250
        Student_1.grade = Student_1.grade - 1
    elif a == "study":
        print("Studying")
        print("Your grade is:", Student_1.grade + 1)
        print("1 month left")
        time = time + 1
        Student_1.grade = Student_1.grade + 1
    elif a == "work":
        print("Working")
        print("Your salary is:", Student_1.salary + 345)
        print("1 month left")
        time = time + 1
        Student_1.salary = Student_1.salary + 345

    if time == 12:
        print("\n\n\t\tYou have lived one year")
        break

