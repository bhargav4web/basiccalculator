def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def multiply(a,b):
	return a*b
def division(a,b):
	return a/b
def remainder(a,b):
	return a%b

print("select operatioin")
print("1.add")
print("2.sub")
print("3.multiply")
print("4.division")
print("5.remainder")

choice=input("enter choice(1/2/3/4):")

num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))


if choice=='1':
	print(num1,"+",num2,"=",add(num1,num2))
elif choice=='2':
	print(num1,"-",num2,"=",sub(num1,num2))
elif choice=='3':
	print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='4':
	print(num1,"/",num2,"=",division(num1,num2))
elif choice=='5':
	print(num1,"%",num2,"=",remainder(num1,num2))
else:
	print("invalid input")

