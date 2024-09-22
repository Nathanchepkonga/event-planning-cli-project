# cli.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lib.db.database import session, init_db
from lib.db.models import Event, Guest, Expense
from lib.helper import print_menu, get_user_choice, get_event_details, get_guest_details, get_expense_details, display_event, display_guest, display_expense

def main():
    init_db()  # Initialize the database

    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 1:
            # Create Event
            event_data = get_event_details()
            if event_data:
                new_event = Event(**event_data)
                session.add(new_event)
                session.commit()
                print(f"Event '{new_event.name}' created successfully!")
        
        elif choice == 2:
            # View All Events
            events = session.query(Event).all()
            for event in events:
                display_event(event)
        
        elif choice == 3:
            # Find Event by ID
            event_id = input("Enter event ID: ")
            event = session.query(Event).get(event_id)
            if event:
                display_event(event)
            else:
                print("Event not found.")
        
        elif choice == 4:
            # Delete Event
            event_id = input("Enter event ID to delete: ")
            event = session.query(Event).get(event_id)
            if event:
                session.delete(event)
                session.commit()
                print(f"Event '{event.name}' deleted successfully!")
            else:
                print("Event not found.")
        
        elif choice == 5:
            # Manage Guest List
            event_id = input("Enter event ID to manage guests: ")
            event = session.query(Event).get(event_id)
            if event:
                guest_data = get_guest_details()
                if guest_data:
                    new_guest = Guest(**guest_data, event=event)
                    session.add(new_guest)
                    session.commit()
                    print(f"Guest '{new_guest.name}' added to event '{event.name}'!")
            else:
                print("Event not found.")
        
        elif choice == 6:
            # Track Expenses
            event_id = input("Enter event ID to track expenses: ")
            event = session.query(Event).get(event_id)
            if event:
                expense_data = get_expense_details()
                if expense_data:
                    new_expense = Expense(**expense_data, event=event)
                    session.add(new_expense)
                    session.commit()
                    print(f"Expense '{new_expense.name}' added to event '{event.name}'!")
            else:
                print("Event not found.")
        
        elif choice == 7:
            # Exit
            print("Exiting the Event Planning CLI. Goodbye!")
            break

if __name__ == "__main__":
    main()
