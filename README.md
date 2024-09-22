# Event Planning CLI

## Overview
The **Event Planning CLI** helps users to plan and manage events, guest lists, and track expenses with ease. Users can create events, add guests, and manage expenses using a simple Command Line Interface (CLI).

### Features:
- Create and view events.
- Manage guest lists for events.
- Add and list expenses for each event.
- CLI to interact with users.

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-username/event-planning-cli.git
    cd event-planning-cli
    ```

2. Install dependencies using `Pipenv`:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Initialize the database:
    ```bash
    python lib/db/seed.py
    ```

4. Run the application:
    ```bash
    python lib/cli.py
    ```

## Database Structure

- **Event**: Tracks event details such as name, date, and location.
- **Guest**: Contains information about guests, linked to events.
- **Expense**: Stores expenses related to each event.

### Event Table
- `id`: Integer (Primary Key)
- `name`: String
- `date`: String
- `location`: String

### Guest Table
- `id`: Integer (Primary Key)
- `name`: String
- `email`: String
- `event_id`: Foreign Key (Event ID)

### Expense Table
- `id`: Integer (Primary Key)
- `name`: String
- `amount`: Float
- `event_id`: Foreign Key (Event ID)

## Running Tests

