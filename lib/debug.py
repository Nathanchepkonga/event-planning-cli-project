from db.models import Event, session, Guest, Expense



def debug():
    print("Creating sample data...")
    event1 = Event(name="Birthday Party", location="Central Park")
    guest1 = Guest(name="Alice", event=event1)
    expense1 = Expense(description="Decorations", amount=500, event=event1)
    session.add_all([event1, guest1, expense1])
    session.commit()
    print("Sample data created.")

if __name__ == "__main__":
    debug()
