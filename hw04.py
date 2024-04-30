def parse_input(user_input) -> tuple:
    """Parses the user input and returns the command and arguments.

    Args:
        user_input (str): The user input to be parsed.

    Returns:
        tuple: A tuple containing the command (str) and arguments (list).

    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts) -> str:
    """Adds a new contact to the dictionary."""
    if len(args) != 2:
        return "Invalid command usage. Correct usage: add [name] [phone]"
    name, phone = args
    if name in contacts:
        return "Такий контакт вже є. Спробуйте інше ім'я."
    contacts[name] = phone
    return f"Contact {name} added with number {phone}."

def change_contact(args, contacts) -> str:
    """Changes an existing contact's phone number."""
    if len(args) != 2:
        return "Invalid command usage. Correct usage: change [name] [new_phone]"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return f"Contact {name} updated to new number {new_phone}."
    else:
        return "Contact not found."

def show_phone(args, contacts) -> str:
    """Shows a contact's phone number."""
    if len(args) != 1:
        return "Invalid command usage. Correct usage: phone [name]"
    name = args[0]
    if name in contacts:
        return f"{name}'s number is {contacts[name]}"
    else:
        return "Contact not found."

def show_all(contacts) -> str:
    """Displays all contacts."""
    if contacts:
        return '\n'.join(f"{name}: {phone}" for name, phone in contacts.items())
    else:
        return "No contacts saved."

def main():
    """
    The main function of the assistant bot program.
    
    This function initializes an empty dictionary to store contacts and then enters a loop to prompt the user for commands.
    The user can enter commands such as "hello", "add", "change", "phone", "all", "close", or "exit" to interact with the assistant bot.
    The function calls different helper functions based on the user's command and displays the corresponding output.
    The loop continues until the user enters "close" or "exit" to exit the program.
    """
    contacts = {} # Dictionary to store contacts
    print("Welcome. I am an assistant bot!")
    
    while True: # Main loop to interact with the user
        user_input = input("Enter a command: ") # Prompt the user for input
        if user_input.lower() in ["close", "exit"]: # Check if the user wants to exit
            print("Good bye!")
            break

        command, args = parse_input(user_input) # Parse the user input
        
        # Helper functions to handle different commands
        def switch_case(command):
            switcher = {
                "hello": "How can I help you?",
                "add": add_contact(args, contacts),
                "change": change_contact(args, contacts),
                "phone": show_phone(args, contacts),
                "all": show_all(contacts),
            }
            return switcher.get(command, "Invalid command. Available commands: hello, add, change, phone, all, close, exit")

        print(switch_case(command))

if __name__ == "__main__":
    main()
