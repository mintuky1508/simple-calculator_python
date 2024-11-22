print("what do you want,[ +, -, /, *]" )
choice=input("input your choise: ")
print(choice)

if choice == "+":
    num1=int(input("first number"))
    num2=int(input("sencond number"))
    print(num1+num2)

elif choice=="-":
    num1=int(input("first number"))
    num2=int(input("sencond number"))
    print(num1-num2)

elif choice=="/":
    num1=int(input("first number"))
    num2=int(input("sencond number"))
    print(num1/num2)

elif choice=="*":
    num1=int(input("first number"))
    num2=int(input("sencond number"))
    print(num1*num2)

else:
    print("invalid number")
