import os
import pymongo


class Database(object):

    URI = os.environ.get('MONGODB_URI')
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.get_default_database()

    @staticmethod
    def insert(data):
        Database.DATABASE['posts'].insert(data)

    @staticmethod
    def find(query):
        return Database.DATABASE['posts'].find(query)

    @staticmethod
    def purge():
        return Database.DATABASE['posts'].remove({})
