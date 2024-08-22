#!/usr/bin/env python3
"""Python function that lists all documents
in a collection:"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The MongoDB collection object.

    Returns:
    list: A list of documents in the collection.
    Returns an empty list if no document is found.
    """
    if mongo_collection is None:
        return []

    documents = list(mongo_collection.find())

    return documents
