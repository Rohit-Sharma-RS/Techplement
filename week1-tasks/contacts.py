import json
import os

DATA_FILE = "contacts.json"

def load_contacts():
    """
    Loads contacts from the JSON file if it exists.
    
    Returns:
        Dictionary: A dictionary of contacts. Returns an empty dictionary if the file 
              doesn't exist or if an error occurs while loading.
    """
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        return {}
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading contacts: {e}")
        return {}

def save_contacts(contacts):
    """
    Saves the contacts dictionary to a JSON file.
    
    Parameters:
        contacts: A dictionary of contact information to be saved.
    """
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(contacts, f, indent=4)
    except IOError as e:
        print(f"Error saving contacts: {e}")

def add_contact(contacts):
    """
    Adds a new contact to the contacts dictionary.
    
    Parameters:
        contacts: The current dictionary of contacts to which the new 
                         contact will be added.
    """
    try:
        name = input("Enter contact name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        
        phone = input("Enter contact phone number: ").strip()
        if not phone.isdigit():
            raise ValueError("Phone number must contain only digits.")
        
        email = input("Enter contact email: ").strip()
        if "@" not in email or "." not in email:
            raise ValueError("Invalid email format.")
        
        contacts[name] = {"phone": phone, "email": email}
        print(f"Contact {name} added successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def search_contact(contacts):
    """
    Searches for a contact by name in the contacts dictionary...
    
    Parameters:
        contacts: The dictionary containing all contacts.
    """
    try:
        name = input("Enter name to search: ").strip()
        if not name:
            raise ValueError("Search name cannot be empty.")
        
        if name in contacts:
            print(f"Name: {name}")
            print(f"Phone: {contacts[name]['phone']}")
            print(f"Email: {contacts[name]['email']}")
        else:
            print("Contact not found.")
    except ValueError as e:
        print(f"Error: {e}")

def update_contact(contacts):
    """
    Updates an existing contact's phone number or email...
    
    Parameters:
        contacts : The current dictionary of contacts where updates will be made.
    """
    try:
        name = input("Enter name of contact to update: ").strip()
        if name not in contacts:
            print("Contact not found.")
            return
        
        print("Leave fields blank to keep current values.")
        new_phone = input("Enter new phone number: ").strip()
        new_email = input("Enter new email: ").strip()
        
        if new_phone:
            if not new_phone.isdigit():
                raise ValueError("Phone number must contain only digits.")
            contacts[name]["phone"] = new_phone
        
        if new_email:
            if "@" not in new_email or "." not in new_email:
                raise ValueError("Invalid email format.")
            contacts[name]["email"] = new_email
        
        print(f"Contact {name} updated successfully!")
    except ValueError as e:
        print(f"Error: {e}")

def view_contacts(contacts):
    """
    Displays all contacts in the dictionary...
    
    Parameters:
        contacts : The dictionary containing all contact information.
    """
    try:
        if not contacts:
            print("No contacts available.")
            return
        
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    except Exception as e:
        print(f"Error viewing contacts: {e}")

def main():
    contacts = load_contacts()
    
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. View All Contacts")
        print("5. Exit")
        
        try:
            choice = int(input("Choose an option (1-5): "))
            if choice == 1:
                add_contact(contacts)
                save_contacts(contacts)
            elif choice == 2:
                search_contact(contacts)
            elif choice == 3:
                update_contact(contacts)
                save_contacts(contacts)
            elif choice == 4:
                view_contacts(contacts)
            elif choice == 5:
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
