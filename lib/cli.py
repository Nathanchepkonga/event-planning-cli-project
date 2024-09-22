from db.models import Event, session, Guest, Expense


def display_menu():
    print("1. Create Event")
    print("2. View All Events")
    print("3. Add Guest to Event")
    print("4. Add Expense to Event")
    print("5. Exit")

def create_event():
    name = input("Enter event name: ")
    location = input("Enter event location: ")
    event = Event(name=name, location=location)
    session.add(event)
    session.commit()
    print(f"Event '{name}' created.")

def view_all_events():
    events = session.query(Event).all()
    for event in events:
        print(f"ID: {event.id}, Name: {event.name}, Location: {event.location}")

def add_guest_to_event():
    event_id = int(input("Enter event ID: "))
    name = input("Enter guest name: ")
    guest = Guest(name=name, event_id=event_id)
    session.add(guest)
    session.commit()
    print(f"Guest '{name}' added to event ID {event_id}.")

def add_expense_to_event():
    event_id = int(input("Enter event ID: "))
    description = input("Enter expense description: ")
    amount = float(input("Enter expense amount: "))
    expense = Expense(description=description, amount=amount, event_id=event_id)
    session.add(expense)
    session.commit()
    print(f"Expense '{description}' of {amount} added to event ID {event_id}.")

def run():
    while True:
        display_menu()
        choice = input("Choose an option: ")

        if choice == '1':
            create_event()
        elif choice == '2':
            view_all_events()
        elif choice == '3':
            add_guest_to_event()
        elif choice == '4':
            add_expense_to_event()
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    run()
