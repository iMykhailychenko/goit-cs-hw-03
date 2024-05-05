from beaupy import select
from dotenv import dotenv_values
from pymongo import MongoClient
from rich.console import Console

from app.repositories import CatsRepository
from app.services import new_record, read_all
from app.models import DBError

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
        try:
            action = select(actions, cursor="🢧", cursor_style="cyan")
            if handlers_map[action](repo) == EXIT_CODE:
                print("Bye!")
                break
        except DBError as e:
            console.print(f"[red]DB Error: {e}[/red]")


if __name__ == "__main__":
    main()
