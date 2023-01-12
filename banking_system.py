
import mysql.connector

#Checking for connection to database
try:
    mycon=mysql.connector.connect(
                                    host="localhost",
                                    user="root",
                                    password='vnyk@1964',
                                    database="banking"
                                )

    if mycon.is_connected()==True:
        print("Connection Successfull!!\n")

    mycon.autocommit=True
    cur=mycon.cursor()

    cur_user=None
    cur_user_pin=None
    cur_user_balance=None

    #Fucntion for log-in of user 
    def login():
        name=input("Enter your Name : ")
        pin=int(input("Enter your PIN : "))
        cur.execute("SELECT Name,PIN,Balance FROM clients_data WHERE Name='{}' AND PIN={}".format(name,pin))
        data=cur.fetchall()
        if data!=[]:
            print(data[0][0])
            if (data[0][0]==name) and (data[0][1]==pin):
                global cur_user,cur_user_balance
                cur_user=data[0][0]
                
                cur_user_balance=data[0][2]
                
                print("Current User :",cur_user)
                return 'Success'
                
        else:
            print("\nName or PIN entered is Wrong!")

    #MAIN CODE
    while True:
        print("""\n                        +*********************************************************+
                        |=============++ WELCOME TO BANKING SYSTEM ++=============| 
                        +*********************************************************+
                        |=========| 1. Open New Client Account         |==========|             
                        |=========| 2. Withdraw Money                  |==========|
                        |=========| 3. Deposit Money                   |==========|
                        |=========| 4. Check Details of Acoounts       |==========|
                        |=========| 5. Quit                            |==========|
                        +*********************************************************+
""")

        choice=int(input("\nEnter your Choice : "))

        #If Option 1 is Selected
        if choice == 1:
            print("\n\t\t===== New Account=====")

            while True:
                name=input("\nWrite Your Fullname : ")
                cur.execute("SELECT Name FROM clients_data WHERE name='{}'".format(name))
                name_data=cur.fetchall()
            
                if name_data!=[]:
                    print("\nAccount with same name already exists!")
                else:
                    break
            pin = int(input("Please Write a Pin to Secure your Account : "))
            
            while True:
                deposit=int(input("\nPlease Deposit Money(atleast Rs.2200) to Start an Account : "))
                if deposit<2200:
                    print("\nMinimum balance required to create acoount is Rs.2200!!")
                else:
                    break
            print("\nYour Acount has been created Successfully!!")
            cur.execute("INSERT INTO clients_data(Name,PIN,Balance) VALUE('{}',{},{})".format(name,pin,deposit))
        
        #If Option 2 is Selected
        elif choice == 2:
            print("\n\t\t===== Withdraw Money =====")
            if login()=='Success':
                print("\n***Your Current Balance : Rs.",cur_user_balance,"****")
                withdraw_amount=int(input("\nHow much Amount you want to withdraw? "))
                if withdraw_amount>cur_user_balance:
                    print("\nNot enough Money","You don't have enough money in your Account!!")
                else:
                    balance_left=cur_user_balance-withdraw_amount
                    cur.execute("UPDATE clients_data SET Balance={} WHERE Name='{}'".format(balance_left,cur_user))
                    print("\nMoney Withdrawn Successfully!!")
                    print("\nMoney withdrawn : Rs.",withdraw_amount)
                    print("Money Left in Account : Rs.",balance_left)
            
        #If Option 3 is Selected
        elif choice == 3:
            print("\n\t\t===== Deposit Money =====")
            if login()=='Success':
                while True:
                    print("\n***Your Current Balance :",cur_user_balance,"****")
                    deposit_money=int(input("\nHow much Amount you want to Deposit? "))
                    if deposit_money>100000:
                        print("\nYou can only Deposit Rs.1 Lakh in a Day!")
                    else:
                        break
                
                total_money=cur_user_balance+deposit_money
                cur.execute("UPDATE clients_data SET Balance={} WHERE Name='{}'".format(total_money,cur_user))
                print("\nMoney Deposited Successfully!!")
        
        #If Option 4 is Selected
        elif choice == 4:
            print("\n\t\t===== Check Details of Account =====")
            if login()=='Success':
                print("\n\tClient Name :",cur_user)
                print("\n\tBalance : Rs.",cur_user_balance)

        #If Option 5 is Selected
        elif choice == 5:
            print("\n\tThankyou!! Visit Again Soon ☺...")
            break

        else:
            print("\n\tPlease Select Correct Option mentioned above!!")


#If Connection Fails
except:
    print("\nUnable to Connect to Database\nPlease check Password")
