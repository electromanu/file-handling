import sys
import os
def fun():
    print("choose your option\n 1.create fle\n 2.read file\n 3.edit file\n 4.list file\n 5.delet file\n 6.stop programme\n")
   
    d=int(input(""))
    a=d
    match a:
        case 1:
            print("CREATING FILE\n")
            print("......................................................................")
            print("enter your file name:\n")
            f=input("")
            h=f+'.txt'
            with open(h, 'w') as file:
               print(f, " file is created sucessfully....")
            print("......................................................................")
            fun()
        case 2:
            print("ENTER THE  FILE NAME \n")
            print("......................................................................")
            f=input("")
            with open(f+'.txt', 'r') as file:
                  print(file. read())
            fun()
        case 3:
             print("ENTER THE  FILE NAME \n")
             print("......................................................................")
             f=input("")
             with open(f+'.txt', 'a') as file:
                 app=input('enter the content to add :')
                 file.write(app)
             print("......................................................................")
             print("entered content is added successfully")     
             fun()
        case 4:
            print("listing all files")
            print("......................................................................")
            path= 'D:\manohar 1sem bca'
            file=os.listdir(path)
            for file in file:
                print(file)
            print(".......................................................................")
            print("listing ened")
            print("......................................................................")
            fun()
        case 5: 
            print("ENTER THE  FILE NAME to delete\n")
            print("......................................................................")
            f=input("")
            file=os.remove(f+'.txt')
            print(".......................................................................")
            print("file deleted ")
            print("......................................................................")
            fun()
        case 6:
             print("......................................................................")
             print("end programm")
             print("......................................................................")
             sys.exit(0)
             

            
