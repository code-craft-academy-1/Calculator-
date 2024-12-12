import math

def advanced_calculator():
    print("Advanced Calculator")
    print("Available operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (**)")
    print("6. Square root (sqrt)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")

    while True:
        operation = input("\nEnter the operation (or 'exit' to quit): ").lower()

        if operation == 'exit':
            print("Exiting the calculator. Goodbye!")
            break

        if operation in ['+', '-', '*', '/', '**']:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("Error: Division by zero is not allowed.")
                        continue
                    result = num1 / num2
                elif operation == '**':
                    result = num1 ** num2

                print(f"Result: {result}")

            except ValueError:
                print("Invalid input. Please enter numeric values.")
        
        elif operation == 'sqrt':
            try:
                num = float(input("Enter a number: "))
                if num < 0:
                    print("Error: Cannot calculate the square root of a negative number.")
                    continue
                result = math.sqrt(num)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif operation in ['sin', 'cos', 'tan']:
            try:
                angle = float(input("Enter the angle in degrees: "))
                radians = math.radians(angle)
                if operation == 'sin':
                    result = math.sin(radians)
                elif operation == 'cos':
                    result = math.cos(radians)
                elif operation == 'tan':
                    result = math.tan(radians)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        elif operation == 'log':
            try:
                num = float(input("Enter a number: "))
                if num <= 0:
                    print("Error: Logarithm is only defined for positive numbers.")
                    continue
                result = math.log(num)
                print(f"Result: {result}")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        else:
            print("Invalid operation. Please try again.")

# Run the calculator
advanced_calculator()
