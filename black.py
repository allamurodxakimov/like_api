import json
#Create Like counting class
from tinydb import TinyDB, Query
from tinydb.table import Document

class LikeDB:
    def __init__(self, db_path):
        #Initialize the database
        self.db_path = db_path
        self.db = TinyDB(db_path, indent=4)
        self.users = self.db.table('users')
        self.images = self.db.table('images')




    def add_image(self,image_id:str, message_id:str):
        """Adds an image to the database
        args:
            image_id: The id of the image
            message_id: The id of the message that the image is attached to
        """
        #Add the image to the database
        image = Document({'image_id': image_id}, doc_id=message_id)
        self.images.insert(image)

    # def add_users(self, user_id, image_id, like, dislik):
    #     user = Document({"image_id":{image_id:{
    #         "like":like,
    #         "dislike":dislik
    #     }}},
    #     doc_id=user_id)
    #     self.users.insert(user)

    def get_likes_dislike(self, image_id:str):
        """Counts all users likes
        returns
            all users likes
        """
        # Query the database for all images
        # Count the number of likes
        likes = 0
        dislike = 0
        for user in self.users:
            if user[image_id]['like']:
                likes += 1
            else:
                dislike += 1
            
        return likes, dislike

 
        
        
    def all_dislikes(self):
        """Counts all users dislikes
        returns
            all users dislikes
        """
        pass
        
        
    #Add a like to the database
    def add_like(self, user_id:str,image_id)->dict:
        '''
        Add a like to the database
        args:
            user_id: The user id of the user who liked the post
            image_id: The image id of the image that was liked
        returns:
            The number of likes and dislikes for the post
        '''
        # Get the user document
        # If the user document does not exist, create it
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {'like': True, 'dislike': False}
        else:
            user_doc = {image_id: {'like': True, 'dislike': False}}
        # Create user document
        
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)
        

  
    #Add a dislike to the database
    def add_dislike(self, user_id:str,image_id)->dict:
        '''
        Add a dislike to the database
        args:
            user_id: The user id of the user who disliked the post
        returns:
            The number of likes and dislikes for the post
        '''
        if self.users.contains(doc_id=user_id):
            user_doc = self.users.get(doc_id=user_id)
            user_doc[image_id] = {'like': False, 'dislike': True}
        else:
            user_doc = {image_id: {'like': False, 'dislike': True}}
        # Create user document
     
        user_doc = Document(user_doc, doc_id=user_id)
        self.users.insert(user_doc)


# db = LikeDB('like_db.json')

# # db.add_like('user1', 'img1')
# # db.add_like('user2', 'img2')
# # db.add_dislike('4', 'img2')
# # db.add_image(1012, '3')
# db.add_like("user1", "img1")

