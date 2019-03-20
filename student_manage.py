##Coded By JaskaranSM##
import subprocess     #Python Module for interacting with OS calls.
import os             #Python Module for interacting with OS calls


#variables    
name = ""
roll = int()   
clear = "clear"
database = "database.txt"  #Database File Path

#Function Blocks
os.system(clear)   #Function to clear Console Screen xD

#decorate_* functions Decorate Console with some text

def decorate_detail():     
    os.system(clear)
    print("[----------------------------------------------------------------]")
    print("[-                                                              -]")
    print("[-                    Student Detail Entry                      -]")
    print("[-                                                              -]")
    print("[----------------------------------------------------------------]")
def decorate_read():
    os.system(clear)
    print("[----------------------------------------------------------------]")
    print("[-                                                              -]")
    print("[-                   Stored Data in Database                    -]")
    print("[-                                                              -]")
    print("[----------------------------------------------------------------]")


def get_detail():   #function to get info. from user
    decorate_detail()
    print("\n")
    name = input("Enter Name: ")
    roll = input("Enter Roll No.: ")
    write_detail(name,roll)  #calling this function to write all the data user given to a file 

def write_detail(name,roll):        #Function to Write Data in a database file
    f = open(database,"a+")    
    f.write("\nName = " + name)
    f.write("\nRoll No.= " + roll)
    f.write("\n.....................................................................")
    f.close()     

def menu():                        #Main Function Block
    os.system(clear)
    print("---------------------------------------------------------------------------")
    print("-                                                                         -")
    print("-                                                                         -")
    print("-                               MENU                                      -")
    print("-                                                                         -")
    print("-                                                                         -")
    print("---------------------------------------------------------------------------")

    print("\n1.Enter New Student Details ")
    print("\n2.Show All Student Details Currently in Database ")
    print("\n3.Exit")

    choice = int(input("Enter Your Choice: "))
    if choice == 1:
            os.system(clear)
            get_detail()
            opt = int(input("Press 1 to Enter Another detail, any other key(number) to go back to main menu: "))
            while opt == 1:
                os.system(clear)
                get_detail()
                opt = int(input("Press 1 to Enter Another detail, any other key(number) to go back to main menu: "))

            if opt!= 1:
                os.system(clear)
                menu()    

    elif choice == 2:
        decorate_read()
        r = open("database.txt","r")
        db = r.read()
        print(db)
        r.close()
        opt = int(input("Press 1 to go back to main menu: "))
        if opt == 1:
            menu()
        else:
            print("wrong input")    


    else:
        os.system(clear)
        os.system("exit")        

menu()          #main function






