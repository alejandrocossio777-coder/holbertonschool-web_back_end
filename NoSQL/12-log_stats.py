#!/usr/bin/env python3
""" Log stats """
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    db = client.logs
    collection = db.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(collection.count()))
    print("Methods:")

    for method in methods:
        print("\tmethod {}: {}".format(
            method, collection.count({"method": method})
        ))

    status = collection.count({"method": "GET", "path": "/status"})
    print("{} status check".format(status))

