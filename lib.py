class Event:
    def __init__(self, event_date: str, event_type: str, machine_name: str, user: str) -> None:
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


if __name__ == "__main__":
    print("The file isn't supposed to be executed directly. It containes library classes.")
