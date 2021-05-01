import os
import pickle
import student_operations as func
#-----------------------------------------------------------------------------------------
try:
    with open("ActiveStudents.db","rb") as active_students_db:
        active_students=pickle.load(active_students_db)
    with open("GraduatedStudents.db","rb") as graduate_students_db:
        graduate_students=pickle.load(graduate_students_db)
except :
    active_students=[]
    graduate_students=[]

print("Hello !","\n","   Welcome to the students program ","\n","   How can I help you ?")
first=input("    Press 1 for see menu : ")
if first=="1":
    os.system("cls")
    while True :
        print("-------------------------")
        print("Press A key for add student ")
        print("press S key for searching student")
        print("Press M key for move student to graduate students")
        print("press E for edit student")
        print("press L for see list of students")
        print("press V for save students ")
        print("press Q for quit")
        print("-------------------------")

        choise=input("\n\n enter your choise : ")
        print("\n")
        if choise=="A" or choise=="a":
            func.add_student(active_students)
        elif choise=="S" or choise=="s":
            func.search_student(active_students,graduate_students)
        elif choise=="M" or choise=="m":
            func.move_student(active_students,graduate_students)
        elif choise=="E" or choise=="e":
            func.edit_student(active_students)
        elif choise=="L" or choise=="l":
            func.list_student(active_students,graduate_students)
        elif choise=="V" or choise=="v":
            func.save_students(active_students,graduate_students)
        elif choise=="Q" or choise=="q":
            ask=input("\nDo you want to save studet ? (Y/N)")
            if ask=="Y" or ask=="y" or ask==" ":
                func.save_students(active_students,graduate_students)
                break
            if ask=="N" or ask=="n":
                break
            else:
                print("\nPress Y to yes or N to no !")
                continue
        else:
            print("correct your choise !")
            print("-------------------------")
else:
    print("Bye !")
        
        
        



    

