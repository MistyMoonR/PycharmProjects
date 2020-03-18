password_list = ["pan", "123"]
def login():
    password = input("Give me your password: ")
    if(password in password_list):
        return True
    else:
        counter = 1
        while(counter < 4):
            password = input("Your password is not right, try again and you are trying {} times ".format(counter))
            if(password in password_list):
                return True
            counter += 1
        return False

result = login()
if(result):
    print("Login successfully!")
else:
    print("Fail")

password_list = ["pan","123"]
def login():
    password = input("Give me your password:")
    if(password in password_list):
        return True
    else:
        counter=1
        while(counter<4):
            password = input("Your password is not right, try again and you are trying {} times".format(counter))
            if(password in password_list):
                reture True
            counter += 1
        return False
    result = login()
    if(result):
        print("Login succesfully!")
    else:
        print("Faill")



