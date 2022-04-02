from lib import Event
# from collections.abc import Sequence


def get_event_date(event: Event) -> str:
    return event.date


def current_users(events: list) -> dict:
    machines = {}

    events.sort(key=get_event_date)

    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()

        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)

    return machines


def generate_report(machines: dict, file=None) -> None:
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list), file=file)


if __name__ == "__main__":
    print("The file isn't supposed to be executed directly. It containes utility functions.")
