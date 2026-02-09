b=(float(input("enter your number")))
a=(float(input("enter your number")))

operation=(input("choose your operator (+,-,*,/)"))
if operation == '+':
    print(a+b)
elif operation=='-':
    print(a-b)
elif operation=='*':
    print(a*b)
elif operation=='/':
    print(a/b)
else:
    print('pls enter your number')