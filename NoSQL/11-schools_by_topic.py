#!/usr/bin/env python3
"""Python function that returns a list of schools
having a specific topic."""


def schools_by_topic(mongo_collection, topic):
    """
    Retrieves a list of schools from the MongoDB
    collection that include the specified topic.

    Args:
    mongo_collection (pymongo.collection.Collection):
    The MongoDB collection object.
    topic (str): The topic to search for in the
    schools' topics.

    Returns:
    list: A list of documents where the topic is present
    in the school's topics.
    """
    query = {"topics": topic}
    schools = mongo_collection.find(query)
    return list(schools)
