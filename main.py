import os
from typing import List
TypeOfEmployee = ["Fulltime" , "Parttime"]
TypeOfSalary = ["Basic Salary", "Daily Wage"]
FINE = 40
POSSIBLE_DAYOFFS = 3


class Employee:
    basicSalary = 1500
    DailyWage = 25
    absent = 0
    present = 0
    
    def __init__(self, type, code, name, phonenumber, address, days, basicSalary):
        self.type = type
        self.code = code
        self.name = name
        self.phonenumber = phonenumber
        self.address = address
        if self.type == 0:
            self.absent = days 
            self.basicSalary = basicSalary
        else: 
            self.present = days 
            self.DailyWage = basicSalary

    def __str__(self):
        return "%s %s %s %s"%(self.code, self.name, self.phonenumber, self.address)


    def printinfo(self):
        print("=================================")
        print(TypeOfEmployee[self.type] + " Employee's Information: ")
        print("1. Code: ", self.code)
        print("2. Name: ", self.name)
        print("3. Phonenumber: ", self.phonenumber)
        print("4. Address: ", self.address)
        if self.type == 0:
            print("5. Absent: ", self.absent)
            print("6.", TypeOfSalary[self.type], self.basicSalary)
        if self.type == 1:
            print("5. Present: ", self.present)
            print("6.",TypeOfSalary[self.type], self.DailyWage)

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type
    
        if self.type == other.type == 0:
            return(int(self.basicSalary) < int(other.basicSalary))
        if self.type == other.type == 1:
            return(int(self.DailyWage) < int(other.DailyWage))
        
    def TakeHomePay(self):
        def Calculate():
            if self.type == 0:
                if int(self.absent) <= POSSIBLE_DAYOFFS: 
                    return int(self.basicSalary)
                else: 
                    return max(0, int(self.basicSalary) - int(self.absent)*FINE)
            if self.type == 1:
                return int(self.present) * int(self.DailyWage)
        print("Each employee haseach employee has",POSSIBLE_DAYOFFS, " days off per month")
        print("Employee: ", self.name)
        print("Type", TypeOfEmployee[self.type])
        print("Absent:", self.absent)
        print("Take Home Pay: ", Calculate())
        return 0

    def update(self):
        while True:
            print("CHOOSE ONE INFORMATION TO UPDATE")
            self.printinfo()
            print("Enter 0 to Return to Main Menu.")
            option = int(input("Enter your choice: "))
            if option == 0:
                break
            if option == 1:
                self.code = input("Enter new code: ")
            elif option == 2:
                self.name = input("Enter new name: ")
            elif option == 3:
                self.phonenumber = input("Enter new phonenumber: ")
            elif option == 4:
                self.address = input("Enter new address: ")
            elif option == 5:
                if self.type == 0:
                    self.absent = input("Enter new absent day(s): ")
                else: 
                    self.present = input("Enter new present day(s): ")
            elif option == 6: 
                if self.type == 0:
                    self.basicSalary = input("Enter new Basic Salary: ") 
                else:
                    self.DailyWage = input("Enter new Daily Wage: ")      
            else: print("PLEASE CHOOSE AGAIN")
            print("INFORMATION UPDATED")

            
    

ListOfEmployee = list()





def CreateMenu():
    print(""" 

        EMPLOYEE MANAGER APPLICATION

    CHOOSE YOUR OPTION:
        0. Clear Screen
        1. Add a new fulltime employee
        2. Add a new parttime employee
        3. Search an employee - based on the code user entered.
        4. Delete an employee - based on the code user entered.
        5. Edit an employee   - based on the code user entered.
        6. Print a list of employees in Ascending order of salary.
        7. Show Take-Home Pay.
        8. Exit the program.
    """)
    return 0




def AddEmployee(type):
    code = input("Enter employee's code: ")
    name = input("Enter employee's name: ")
    phonenumber = input("Enter employee's phonenumber ")
    address =  input("Enter employee's address ")
    if type == 0:
        absent = input("Enter employee's absent ")
        salary = input("Enter employee's basic salary: ")
    if type == 1:
        absent = input("Enter employee's present: ")
        salary = input("Enter employee's daily wage: '")
    ListOfEmployee.append(Employee(type, code, name, phonenumber, address, absent, salary))



def FoundEmployee(keycode):
    for employee in ListOfEmployee:
        if keycode == employee.code:
            return True
    print("CODE NOT FOUND!") 
    return False



def SearchEmployee():
    keycode = input("Enter employee's code: ")
    if FoundEmployee(keycode): pass 

    for employee in ListOfEmployee:
        if employee.code == keycode:
            employee.printinfo()


            
def DelEmployee():
    keycode = input("Enter employee's code: ")
    if FoundEmployee(keycode): pass 

    delEmployee = list()
    for index in range(int(len(ListOfEmployee))):
        if ListOfEmployee[index].code == keycode:
            delEmployee.append(index)        

    delEmployee.reverse() 
    for index in delEmployee:
        del ListOfEmployee[index]

    print("Employee with code", keycode, "deleted!")
    return 0



def printSortedEmployee():
    SortedListOfEmployee = sorted(ListOfEmployee)
    #SortedListOfEmployee.reverse()
    for employee in SortedListOfEmployee:
        employee.printinfo()



def EditEmployee():
    keycode = input("Enter employee's code: ")
    if FoundEmployee(keycode): pass 
    for employee in ListOfEmployee:
        if employee.code == keycode:
            employee.update()

def ShowTakeHomePay():
    keycode = input("Enter employee's code: ")
    if FoundEmployee(keycode): pass
    for employee in ListOfEmployee:
        if employee.code == keycode:
            employee.TakeHomePay()




def main():
    os.system("cls")
    while True:
        CreateMenu()
        option = int(input("Enter your choice: "))
        if option == 0:
            os.system('cls')
        if option == 1:
           AddEmployee(0)        
        if option == 2:
            AddEmployee(1)
        if option == 3:
            SearchEmployee()
        if option == 4:
            DelEmployee()
        if option == 5:
            EditEmployee()
        if option == 6:
            printSortedEmployee()           
        if option == 7:
            ShowTakeHomePay()
        if option == 8:
            break
    print("THANKS FOR USING THIS PROGRAM!")





def testData():
    fi = open("test.data", "r+") 
    content = fi.read()
    line = content.split("\n")
    for l in line:
        data = l.split()
        ListOfEmployee.append(Employee(0, data[0], data[1], data[2], data[3], data[4], data[5]))
        ListOfEmployee.append(Employee(1, str(-int(data[0])), data[1], data[2], data[3], data[4], data[5])) 
    
    fi.close()
    main()

testData()