print("Calculator")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")
ch=int(input("Enter choice(1-4):"))
if ch==1:
       a=int(input("Enter A:"))
       b=int(input("Enter B:")) 
       c=a+b
       print("Sum=",c)
elif ch==2:
       a=int(input("Enter A:"))
       b=int(input("Enter B:"))  
       c=a-b
       print("Difference=",c)
elif ch==3:
       a=int(input("Enter A:"))
       b=int(input("Enter B:"))  
       c=a*b
       print("Product=",c)
elif ch==4:
       a=int(input("Enter A:"))
       b=int(input("Enter B:"))  
       c=a/b
       print("Division=",c)
else:
    print("Invalid Choice")
       