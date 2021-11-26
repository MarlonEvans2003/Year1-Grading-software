numbstudent = int(input ("Student Number: "))
highest = 0 
highestname = ""
for i in range(0, int (numbstudent)):
    StudentName = str (input ("Student Name: "))
    Mark = int(input("Mark: "))
    if Mark >= 80:
        print ("Student Name: ", StudentName, "/", "Student Score",Mark, "/", "Student Grade:A")  
    elif Mark >= 70:
        print ("Student Name: ", StudentName, "/", "Student Score", Mark, "/", "Student Grade:B")
    elif Mark >= 60:
        print ("Student Name: ", StudentName, "/", "Student Score", Mark, "/", "Student Grade:C")
    elif Mark >= 50:
        print ("Student Name: ", StudentName, "/", "Student Score", Mark, "/", "Student Grade:D")
    elif Mark >= 40:
        print ("Student Name: ", StudentName, "/", "Student Score", Mark, "/", "Student Grade:E")
    else:
        print ("Student Name: ", StudentName, "/", "Student Score", Mark, "/", "Student Grade:Fail")
    if Mark > highest:
        highest = Mark
        highestname = StudentName
print ("Highest: ", highest, "Name: ", highestname)