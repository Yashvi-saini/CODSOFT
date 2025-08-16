import random
num={"rock":1 ,"paper": -1,"scissor":0,"scissors":0}
str={1:"rock",-1:"paper",0:"scissor"}
while(1):
    computer=random.choice([-1,1,0])
    user=input("enter your choice from rock ,paper or scissors").strip().lower()
    num={"rock":1 ,"paper": -1,"scissor":0,"scissors":0}
    str={1:"rock",-1:"paper",0:"scissor"}
    print(f"computer chose {str[computer]} and user chose {user}")
    if(user in num):
        if(computer==num[user]):
            print("TIE")
        else:
            if(((computer==1) and (num[user]==-1)) or ((computer==-1) and (num[user]==0))or((computer==0) and (num[user]==1))):
                print("you won!")
            else:
                print("you lose")
        choice=input("want to play again?\n enter yes or no").strip().lower()
        if(choice!="yes"):
           break  
    else:
        print("invalid choice")
    
