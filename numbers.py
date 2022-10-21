def sum():
    num1 = int(input("First number:"))
    num2 = int(input("Second number:"))
    return num1+num2

def subtract():
    num1 = int(input("First number:"))
    num2 = int(input("Second number:"))
    return num1-num2

def main():
    total = sum()
    print("The sum is:", total)
    sub = subtract()
    print("The subtraction is:", sub)