#Python program to calculate
#will input into the GUI later
#Addition
def add(x,y):
    return x+y

#Subtraction
def subtract(x,y):
    return x-y

#Multiplication
def multiply(x,y):
    return x*y

#Division  
def divide(x,y):
    return x/y

print("""Operations
      1. Addition
      2. Subtraction
      3. Multiplication
      4. Division
      """)  

choice = input("Enter your choice: ")

#INPUT
try:
    first_number = float(input("Enter first number: "))
    second_number = float(input("Enter second number: "))
except ValueError:
    print("Error: Invalid input. Please enter valid numbers.")
else:
    if choice == "1":
        print(add(first_number, second_number))
    elif choice == "2":
        print(subtract(first_number, second_number))
    elif choice == "3": 
        print(multiply(first_number, second_number))
    elif choice == "4":
        print(divide(first_number, second_number))
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

