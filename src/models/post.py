from src.common.database import Database
from uuid import uuid4


class Post(object):

    def __init__(self, title, author, content, _id=None):
        self.title = title
        self.content = content
        self.author = author
        self._id = uuid4().hex

    @classmethod
    def all(cls):
        return [cls(**elem) for elem in Database.find({})]

    def save_to_mongo(self):
        Database.insert(self.json())

    def json(self):
        return {"title": self.title,
                "content": self.content,
                "author": self.author,
                "_id": self._id}
