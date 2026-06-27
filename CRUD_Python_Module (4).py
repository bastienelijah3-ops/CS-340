from pymongo import MongoClient
from bson.objectid import ObjectId

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient helps the object connection across the class.
        # Format: MongoClient('mongodb://user:password@host:port/?authSource=grid')
        self.client = MongoClient('mongodb://%s:%s@localhost:27017/?authSource=admin' % (username, password))
        self.database = self.client['aac']
        self.collection = self.database['animals']

    def create(self, data):
        """ Inserts a document into the specified MongoDB collection """
        if data is not None:
            try:
                # Insert the data dictionary into the collection
                self.collection.insert_one(data)  
                return True
            except Exception as e:
                print(f"An error occurred during insertion: {e}")
                return False
        else:
            raise Exception("Nothing to save, because data parameter is empty")

    def read(self, search_criteria):
        """ Queries for documents from the MongoDB collection """
        if search_criteria is not None:
            try:
                # Use find() as required. It returns a cursor.
                cursor = self.collection.find(search_criteria)
                
                # Convert the MongoDB cursor into a standard Python list
                result_list = list(cursor)
                return result_list
            except Exception as e:
                print(f"An error occurred during query: {e}")
                return []
        else:
            # If no criteria provided, return an empty list or handle as needed
            print("Search criteria is empty.")
            return []

    def update(self, search_criteria, update_data):
        """ Queries for and changes document(s) from the collection """
        if search_criteria is not None and update_data is not None:
            try:
                # Use update_many to handle single or multiple documents
                # Wrap update_data in the '$set' operator so it updates fields instead of replacing the doc
                result = self.collection.update_many(search_criteria, {"$set": update_data})
                return result.modified_count
            except Exception as e:
                print(f"An error occurred during update: {e}")
                return 0
        else:
            print("Search criteria or update data is empty.")
            return 0

    def delete(self, search_criteria):
        """ Queries for and removes document(s) from the collection """
        if search_criteria is not None:
            try:
                # Use delete_many to safely clear out matched documents
                result = self.collection.delete_many(search_criteria)
                return result.deleted_count
            except Exception as e:
                print(f"An error occurred during deletion: {e}")
                return 0
        else:
            print("Search criteria is empty.")
            return 0