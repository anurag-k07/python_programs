user_database = {}
administrator_database = {}

def register_user(user_type, name, details):
    if user_type == "user":
        user_database[name] = details
        return f"User '{name}' registered successfully."
    elif user_type == "administrator":
        administrator_database[name] = details
        return f"Administrator '{name}' registered successfully."
    else:
        return "Error: Invalid user type. Use 'user' or 'administrator'."

def update_account(user_type, name, new_details):
    if user_type == "user":
        if name in user_database:
            user_database[name] = new_details
            return f"User '{name}' updated successfully."
        else:
            return f"Error: User '{name}' not found."
    elif user_type == "administrator":
        if name in administrator_database:
            administrator_database[name] = new_details
            return f"Administrator '{name}' updated successfully."
        else:
            return f"Error: Administrator '{name}' not found."
    else:
        return "Error: Invalid user type. Use 'user' or 'administrator'."

def show_registered():
    return {
        "users": user_database,
        "administrators": administrator_database
    }

if __name__ == "__main__":
    # Example usage
    print(register_user("user", "Alice", {"email": "alice@example.com", "phone": "123-456-7890"}))
    print(register_user("administrator", "Bob", {"email": "bob@example.com", "phone": "987-654-3210"}))

    print(update_account("user", "Alice", {"email": "alice_new@example.com", "phone": "111-222-3333"}))
    print(update_account("administrator", "Bob", {"email": "bob_new@example.com", "phone": "999-888-7777"}))

    print("Registered Users and Administrators:")
    print(show_registered())
