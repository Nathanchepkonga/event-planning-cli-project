# helper.py

from datetime import datetime

def print_menu():
    print("\n--- Event Planning CLI ---")
    print("1. Create Event")
    print("2. View All Events")
    print("3. Find Event by ID")
    print("4. Delete Event")
    print("5. Manage Guest List")
    print("6. Track Expenses")
    print("7. Exit")

def get_user_choice():
    try:
        choice = int(input("Enter your choice: "))
        if choice not in range(1, 8):
            raise ValueError
        return choice
    except ValueError:
        print("Invalid choice. Please enter a number between 1 and 7.")
        return None

def get_event_details():
    name = input("Enter event name: ")
    location = input("Enter event location: ")
    description = input("Enter event description: ")
    date_str = input("Enter event date and time (YYYY-MM-DD HH:MM): ")
    try:
        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid date format. Please enter the date in the format YYYY-MM-DD HH:MM.")
        return None
    return {
        'name': name,
        'location': location,
        'description': description,
        'date': date
    }

def get_guest_details():
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    phone = input("Enter guest phone number: ")
    return {
        'name': name,
        'email': email,
        'phone': phone
    }

def get_expense_details():
    name = input("Enter expense name: ")
    amount = input("Enter expense amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return None
    return {
        'name': name,
        'amount': amount
    }

def display_event(event):
    print(f"\nEvent ID: {event.id}")
    print(f"Name: {event.name}")
    print(f"Location: {event.location}")
    print(f"Description: {event.description}")
    print(f"Date: {event.date}")

def display_guest(guest):
    print(f"\nGuest ID: {guest.id}")
    print(f"Name: {guest.name}")
    print(f"Email: {guest.email}")
    print(f"Phone: {guest.phone}")

def display_expense(expense):
    print(f"\nExpense ID: {expense.id}")
    print(f"Name: {expense.name}")
    print(f"Amount: ${expense.amount:.2f}")
