#!/usr/bin/env python3
'''
Insert a document mongoDB using Python
'''


def insert_school(mongo_collection, **kwargs):
    '''
    Args:mongo_collection: The MongoDB collection object.

    **kwargs: Key-value pairs representing the fields
    and values of the new document.

    Returns:
    str: The _id of the newly inserted document.
    '''
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
