
import psycopg2

conn = psycopg2.connect(
    "postgresql://lakshitha_iirf_user:7mtVnSQljnk59HlJDGS2cRlg6lynh5uO@dpg-d861g0dckfvc73e9hsa0-a.ohio-postgres.render.com/lakshitha_iirf"
)



cur = conn.cursor()

print("Connected successfully")


# Create Table
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    roll_no INT UNIQUE,
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


# Function for Valid Marks
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


# Function for Number of Students
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


# Get Number of Students
n = get_only_numbers()


# Insert Student Data
for i in range(n):

    print(f"\nEnter Details for Student {i+1}")

    name = input("Enter name: ")

    while True:
        try:
            roll_no = int(input("Enter roll_no: "))
            break
        except ValueError:
            print("Roll number should be only numbers")

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

    # Insert into Database
    cur.execute("""
        INSERT INTO students
        (
            name,
            roll_no,
            english,
            tamil,
            maths,
            total,
            max_marks,
            min_marks,
            status
        )

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

print("\nStudent data inserted successfully")


# Display All Records
print("\nStudent Records:\n")

page_size =3
while True:
    page = int(input("\nEnter page number: "))

    offset = (page-1)* page_size
    cur.execute(""" 
          Select * from students where is_deleted = 0 order by id Limit %s OFFSET %s""",(page_size,offset))
    rows = cur.fetchall()
    if rows:
        print(f"\nShowing page {page}\n")
        for row in rows:
            print(row)
    else:
        print("\nNo more records found")

    next_page = input("\nDo you want another page? (yes/no): ")

    if next_page.lower() != "yes":
        break


# Update Feature
choice = input("\nDo you want to update a student record? (yes/no): ")

if choice.lower() == "yes":

    while True:
        try:
            update_roll = int(input("Enter roll number to update: "))
            break
        except ValueError:
            print("Enter only numbers")

    new_english = get_valid_marks("New English")
    new_tamil = get_valid_marks("New Tamil")
    new_maths = get_valid_marks("New Maths")

    new_total = new_english + new_tamil + new_maths

    new_max = max(new_english, new_tamil, new_maths)
    new_min = min(new_english, new_tamil, new_maths)

    if new_english >= 35 and new_tamil >= 35 and new_maths >= 35:
        new_status = "Pass"
    else:
        new_status = "Fail"

    # Update Query
    cur.execute("""
        UPDATE students

        SET
            english = %s,
            tamil = %s,
            maths = %s,
            total = %s,
            max_marks = %s,
            min_marks = %s,
            status = %s

        WHERE roll_no = %s
    """, (
        new_english,
        new_tamil,
        new_maths,
        new_total,
        new_max,
        new_min,
        new_status,
        update_roll
    ))

    conn.commit()

    print("\nStudent record updated successfully")


# Display Updated Records
print("\nUpdated Student Records:\n")

cur.execute("SELECT * FROM students")

updated_rows = cur.fetchall()

for row in updated_rows:
    print(row)
# delete Feature
delete_student = input ("\n Do you want to delete a student record (yes/no): ")
if delete_student.lower() == "yes":
    while True:
        try:
            delete_roll = int(input("Enter Roll_no to delete: "))
            break
        except ValueError:
            print("Enter only numbers")
    cur.execute("""
           UPDATE STUDENTS set is_deleted = 1 WHERE roll_no = %s
                    """,(delete_roll,))
    conn.commit()
    print("\nStudent record deleted succesfully")
    print("\nRemaining student Record:\n")
    cur.execute("select * From students where is_deleted = 0")
    rows = cur.fetchall()
    for row in rows:
        print(row)


# Close Database Connection
cur.close()
conn.close()

print("\nDatabase connection closed")
