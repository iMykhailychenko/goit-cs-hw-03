from beaupy import prompt, select

from app.models import CatModel
from app.repositories import CatsRepository


def retry(name: str, fn):
    print(f"No cat found with name {name} (Enter to go back)")

    options = ["Back", "Search more"]
    action = select(options, cursor="🢧", cursor_style="cyan")
    if action == "Search more":
        fn()
    return


def update_age(repo: CatsRepository):
    name = prompt("Name:", target_type=str)
    cat = repo.find_by_name(name)

    if not cat:
        return retry(name, lambda: delete_by_name(repo))

    age = prompt(f"Name: {name}\nAge:", target_type=int, initial_value=str(cat["age"]))
    repo.update_by_name(name, {"age": age})
    print(f"Age updated\n\n")


def delete_by_name(repo: CatsRepository):
    name = prompt("Name:", target_type=str)
    cat = repo.find_by_name(name)

    if not cat:
        return retry(name, lambda: delete_by_name(repo))

    repo.delete_by_name(name)
    print(f"Cat {name} removed\n\n")


def add_features(repo: CatsRepository):
    name = prompt("Name:", target_type=str)
    cat = repo.find_by_name(name)
    if not cat:
        return retry(name, lambda: add_features(repo))
    features = cat["features"]

    while True:
        feature = prompt(
            f"Name: {name}\nFeature (or Enter to skip): {features}",
            target_type=str,
        )
        if not feature:
            break
        features.append(feature)

    repo.update_by_name(name, {"features": features})
    print(f"Features updated\n\n")


def view_record(repo: CatsRepository, item: dict):
    options = ["Back", "Remove", "Update"]
    action = select(options, cursor="🢧", cursor_style="cyan")
    if action == "Remove":
        repo.delete(item["_id"])
    elif action == "Update":
        update_all(repo, item)


def find_by_name(repo: CatsRepository):
    name = prompt("Name:", target_type=str)
    cat = repo.find_by_name(name)

    if not cat:
        return retry(name, lambda: find_by_name(repo))

    print(f"Cat info:\n{cat['name']} - {cat['age']} - {cat['features']}\n\n")
    view_record(repo, cat)


def update_all(repo: CatsRepository, cat: dict):
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
    print(f"Cat {name} updated\n\n")


def read_all(repo: CatsRepository):
    cats = repo.read()
    options = ["Back"] + [
        f"{cat['name']} - {cat['age']} - {cat['features']}" for cat in cats
    ]
    index = select(options, cursor="🢧", cursor_style="cyan", return_index=True)

    if not index:
        return

    view_record(repo, cats[index - 1]["_id"])


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
    print(f"Cat {name} created\n\n")


def delete_all(repo: CatsRepository):
    repo.delete_all()
    print("All cats removed\n\n")
