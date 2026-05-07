#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{collection.count_documents({})} logs")
    print("Methods:")

    for method in methods:
        print(f"\tmethod {method}: {collection.count_documents({'method': method})}")

    status = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f"{status} status check")
