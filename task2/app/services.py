from beaupy import prompt, select

from app.models import CatModel
from app.repository import CatsRepository


def update_record(repo: CatsRepository, cat: dict):
    name = prompt("Name:", target_type=str, initial_value=cat["name"])
    age = prompt(f"Name: {name}\nAge:", target_type=int, initial_value=str(cat["age"]))
    features = cat["features"]

    while True:
        feature = prompt(
            f"Name: {name}\nAge: {age}\nFeature (or Enter to skip): {features}",
            target_type=str,
        )
        if not feature:
            break
        features.append(feature)

    record = CatModel(name=name, age=age, features=features)
    repo.update(cat["_id"], record.model_dump())


def read_all(repo: CatsRepository):
    cats = repo.read()
    options = ["Back"] + [
        f"{cat['name']} - {cat['age']} - {cat['features']}" for cat in cats
    ]

    index = select(options, cursor="🢧", cursor_style="cyan", return_index=True)
    if not index:
        return

    action = select(["Back", "Remove", "Update"], cursor="🢧", cursor_style="cyan")
    if action == "Remove":
        repo.delete(cats[index - 1]["_id"])
    elif action == "Update":
        update_record(repo, cats[index - 1])


def new_record(repo: CatsRepository):
    name = prompt("Name:", target_type=str)
    age = prompt(f"Name: {name}\nAge:", target_type=int)
    features = []

    while True:
        feature = prompt(
            f"Name: {name}\nAge: {age}\nFeature (or Enter to skip): {features}",
            target_type=str,
        )
        if not feature:
            break
        features.append(feature)

    record = CatModel(name=name, age=age, features=features)
    repo.create(record.model_dump())
