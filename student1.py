import csv




stu = []

def get_valid_marks(subject):
     while True:
        try:
            marks = int(input(f"Enter {subject} marks: "))
            if 0<=marks<=100:
                return marks 
            else:
                print ("Marks should be in the range of 0 to 100")
        except ValueError:
             print("Value Error !! Enter only numbers")

def get_only_numbers():
     while True:
        try:
            n = int(input("Enter number of inputs: "))
            if n > 0:
                return n
            else:
                print("Enter valid number")
        except ValueError:
            print("Input should be only in numbers")
            
               

n = get_only_numbers()
     
for i in range(n):
    li = []
    name = input("Enter name: ")
    roll_no = int(input("Enter roll_no: "))
    
    English = get_valid_marks("English")
    li.append(English)
   
    
    Tamil = get_valid_marks("Tamil")
    li.append(Tamil)
    Maths = get_valid_marks("Maths")
    li.append(Maths)
    Total = English + Tamil + Maths
    
    Max_Marks = max(li)
    Min_Marks = min(li)

    if English >= 35 and Tamil >= 35 and Maths >= 35:
        status = "Pass"
    else:

        status = "Fail"

    students = {
        "name":name,
        "roll_no":roll_no,
        
        "status":status,
        "max_marks":Max_Marks,
        "min_marks":Min_Marks,
        "status":status,
        "total":Total
    }
    stu.append(students)
for i in stu:
        
        print(f"Name:{i['name']} Max_marks:{i['max_marks']} Min_marks:{i['min_marks']} status:{i['status']} Total:{i['total']}")
file = open("students.csv","w",newline = "")
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
    "Status"
])
writer.writerow([
    name,
    roll_no,
    
    English,
    Tamil,
    Maths,
    Total,
    Max_Marks,
    Min_Marks,
    status
])
file.close()