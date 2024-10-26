from typing import Tuple, List, Dict


def parse_input(user_input: str) -> Tuple[str, List[str]]:
    """
    Parses user input into a command and arguments.

    Args:
        user_input (str): Input string from the user.

    Returns:
        tuple: Command and list of arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Adds a new contact to the contacts dictionary.

    Args:
        args (list): List containing name and phone number.
        contacts (dict): Dictionary to store contacts.

    Returns:
        str: Confirmation message or error message if arguments are missing.
    """
    if len(args) != 2:
        return "Error: Command format is 'add [name] [phone]'"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Changes the phone number for an existing contact.

    Args:
        args (list): List containing name and new phone number.
        contacts (dict): Dictionary storing contacts.

    Returns:
        str: Confirmation message if contact updated or error message if contact not found.
    """
    if len(args) != 2:
        return "Error: Command format is 'change [name] [new_phone]'"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Error: Contact not found."


def show_phone(args: List[str], contacts: Dict[str, str]) -> str:
    """
    Shows the phone number for a specified contact.

    Args:
        args (list): List containing the name.
        contacts (dict): Dictionary storing contacts.

    Returns:
        str: Phone number or error message if contact not found.
    """
    if len(args) != 1:
        return "Error: Command format is 'phone [name]'"
    name = args[0]
    if name in contacts:
        return f"{name}: {contacts[name]}"
    else:
        return "Error: Contact not found."


def show_all(contacts: Dict[str, str]) -> str:
    """
    Shows all contacts in the contacts dictionary.

    Args:
        contacts (dict): Dictionary storing contacts.

    Returns:
        str: List of all contacts and their phone numbers or message if no contacts.
    """
    if not contacts:
        return "No contacts available."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def show_help() -> str:
    """
    Returns a string with a list of available commands and their descriptions.

    Returns:
        str: List of commands with descriptions.
    """
    return """
Available commands:
- hello: Greet the bot
- add [name] [phone]: Add a new contact
- change [name] [new_phone]: Change an existing contact's phone number
- phone [name]: Show the phone number of a contact
- all: Show all contacts
- help: Show this help message
- close, exit: Exit the bot
"""


def main() -> None:
    """
    Main function to interact with the user in a command loop.
    """
    contacts: Dict[str, str] = {}
    print("Welcome to the assistant bot!")
    print(show_help())  # Show help at the start

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command. Please use one of the following commands:")
            print(show_help())


if __name__ == "__main__":
    main()
