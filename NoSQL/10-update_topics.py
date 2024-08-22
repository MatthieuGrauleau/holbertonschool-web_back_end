#!/usr/bin/env python3
"""Python function that changes all topics of
a school document based on the name."""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics of a school document in
    the MongoDB collection.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The MongoDB collection object.
    name (str): The school name to update.
    topics (list): A list of topics to set for the school.

    Returns:
    None
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
