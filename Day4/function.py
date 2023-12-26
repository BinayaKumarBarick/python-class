def get_integer_list():
    my_list = []
    num_elements = int(input("Enter the number of elements: "))
    for _ in range(num_elements):
        try:
            value = int(input("Enter an integer: "))
            my_list.append(value)
        except ValueError:
            print("Invalid input. Please enter an integer.")
    return my_list

def perform_operation(my_list, operation):
    if operation == "add":
        result = sum(my_list)
    elif operation == "subtract":
        result = my_list[0] - sum(my_list[1:])
    elif operation == "divide":
        result = my_list[0]
        for num in my_list[1:]:
            result /= num
    elif operation == "multiply":
        result = 1
        for num in my_list:
            result *= num
    elif operation == "floor divide":
        result = my_list[0]
        for num in my_list[1:]:
            result //= num
    else:
        print("Invalid operation choice. Please choose from add/subtract/divide/multiply/floor divide.")
        result = None
    return result

# Example usage:
my_list = get_integer_list()
operation_choice = input("Enter the operation (add/subtract/divide/multiply/floor divide): ")
result = perform_operation(my_list, operation_choice)
if result is not None:
    print(f"Result of {operation_choice}: {result}")
