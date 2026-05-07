#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


def _count(coll, query=None):
    """Count documents with compatibility across PyMongo versions."""
    if query is None:
        query = {}
    try:
        return coll.count_documents(query)
    except Exception:
        return coll.count(query)


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    print("{} logs".format(_count(collection)))
    print("Methods:")
    print("\tmethod GET: {}".format(_count(collection, {"method": "GET"})))
    print("\tmethod POST: {}".format(_count(collection, {"method": "POST"})))
    print("\tmethod PUT: {}".format(_count(collection, {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(_count(collection, {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(_count(collection, {"method": "DELETE"})))
    print("{} status check".format(
        _count(collection, {"method": "GET", "path": "/status"})
    ))
