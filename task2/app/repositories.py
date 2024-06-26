from bson import ObjectId

from app.models import DBError


class CatsRepository:
    def __init__(self, db):
        self.__collection = db["cats"]

    def create(self, values: dict):
        try:
            return self.__collection.insert_one(values)
        except Exception as e:
            raise DBError(e)

    def read(self):
        try:
            return list(self.__collection.find())
        except Exception as e:
            raise DBError(e)

    def find_by_name(self, name: str):
        try:
            return self.__collection.find_one({"name": name})
        except Exception as e:
            raise DBError(e)

    def update(self, id: str, values: dict):
        try:
            self.__collection.update_one({"_id": ObjectId(id)}, {"$set": values})
        except Exception as e:
            raise DBError(e)

    def update_by_name(self, name: str, values: dict):
        try:
            self.__collection.update_one({"name": name}, {"$set": values})
        except Exception as e:
            raise DBError(e)

    def delete(self, id: str):
        try:
            return self.__collection.delete_one({"_id": ObjectId(id)})
        except Exception as e:
            raise DBError(e)

    def delete_by_name(self, name: str):
        try:
            return self.__collection.delete_one({"name": name})
        except Exception as e:
            raise DBError(e)

    def delete_all(self):
        try:
            return self.__collection.delete_many({})
        except Exception as e:
            raise DBError(e)
