import random as rn
def pas():
    char= "abcdefghijklmnopqrstuvwxyz`1234567890-=~!@#$%^&*()_+[]|:";'<>,.?/'
    length = int(input("enter the length: "))
    password =""
    for i in range(length):
        password += rn.choice(char)
    print(password)




    