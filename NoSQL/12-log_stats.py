#!/usr/bin/env python3
""" 12-log_stats """
from pymongo import MongoClient


def count_docs(collection, query=None):
    """Count documents with backward compatibility."""
    if query is None:
        query = {}
    try:
        return collection.count_documents(query)
    except Exception:
        return collection.count(query)


if __name__ == "__main__":
    client = MongoClient()
    collection = client.logs.nginx

    print("{} logs".format(count_docs(collection)))
    print("Methods:")
    print("\tmethod GET: {}".format(
        count_docs(collection, {"method": "GET"})))
    print("\tmethod POST: {}".format(
        count_docs(collection, {"method": "POST"})))
    print("\tmethod PUT: {}".format(
        count_docs(collection, {"method": "PUT"})))
    print("\tmethod PATCH: {}".format(
        count_docs(collection, {"method": "PATCH"})))
    print("\tmethod DELETE: {}".format(
        count_docs(collection, {"method": "DELETE"})))
    print("{} status check".format(
        count_docs(collection, {"method": "GET", "path": "/status"})
    ))
