import os
import pickle
from datetime import datetime as dt
#----------------------------------
def check(code,key,func):
    for student in func:
        if student[key]==code:
            return True
    return False
"""-------functions-------"""

def  add_student(students):
    os.system("cls")
    student=dict()
    print("-------------------------")
    student["first name"]=input("Enter the first name of a student : ")
    student["last name"]=input("Enter the last name of a student : ")
    while True:
        try:
            student["national code"]=input("Enter the national code of a student : ")
            if len(student["national code"])!=10 :
                raise Exception()
            elif check(student["national code"],"national code",students)==True:
                print("\nThis code has Entered before ! \n")
            else : 
                break
        except:
            print("\nNational code is a 10 digit number ! \n ")
    while True:
        try:
            student["student code"]=int(input("Enter the student code (7 digit number) : "))
            if student["student code"]<1000000  or student["student code"]>9999999:
                raise Exception()
            elif check(student["student code"],"student code",students)==True:
                print("\nThis code has Entered before ! \n")
            else:
                break
        except:
            print("\nStudent code is a 7 digit number ! \n")
    while True:
        try:
            birthday=input("Enter student birthday in YYYY/MM/DD format : ")
            student["birthday"]=dt.strptime(birthday,"%Y/%m/%d").date()
            break
        except:
            print("please enter in this format : YYYY/MM/DD")
    
    student["courses"]=list()
    student["grades"]=list()
    while True:
        print("\n")
        course=input("Enter course name : ")
        try:
            grade=int(input("Enter grade (between 0-100) : "))
            if grade>100:
                raise Exception()
        except:
            print("\nEnter number between 0-100 \n")
            continue
        student["courses"].append(course)
        student["grades"].append(grade)
        print("\n")

        try:  
            while True:
                ask=input("Enter another course ?  (Y/N) ")
                if ask=="Y" or ask=="y"  :
                    break
                elif ask=="N" or ask=="n":
                    raise Exception()
                else:
                    print("Please enter Y or N !")
                    continue
        except:     
            break
    students.append(student)
    os.system("cls")
    
#-------------------------------------------------------------------

def search_student(active_students,graduate_students):
    choise=input("Press G for graduate students and A for active students : ")
    print("\n")
    if choise=="G" or choise=="g":
        stcode=int(input("Enter student code : "))
        print("\n")
        for student in graduate_students:
            if student["student code"]==stcode:
                os.system("cls")
                print("\nFirst name  :  ",student["first name"])
                print("\nLast name  :  ",student["last name"])
                print("\nNational code  :  ",student["national code"]) 
                print("\nStudent code  :  ",student["student code"])
                print("\nBirthday  :  ",student["birthday"])
                birthday=student["birthday"].year
                print("\nAge  :  ",1400-birthday)
                print("----------courses----------\n")
                for i in student["courses"]:
                    j=student["courses"].index(i)
                    print(student["courses"][j]," : ",student["grades"][j])
                Sum=0
                z=0
                for grade in student["grades"]:
                    Sum=Sum+grade
                    z=z+1
                avg=Sum/z
                Max=max(student["grades"])
                Min=min(student["grades"])
                print("\nAverage of grades : ",avg)
                print("\nMaximum grade : ",Max) 
                print("\nMinimum grade : ",Min)

        input()
        os.system("cls")
                
    
    elif choise=="A" or choise=="a":
        stcode=int(input("Enter student code : "))
        print("\n")
        for student in active_students:
            if student["student code"]==stcode:
                os.system("cls")
                print("\nFirst name  :  ",student["first name"])
                print("\nLast name  :  ",student["last name"])
                print("\nNational code  :  ",student["national code"]) 
                print("\nStudent code  :  ",student["student code"])
                print("\nBirthday  :  ",student["birthday"])
                birthday=student["birthday"].year
                print("\nAge  :  ",1400-birthday)
                print("----------courses----------\n")
                for i in student["courses"]:
                    j=student["courses"].index(i)
                    print(student["courses"][j]," : ",student["grades"][j])
                Sum=0
                z=0
                for grade in student["grades"]:
                    Sum=Sum+grade
                    z=z+1
                avg=Sum/z
                Max=max(student["grades"])
                Min=min(student["grades"])
                print("\nAverage of grades : ",avg)
                print("\nMaximum grade : ",Max) 
                print("\nMinimum grade : ",Min)            
        input()
        os.system("cls")
    else:
        print("Wrong choise !")
        
#-------------------------------------------------------------------
def move_student(active_students,graduate_students):
    try: 
        stcode=int(input("Enter student code : "))
        print("\n")
        for student in active_students:
            if student["student code"]==stcode:
                graduate_students.append(student)
                active_students.remove(student)
                print("\nstudent moved successfully !")
            
    except:
        print("\nThis student code does not exist !")

    os.system("cls")        
#-------------------------------------------------------------------
def edit_student(active_students):
    stcode=int(input("Enter student code for edit : "))
    print("\n")
    for student in active_students:
        if student["student code"]==stcode:
            while True:
                    course=input("Enter course name : ")
                    try:
                        grade=int(input("Enter grade (between 0-100) : "))
                        if grade>100:
                            raise Exception
                    except:
                        print("\nEnter number between 0-100 \n")
                        continue
                    student["courses"].append(course)
                    student["grades"].append(grade)
                    print("\n")
                    try:  
                        while True:
                            ask=input("Enter another course ?  (Y/N) ")
                            if ask=="Y" or ask=="y"  :
                                break
                            elif ask=="N" or ask=="n":
                                raise Exception()
                            else:
                                print("Please enter Y or N !")
                                continue
                    except:
                        break

    else:
        os.system("cls")
    
#-------------------------------------------------------------------
def save_students(active_students,graduate_students):
    try:
        with open ("ActiveStudents.db","wb") as active_students_db:
            pickle.dump(active_students,active_students_db)
    
        with open ("GraduatedStudents.db","wb") as graduate_students_db:
            pickle.dump(graduate_students,graduate_students_db)
        print("\nStudent saved successfully ...")
    except:
        print("\nThere is a problem in save process !")
        return 0

    input()
    os.system("cls")

#-------------------------------------------------------------------
def list_student(active_students,graduate_students):
    os.system("cls")
    active_students.sort(key=lambda k : k["student code"])
    graduate_students.sort(key=lambda k : k["student code"])
    print("\n--------------------------------active students--------------------------------\n")
    num=1
    for student in active_students:
        print("Student ",num," :")
        print("\nFirst name  :  ",student["first name"])
        print("\nLast name  :  ",student["last name"])
        print("\nNational code  :  ",student["national code"]) 
        print("\nStudent code  :  ",student["student code"])
        print("\nBirthday  :  ",student["birthday"])
        birthday=student["birthday"].year
        print("\nAge  :  ",1400-birthday)
        num=num+1
        print("========================================\n")
    print("------------------------------graduate students------------------------------")
    num2=1
    for student in graduate_students:
        print("Student ",num2," :")
        print("\nFirst name  :  ",student["first name"])
        print("\nLast name  :  ",student["last name"])
        print("\nNational code  :  ",student["national code"]) 
        print("\nStudent code  :  ",student["student code"])
        print("\nBirthday  :  ",student["birthday"])
        birthday=student["birthday"].year
        print("\nAge  :  ",1400-birthday)
        num2=num2+1
        print("========================================")
    input()
    os.system("cls")








