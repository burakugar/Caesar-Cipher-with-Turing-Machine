from console_client import add_unary,substract_unary

print("Choose the section: ")
print("Add Binary: 1")
print("Subtract Binary: 2")

var= input()

if var=='1':
    add_unary()
else:
    substract_unary()