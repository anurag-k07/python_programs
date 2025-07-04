"""login={}
u=int(input("Enter the no. of users you want to add:"))
for i in range(u):
    uname=input("Enter username:")
    password=input("Enter password:")
    print()
    login[uname]=password
uname_enter=input("Enter your username:")
pass_enter=input("Enter your password:")
if uname_enter in login:
    if login[uname_enter]==pass_enter:
        print("Login is succesful"
    else:print("Incorrect password")
else:print("Username not found")"""
from datetime import datetime

# Data structures for users and administrators
users = {}
administrators = {}

# Function to register a new user or administrator
def register_account(account_type, name, email):
    if account_type not in ["user", "administrator"]:
        return "Error: Invalid account type. Must be 'user' or 'administrator'."

    database = users if account_type == "user" else administrators

    if email in database:
        return f"Error: {account_type.capitalize()} with email '{email}' is already registered."

    database[email] = {"name": name, "email": email, "registered_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    return f"{account_type.capitalize()} '{name}' registered successfully."

# Function to update account information
def update_account(account_type, email, new_name=None, new_email=None):
    if account_type not in ["user", "administrator"]:
        return "Error: Invalid account type. Must be 'user' or 'administrator'."

    database = users if account_type == "user" else administrators

    if email not in database:
        return f"Error: {account_type.capitalize()} with email '{email}' not found."

    if new_name:
        database[email]["name"] = new_name
    if new_email:
        database[new_email] = database.pop(email)
        database[new_email]["email"] = new_email

    return f"{account_type.capitalize()} information updated successfully."

# Function to show registered accounts
def show_accounts():
    result = "Registered Users:\n"
    result += "\n".join([f"Name: {info['name']}, Email: {info['email']}" for info in users.values()])
    result += "\n\nRegistered Administrators:\n"
    result += "\n".join([f"Name: {info['name']}, Email: {info['email']}" for info in administrators.values()])
    return result

# Example usage
if __name__ == "__main__":
    # Register new users and administrators
    print(register_account("user", "Alice", "alice@example.com"))
    print(register_account("administrator", "Bob", "bob@example.com"))

    # Update account information
    print(update_account("user", "alice@example.com", new_name="Alice Smith"))
    print(update_account("administrator", "bob@example.com", new_email="bob_admin@example.com"))

    # Show all registered accounts
    print(show_accounts())