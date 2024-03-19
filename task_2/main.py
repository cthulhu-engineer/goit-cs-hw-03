from pymongo import MongoClient
from pymongo.errors import PyMongoError

# Підключення до MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["cats_db"]
collection = db["cats"]


# Функції CRUD

def create_cat(cat_data):
    try:
        collection.insert_one(cat_data)
        print("Cat added successfully.")
    except PyMongoError as e:
        print(f"Error adding cat: {e}")


def read_all_cats():
    try:
        cats = collection.find()
        for cat in cats:
            print(cat)
    except PyMongoError as e:
        print(f"Error reading cats: {e}")


def read_cat_by_name(name):
    try:
        cat = collection.find_one({"name": name})
        if cat:
            print(cat)
        else:
            print("Cat not found.")
    except PyMongoError as e:
        print(f"Error finding cat: {e}")


def update_cat_age(name, new_age):
    try:
        result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
        if result.modified_count:
            print("Cat's age updated successfully.")
        else:
            print("No cat found with that name.")
    except PyMongoError as e:
        print(f"Error updating cat's age: {e}")


def add_feature_to_cat(name, new_feature):
    try:
        result = collection.update_one({"name": name}, {"$addToSet": {"features": new_feature}})
        if result.modified_count:
            print("New feature added to cat successfully.")
        else:
            print("No cat found with that name.")
    except PyMongoError as e:
        print(f"Error adding feature to cat: {e}")


def delete_cat_by_name(name):
    try:
        result = collection.delete_one({"name": name})
        if result.deleted_count:
            print("Cat deleted successfully.")
        else:
            print("No cat found with that name.")
    except PyMongoError as e:
        print(f"Error deleting cat: {e}")


def delete_all_cats():
    try:
        collection.delete_many({})
        print("All cats deleted successfully.")
    except PyMongoError as e:
        print(f"Error deleting cats: {e}")


# Створення кота
create_cat({"name": "barsik", "age": 3, "features": ["ходить в капці", "дає себе гладити", "рудий"]})

# Читання всіх котів
read_all_cats()

# Читання кота за іменем
read_cat_by_name("barsik")

# Оновлення віку кота
update_cat_age("barsik", 4)

# Додавання нової характеристики коту
add_feature_to_cat("barsik", "любить спати на сонці")

# Видалення кота за іменем
delete_cat_by_name("barsik")

# Видалення всіх котів
delete_all_cats()
