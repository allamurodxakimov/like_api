import json
from tinydb import TinyDB, Query
from tinydb.table import Document

class LikeDB:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = TinyDB(db_path, indent=4)
        self.users = self.db.table('users')
        self.images = self.db.table('images')

    def add_image(self, image_id: str, message_id: str, url: str):

        image = Document({'image_id': image_id, "url": url}, doc_id=message_id)
        self.images.insert(image)

    def add_users(self, image_id, user_id):

        user = Document({
            image_id:{
            "like":0,
            "dislike":0}
        }, doc_id=user_id)
        self.users.insert(user)

    def get_likes_dislikes(self, image_id: str):
        likes = 0
        dislikes = 0
        for user in self.users:
            date = user.get(image_id)
            if date != None:
                if date['like']:
                    likes+=1
                else:
                    dislikes+=1
            
        return likes, dislikes
    
    def add_like(self, user_id: str, image_id: str):
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {"like": True, 'dislike': False}
        else:
            user_doc = {image_id: {"like": True, 'dislike': False}}
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)
    
    def add_dislike(self, user_id: str, image_id: str):
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {'like': False, "dislike": True}
        else:
            user_doc = {image_id: {'like': False, 'dislike': True}}
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)

    def all_likes_dislikes(self):
        likes = 0
        dislikes = 0
        for user in self.users:
            for like in user.values():
                if like['like']:
                    likes+=1
                else:
                    dislikes+=1
        return [likes, dislikes]

