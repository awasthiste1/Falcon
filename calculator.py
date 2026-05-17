#!/usr/bin/env python3
"""
Simple Calculator Application
A basic command-line calculator that performs arithmetic operations.
"""

def add(x, y):
    """Add two numbers"""
    return x + y


def subtract(x, y):
    """Subtract two numbers"""
    return x - y


def multiply(x, y):
    """Multiply two numbers"""
    return x * y


def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y


def get_number(prompt):
    """Get a valid number from user input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Main calculator function"""
    print("\n" + "="*50)
    print("         SIMPLE CALCULATOR")
    print("="*50)
    
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        print("="*50)
        
        choice = input("\nEnter choice (1/2/3/4/5): ").strip()
        
        if choice == '5':
            print("\nThank you for using the calculator! Goodbye!")
            break
        
        if choice in ('1', '2', '3', '4'):
            num1 = get_number("Enter first number: ")
            num2 = get_number("Enter second number: ")
            
            if choice == '1':
                print(f"\n{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"\n{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"\n{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
        else:
            print("\nInvalid choice! Please select a valid operation.")


if __name__ == "__main__":
    main()
