import logging
import os


logger = logging.getLogger('event_planning_debugger')


logger.setLevel(logging.DEBUG)


log_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'event_planning.log')
file_handler = logging.FileHandler(log_file)


console_handler = logging.StreamHandler()


file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(console_handler)


def log_event(event_name, event_info):
    """
    Log the details of an event being created, modified, or deleted.
    """
    logger.info(f"Event: {event_name} | Info: {event_info}")


def log_error(error_message):
    """
    Log any errors that occur during the event planning operations.
    """
    logger.error(f"Error: {error_message}")


if __name__ == "__main__":
    log_event("Wedding Reception", "Successfully created event with ID: 101")
    

    log_error("Failed to delete event with ID: 102 - Event not found")
