from beaupy import select
from dotenv import dotenv_values
from pymongo import MongoClient
from rich.console import Console

from app.repository import CatsRepository
from app.services import new_record, read_all

console = Console()
config = dotenv_values(".env")


def connect():
    return MongoClient(config["MONGO_URI"])["cs_hw3"]


actions = [
    "View all recors",
    "Add new record",
    "Exit",
]

EXIT_CODE = "exit"

handlers_map = {
    actions[0]: read_all,
    actions[1]: new_record,
    actions[2]: lambda _: EXIT_CODE,
}


def main():
    db = connect()
    repo = CatsRepository(db)

    while True:
        action = select(actions, cursor="🢧", cursor_style="cyan")
        if handlers_map[action](repo) == EXIT_CODE:
            print("Bye!")
            break


if __name__ == "__main__":
    main()
