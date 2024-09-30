def input_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def choose_operation():
    print("Choose an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = input("Enter your choice (1-4): ")
    return choice

def perform_operation(num1, num2, operation):
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

def calculator():
    print("Start")
    
    num1, num2 = input_numbers()
    
    operation = choose_operation()
    
    result = perform_operation(num1, num2, operation)
    
    print(f"Result: {result}")
    
    print("End")

if __name__ == "__main__":
    calculator()
