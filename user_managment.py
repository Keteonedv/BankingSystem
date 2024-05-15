users=[
    {"name": "Keti", "lastname": "Davitadze", "iban":"TB000", "balance": 0},
    {"name": "Elisabeth", "lastname": "Smith", "iban":"TB001", "balance": 0},
    {"name": "David", "lastname": "Aghmashenebeli", "iban":"TB002", "balance": 0}
]
transactions=[
    {'sender_iban': "TB000", 'reciver_iban': 'TB002', "amount": 200}
]



def account_exist(account_number):
    for user in users:
        if user["iban"] == account_number:
            return True
    return False


def user_sign_up (account_number):
      
    name=input("Enter Your Name: " ).title()
    lname=input("Enter Your Last Name: " ).title()
    new_user={"name":name, "lastname": lname,"iban":account_number, "balance": 0  }
    users.append(new_user)
    print("User signed up successfully!")
    
def find_the_user(acc_num):
    for user in users:
        if user["iban"]==acc_num:
            return user
    return None
        
def is_valid_account(acc_num):
    if len(acc_num) != 5:
        return False
    if acc_num[:2] != "TB":
        return False
    if not acc_num[2:].isdigit():
        return False
    return True
