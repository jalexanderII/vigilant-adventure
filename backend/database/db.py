import os

import motor.motor_asyncio
from dotenv import load_dotenv
from pymongo.collection import Collection


def initiate_mongo_client() -> Collection:
    load_dotenv()
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGOURI"])
    db = client[os.getenv("PLANNING_DB_NAME")]
    return db[os.getenv("PLANNING_COLLECTION")]
