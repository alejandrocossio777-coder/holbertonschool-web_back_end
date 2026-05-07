#!/usr/bin/env python3
"""
Script that provides stats about Nginx logs stored in MongoDB
"""

from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx

    # Total number of logs
    total_logs = collection.count()
    print(f"{total_logs} logs")

    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.find({"method": method}).count()
        print(f"\tmethod {method}: {count}")

    # Status check: GET /status
    status_check = collection.find({
        "method": "GET",
        "path": "/status"
    }).count()
    print(f"{status_check} status check")
