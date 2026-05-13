n = int(input("Enter number of inputs: "))
stu = []
for i in range(n):
    name = input("Enter name: ")
    roll_no = int(input("Enter roll_no: "))
    marks = int(input("Enter marks: "))
    if marks >= 35:
        status = "pass"
    else:
        status = "fail"
    
    students = {
        "name":name,
        "roll_no":roll_no,
        "marks":marks,
        "status":status
    }
    stu.append(students)
for i in stu:
        print(f"Name:{i['name']} Roll_no:{i['roll_no']} Marks:{i['marks']} status:{i['status']}")
