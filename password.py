import string 
import random

s1=list(string.ascii_lowercase)
s2=list(string.ascii_uppercase)
s3=list(string.digits)
s4=list(string.punctuation)


character_num=input('how many characters want for your password ? : ')

while True:
    try:
        character_num=int(character_num)
        if character_num <8:
            print('your password must at least 8 characterts')
            character_num=input("how many characters want for your password ? : ")
        else:
            break    
    except:  
        print('please enter numbers only ')
        character_num=input("enter number : ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)        

part1=round(character_num * (30/100))
part2=round(character_num * (20/100))

password=[]

for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part2):
    password.append(s3[i])
    password.append(s4[i]) 
  
password =''.join(password[0:])  
print(password) 