def fibonacci_generator():
    """
    A generator function that yields the Fibonacci sequence.

    Yields:
        int: The next number in the Fibonacci sequence.
        

    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_fibonacci_numbers():       
    """
    Generates Fibonacci numbers based on user input.

    This function creates an instance of the Fibonacci generator and prompts the user
    to determine whether they want the next Fibonacci number. It continues generating
    Fibonacci numbers until the user chooses to exit.

    Returns:
        None
    """
    fib_gen = fibonacci_generator()  # Create an instance of the Fibonacci generator
    while True:
        # Ask user if they want the next Fibonacci number
        user_response = input("Would you like the next Fibonacci number? (yes/no): ")
        if user_response.lower() in ['yes', 'y']:
            print(f"The next Fibonacci number is {next(fib_gen)}")
        elif user_response.lower() in ['no', 'n']:
            print("Exiting the Fibonacci sequence generator.")
            break
        else:
            print("Invalid response, please answer with 'yes' or 'no'.")

# To run the user interaction function
get_fibonacci_numbers()