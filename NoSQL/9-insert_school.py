#!/usr/bin/env python3
"""Python function that inserts a new document
in a collection based on kwargs."""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into the MongoDB
    collection based on provided kwargs.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The MongoDB collection object.
    **kwargs: Arbitrary keyword arguments representing
    the document fields and values.

    Returns:
    bson.ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
