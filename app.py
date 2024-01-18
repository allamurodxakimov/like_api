# Import libraries
from flask import Flask, request
from like_db import LikeDB
# Create an instance of Flask
app = Flask(__name__)
likeDB = LikeDB('like_db.json')
@app.route("/")
def home():
    return "Hello World!"

@app.route("/api/addImage", methods=["POST"])
def addImage():
    # Get the image from the request
    if request.method == "POST":
        # Get json data from request
        data = request.get_json(force=True)
        # Get the image id from data
        image_id = data["image_id"]
        # Get the message id from data
        message_id = data["message_id"]
        url = data['url']
        likeDB.add_image(image_id, message_id, url)
        print(f'Image id: {image_id} Message id: {message_id}')

    return {"statust":"OK"}

@app.route('/api/addUser', methods=["POST"])
def addUser():
    if request.method=="POST":
        data = request.get_json()
        image_id = data['image_id']
        user_id = data['user_id']
        likeDB.add_users(image_id=image_id, user_id=user_id)
    return {"statust":"OK"}

@app.route('/api/addLike', methods=["POST"])
def addLike():
    if request.method=="POST":
        data = request.get_json()
        image_id = data['image_id']
        user_id = data['user_id']
        likeDB.add_like(user_id=user_id, image_id=image_id)
    return {"statust":"OK"}

@app.route('/api/addDislike', methods=["POST"])
def addDislike():
    if request.method=="POST":
        data = request.get_json()
        user_id = data['user_id']
        image_id = data['image_id']
        likeDB.add_dislike(user_id=user_id, image_id=image_id)
    return {"statust": "OK"}

@app.route('/api/getlikesdislikes', methods=['POST'])
def getLikesDislikes():
    if request.method=="POST":
        data = request.get_json()
        image_id = data['image_id']
        likeDB.get_likes_dislikes(image_id)
        data = likeDB.get_likes_dislikes(image_id)
    return list(data)

@app.route("/api/allLikesDislikes", methods=['POST'])
def allLikesDislikes():
    data  = likeDB.all_likes_dislikes()
    return {
        "likes":data[0],
        "dislikes":data[-1]
    }


# Run the app
if __name__ == "__main__":
    app.run(debug=True)