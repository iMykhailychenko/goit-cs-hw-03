from bson import ObjectId


class CatsRepository:
    def __init__(self, db):
        self.__collection = db["cats"]

    def create(self, values: dict):
        return self.__collection.insert_one(values)

    def read(self):
        return list(self.__collection.find())

    def update(self, id: str, values: dict):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": values})

    def delete(self, id: str):
        return self.__collection.delete_one({"_id": ObjectId(id)})
