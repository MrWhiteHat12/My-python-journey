number1 = input("what is the first number: ")
opperation = input("what is the operation(+-*/): ")
number2 = input("what is the second number: ")
sollution = ("error")
success = True
# This is a simple calculator that performs basic arithmetic operations
try:
    num1 = int(number1)
    num2 = int(number2)
except ValueError:
    print("opperation failed")
    success = False

if success:
    if opperation == ("+"):
        sollution = (int(number1)+int(number2))
    elif opperation == ("-"):
        sollution = (int(number1)-int(number2))
    elif opperation == ("/"):
        if number2 == 0:
            print("thats not going to work")
        sollution = (int(number1)/int(number2))
    elif opperation == ("*"):
        sollution = (int(number1)*int(number2))
    else:
        print("opperation failed")
        success = False

if success == True:
    print("sollution")
