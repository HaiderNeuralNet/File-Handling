from pathlib import Path
import os

def readfiles():
    path=Path('')
    items=list(path.rglob(''))
    for i, item in enumerate(items):
        print(f'{i+1} : {item}')

def createfile():
    try:
        readfiles()
        name=input("Type the name of your File :-")
        p=Path(name)
        if not p.exists():
            with open(p,'w') as fs:
                data=input('What you want to write in this file ---')
                fs.write(data)

            print("File created sucessfully")

        else:
            print("This file is already Exist")
    except Exception as err:
        print(f"There an error occur in {err}")
        

        

def readfile():
    try:
        readfiles()
        name=input('What file you read ----')
        p=Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data=fs.read()
                
            print("Readed Sucessfully:")
            print(data)
        else:
            print('The file cannot created and its not exist:-')
            
    except Exception as err:
        print(f"There is an error occur in {err}")
        


def updatefile():
    try:
        readfiles()
        name=input("Tell me which file you want to update:-")
        p=Path(name)
        if p.exists() and p.is_file():
            print("||======================================================||")
            print("||   Press 1 for updating the name of file :-           ||")
            print("||   Press 2 for overwrite the data of your file :-     ||")
            print("||   Press 3 for appending extra content in your file :-||")
            print("||======================================================||")
            
            opt=int(input("Enter your option from (1-3):-"))
            
            if opt==1:
                name2=input("Tell me your new file name i can update it :-")
                p2=Path(name2)
                p.rename(p2)
                print("Rename your file Sucessfull :-")
                
                print(p2)
                
            if opt==2:
                with open(p,'w') as fs:
                    data=input("Tell me what you want to write  this is overwrite the data:-")
                    fs.write(data)
                    print("The data overwrite sucessfull :-")
                    print('Check your file',data)
                    
            if opt==3:
                with open(p,'a') as fs:
                    data=input("Tell what you want to append :-")
                    fs.write(" "+data)
                    print('context add sucessfully:')
                    print("check your file:-",data)
    except Exception as err:
        print(f"There is an error occur in {err}") 
        
              
def deletefile():
    try:
        readfiles()
        name=input("Enter file name that you want to delete:-")    
        p=Path(name) 
        if p.exists() and p.is_file():
            os.remove(name)
            print('File ',name,'is deleted sucessfully:-')
            
            
        else:
            print("no such file exist :-")
            
    except Exception as err:
        print(f"an error occur in  :{err}")
               









while True:
    os.system('cls' if os.name == 'nt' else 'clear')


    print("||============================================================||")
    print("||This is the file handling project for better understanding :||")
    print("||------------------------------------------------------------||")
    print('||                        CRUD operations :                   ||')
    print('||------------------------------------------------------------||')
    print("||                    Press 1 for creating file :-            ||")
    print("||                    Press 2 for Reading file  :-            ||")
    print("||                    Press 3 for Updating file :             ||")
    print("||                    Press 4 for Deleting file :-            ||")
    print("||============================================================||")


    check=int(input("Enter you choice from (1-4):-"))


    if check==1:
        createfile()
        input("\nPress Enter to return to menu...")

    elif check ==2:
        readfile()
        input("\nPress Enter to return to menu...")
        
    elif check ==3:
        updatefile()
        input("\nPress Enter to return to menu...")
    elif check==4:
        deletefile()
        input("\nPress Enter to return to menu...")
    




