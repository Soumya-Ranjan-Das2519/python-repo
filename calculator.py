print('''+ ADD
      - SUBSTRACT
      * MULTIPLICATION
      / DIVISION
      % MODULOUS''')
num1=eval(input("enter the value1:"))
num2=eval(input("enter the value2:"))
opr=input("enter the operation..>")
if opr=="+":
    print(num1+num2)
elif opr=="-":
    print(num1-num2)
elif opr=="*":
    print(num1*num2)
elif opr=="/":
    print(num1/num2)
elif opr=="%":
    print(num1*num2/100)
else:
    print("invalid Opr....")     


