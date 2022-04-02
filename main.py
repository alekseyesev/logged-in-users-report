from mock_events import events
from utils import current_users, generate_report

if __name__ == "__main__":
    users = current_users(events)

    generate_report(users)
else:
    print("The file isn't supposed to be imported as module.")
