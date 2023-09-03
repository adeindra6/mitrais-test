from app import app
from flask import request
from app.controllers import users

@app.route("/")
@app.route("/index", methods=["GET"])
def index():
    message = {
        "message": "Mitrais Test",
    }

    return message

@app.route("/users", methods=["GET", "POST"])
def usersRoute():
    if request.method == "POST":
        userJson = request.get_json()
        response = users.storeUser(userJson)

        return response
    elif request.method == "GET":
        usersData = users.fetchUsers()

        return usersData
