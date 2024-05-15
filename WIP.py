from user_managment import *
while True:
    print("\n1. Sign Up \n2. Fill The Balance \n3.exit")
    choice = input("Enter Your Choice: ")

    if choice == "1":
        while True:
            account_number = input("Please Enter Your Account Number: ")
            if account_exist(account_number):
                print("You Have Already Signed Up. Please Try Again With Another Account Number!")
            elif not is_valid_account(account_number):
                print("Invalid Account Number, Please Try Again!")
            else:
                user_sign_up(account_number)
                break

    elif choice == "2":
        while True:
            Acc_num = input("Please Enter Your Account Number:")
            if account_exist(Acc_num):
                found_user = find_the_user(Acc_num)
            
                amount = input("Enter The Amount Of Money: ")
                if amount.isdigit():
                    found_user["balance"] = amount
                    print("Entered:", amount)
                    print(found_user)  
                    break
                else: 
                    print("Invalid amount. Please enter a valid number.")
            else:
                print("This Account does not exist, Try Again!")

    elif choice=='3':
        break
       



