a=int(input("Enter First Number: "))
b=int(input("Enter Second Number: "))
c=int(input("Enter Third Number: "))
print("")

if a>=b and a>=c:
    print(a,"is the largest number.")
elif b>=c :
    print(b,"is the largest number.")
else:
    print("among",a,",",b,"and",c,)
    print(c,"is the largest number.")