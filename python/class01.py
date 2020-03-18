print(True)
from random import  randint
num=randint(1,100)
print(num)

for i in range(0,3):
    for j in range(0,i+1):
        print("*"),
    print()


pound_input = input("Put a pound number:")
kg_number = float(pound_input)/2.2046
print("THe {} lb equals to {} kg".format(pound_input,str(kg_number)))


pound_input = input('hello')
kg_number = float(pound_input)/2
print('the {} lb equals to {} kg'.format(pound_input,str(kg_number)))


ask_sentence = "hello,{}!"
print("hello")
name=input("what is your name")
print(ask_sentence,format(name))

name="1391 231 0006"
print("********"+name[8:14])

def isequal(num1,num2):
    if num1<num2:
        print("too small")
        return False
    if num1>num2:
        print("too big")
        return False
    if num1==num2:
        print("bingo")
        return True

from random import randint
num=randint(1,10)
print ("guess what i think")
print ("1 2 3 4 5 6 7 8 9 10 11")
bingo=False
while bingo==False:
    answer=input()
    bingo=isequal(answer,num)
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
password_list2 = ['helloworld','HELLOWORLD']
 def login():
     password = input('Guess')
     if(password in password_list2):
         return True
     counter +=1
     while(counter<4)
         password = input('you not right,try again')
         if(password in password_list2):
             return True
         counter+=1
        return False

