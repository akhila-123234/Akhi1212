DAA=float(input("Enter marks:"))
Devops=float(input("Enter marks:"))
IRS=float(input("Enter marks:"))
PPL=float(input("Enter marks:"))
CN=float(input("Enter marks:"))
total=(DAA+Devops+IRS+PPL+CN)
percentage=(total/500)*100
print("your marks in percentage is",percentage)
if percentage>90:
    print("grade:O")
elif percentage>80 and percentage<80:
    print("grade:A")
elif percentage>70 and percentage<80:
    print("grade:B")
else:
    print("grade:F")            
