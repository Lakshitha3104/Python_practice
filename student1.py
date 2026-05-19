import csv


class Student:
    def __init__(self, name, roll_no, english, tamil, maths):
        self.name = name
        self.roll_no = roll_no
        self.english = english
        self.tamil = tamil
        self.maths = maths

        self.total = self.calculate_total()
        self.max_marks = self.calculate_max()
        self.min_marks = self.calculate_min()
        self.status = self.calculate_status()
        self.rank = self.calculate_rank()

    def calculate_total(self):
        return self.english + self.tamil + self.maths

    def calculate_max(self):
        return max(self.english, self.tamil, self.maths)

    def calculate_min(self):
        return min(self.english, self.tamil, self.maths)

    def calculate_status(self):
        if self.english >= 35 and self.tamil >= 35 and self.maths >= 35:
            return "Pass"
        return "Fail"

    def calculate_rank(self):
        if self.total >= 270:
            return "Rank 1"
        elif self.total >= 240:
            return "Rank 2"
        elif self.total >= 180:
            return "Rank 3"
        else:
            return "No Rank"

    def display(self):
        print(
            f"Name: {self.name} | "
            f"Roll No: {self.roll_no} | "
            f"Total: {self.total} | "
            f"Max: {self.max_marks} | "
            f"Min: {self.min_marks} | "
            f"Status: {self.status} | "
            f"Rank: {self.rank}"
        )

    def to_csv_row(self):
        return [
            self.name,
            self.roll_no,
            self.english,
            self.tamil,
            self.maths,
            self.total,
            self.max_marks,
            self.min_marks,
            self.status,
            self.rank
        ]


def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100")
        except ValueError:
            print("Enter numbers only")


def get_valid_number():
    while True:
        try:
            n = int(input("Enter number of students: "))
            if n > 0:
                return n
            else:
                print("Enter valid number")
        except ValueError:
            print("Numbers only")


students_list = []

file = open("students.csv", "w", newline="")
writer = csv.writer(file)

writer.writerow([
    "Name",
    "Roll No",
    "English",
    "Tamil",
    "Maths",
    "Total",
    "Max Marks",
    "Min Marks",
    "Status",
    "Rank"
])

n = get_valid_number()

for i in range(n):
    name = input("Enter name: ")
    roll_no = int(input("Enter roll no: "))

    english = get_valid_marks("English")
    tamil = get_valid_marks("Tamil")
    maths = get_valid_marks("Maths")

    student = Student(name, roll_no, english, tamil, maths)

    students_list.append(student)
    writer.writerow(student.to_csv_row())

file.close()

for student in students_list:
    student.display()