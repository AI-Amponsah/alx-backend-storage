#!/usr/bin/env python3
""" MongoDB insert """


def insert_school(mongo_collection, **kwargs):
    """Inserts a document in school collection"""
    if len(kwargs) == 0:
        return None
    return mongo_collection.insert(kwargs)
