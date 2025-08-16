import random
import string
#level 1 : using alphabetsonly
#level 2 : using combo of alaphabets and digits
#level 3 : using combo of alpha + digits + speacial char
length=int(input("enter the length of pass you want\n"))
level=input("enter difficulty level i.e choose (easy,medium,hard)\n").strip().lower()
input_dict={"easy":1,"medium":2,"hard":3}
choice=input_dict[level]
#length and complexity taken
if(choice==1):
    pswrd=string.ascii_letters
elif(choice==2):
    pswrd=alpha=string.ascii_letters + string.digits
else:
    pswrd=alpha=string.ascii_letters + string.digits + string.punctuation
password="".join(random.choice(pswrd) for _ in range(length))
print(f"password generated as per your entered choice is: {password}")

