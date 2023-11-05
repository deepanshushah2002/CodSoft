a = float(input("Enter a first number:- "))
b = float(input("Enter a second number:- "))
print("1. Subtraction(-)       2. Addition(+)\n3. Multiple(*)          4. Divide(/)")
c = int(input("Enter a operation in number:- "))
match c:
    case 1:
        sum = a-b
    case 2:
        sum = a+b
    case 3:
        sum = a*b
    case 4:
        sum = a/b
print("Your sum is :- " ,sum)