DAA=float(input("Enter marks:"))
Devops=float(input("Enter marks:"))
IRS=float(input("Enter marks:"))
PPL=float(input("Enter marks:"))
CN=float(input("Enter marks:"))
total=(DAA+Devops+IRS+PPL+CN)
print("your marks in percentage is",total,%)
if total>90:
    print("grade:O")
elif total>80 and total<80:
    print("grade:A")
elif total>70 and total<80:
    print("grade:B")
else:
    print("grade:F")            