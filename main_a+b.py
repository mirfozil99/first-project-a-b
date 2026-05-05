a=int(input("give number to a = "))
b=int(input("give number to b = "))
c=str(input("give operation (+,-,*,/)"))
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    if b!=0 or a!=0:
        print(a/b)
else:
    print("yobnulsya shtoli")
