from pymongo import MongoClient
import json
from dataclasses import dataclass
from config import uri
import datetime
#import pandas as pd

@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: list
    preferences: UserPreferences
    created_ts: float
    active: bool

    def to_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "roles": self.roles,
            "preferences": self.preferences.__dict__, 
            "active": self.active,
            "created_ts": self.created_ts,
        }

def get_db(uri):
    client = MongoClient(uri)
    return client['udata']

def parse_user(user_data):
    roles = []
    for key, value in user_data.items():
        if key.startswith("is_user_") and key.endswith(("admin", "manager", "tester")):
            role = key.split("_")[-1]
            if value:
                roles.append(role)

    preferences = UserPreferences(timezone=user_data["user_timezone"])
    user_object = User(
        username=user_data["user"],
        password=user_data["password"],
        roles=roles,
        preferences=preferences,
        created_ts=datetime.datetime.strptime(user_data["created_at"], "%Y-%m-%dT%H:%M:%SZ").timestamp(),
        active=user_data["is_user_active"],
    )

    return user_object.to_dict()

def main():
    database = get_db(uri)
    collection = database['udata_collection']

    with open('udata.json', 'r') as file:
        json_data = json.load(file)

    users = json_data["users"]

    documents = [parse_user(user) for user in users]
    results = collection.insert_many(documents)

    print(f"Successfully inserted {len(results.inserted_ids)} documents.")

if __name__ == "__main__":
    main()