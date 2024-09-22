from models import Event, Guest, Expense, session

def seed_data():
    event1 = Event(name="Wedding", location="Beach Resort")
    guest1 = Guest(name="John Doe", event=event1)
    expense1 = Expense(description="Catering", amount=1500.0, event=event1)

    session.add_all([event1, guest1, expense1])
    session.commit()
    print("Data seeded!")

if __name__ == "__main__":
    seed_data()
