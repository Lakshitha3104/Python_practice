
import psycopg2

conn = psycopg2.connect(
    "postgresql://lakshitha_iirf_user:7mtVnSQljnk59HlJDGS2cRlg6lynh5uO@dpg-d861g0dckfvc73e9hsa0-a.ohio-postgres.render.com/lakshitha_iirf"
)

cur = conn.cursor()
print("Connected successfully")


cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    roll_no INT,
    english INT,
    tamil INT,
    maths INT,
    total INT,
    max_marks INT,
    min_marks INT,
    status VARCHAR(20)
);
""")

conn.commit()
print("Table created successfully")


def get_valid_marks(subject):
    while True:
        try:
            marks = int(input(f"Enter {subject} marks: "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("Marks should be between 0 and 100")
        except ValueError:
            print("Enter only numbers")


def get_only_numbers():
    while True:
        try:
            n = int(input("Enter number of inputs: "))
            if n > 0:
                return n
            else:
                print("Enter valid number")
        except ValueError:
            print("Input should be only numbers")


n = get_only_numbers()

for i in range(n):
    name = input("Enter name: ")
    roll_no = int(input("Enter roll_no: "))

    english = get_valid_marks("English")
    tamil = get_valid_marks("Tamil")
    maths = get_valid_marks("Maths")

    total = english + tamil + maths
    max_marks = max(english, tamil, maths)
    min_marks = min(english, tamil, maths)

    if english >= 35 and tamil >= 35 and maths >= 35:
        status = "Pass"
    else:
        status = "Fail"

    cur.execute("""
        INSERT INTO students
        (name, roll_no, english, tamil, maths, total, max_marks, min_marks, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        name,
        roll_no,
        english,
        tamil,
        maths,
        total,
        max_marks,
        min_marks,
        status
    ))

conn.commit()
print("Data inserted successfully")


cur.execute("SELECT * FROM students")
rows = cur.fetchall()

print("\nStudent data from database:\n")
for row in rows:
    print(row)


cur.close()
conn.close()
print("Everything is Success")
