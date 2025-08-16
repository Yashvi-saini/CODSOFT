a=float(input("enter the first number here"))
b=float(input("enter the second number here"))
valid_operands=["+","-","*","/"]
operand=input("enter your choice from (+,-,*,/)\n")
if(operand not in valid_operands):
    print("invalid operands entered")
else:
    if(operand=="+"):
        print(f"sum is{a+b}")
    elif(operand=="-"):
        print(f"subtraction is {a-b}")
    elif(operand=="*"):
        print(f"multiplication is {a*b}")
    else:#division case needs to be checked for denominator
        if(b==0):
            print("divisible by zero not possible!")
        else:
          print(f"division is {a/b}")
