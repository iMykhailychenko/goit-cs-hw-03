from beaupy import select
from dotenv import dotenv_values
from pymongo import MongoClient
from rich.console import Console

from app.models import DBError
from app.repositories import CatsRepository
from app.services import (
    add_features,
    delete_all,
    delete_by_name,
    find_by_name,
    new_record,
    read_all,
    update_age,
)

console = Console()
config = dotenv_values(".env")


def connect():
    return MongoClient(config["MONGO_URI"])["cs_hw3"]


actions = [
    "View all recors",
    "Add new record",
    "Find by name",
    "Update age",
    "Add more features",
    "Remove by name",
    "Remove all",
    "Exit",
]

EXIT_CODE = "exit"

handlers_map = {
    actions[0]: read_all,
    actions[1]: new_record,
    actions[2]: find_by_name,
    actions[3]: update_age,
    actions[4]: add_features,
    actions[5]: delete_by_name,
    actions[6]: delete_all,
    actions[7]: lambda _: EXIT_CODE,
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
