from app import models, db
import json

def storeUser(userJson):
    mobile_number = userJson["mobile_number"]
    first_name = userJson["first_name"]
    last_name = userJson["last_name"]
    date_of_birth = userJson["date_of_birth"]
    gender = userJson["gender"]
    email = userJson["email"]

    users = models.Users(
        mobile_number=mobile_number,
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date_of_birth,
        gender=gender,
        email=email
    )

    db.session.add(users)
    db.session.commit()

    response = {
        "message": "Store users successful",
        "data": {
            "mobile_number": mobile_number,
            "first_name": first_name,
            "last_name": last_name,
            "date_of_birth": date_of_birth,
            "gender": gender,
            "email": email,
        },
    }

    return response

def fetchUsers():
    users = models.Users.query.all()

    listUsers = []
    for u in users:
        listUsers.append({
            "id": u.id,
            "mobile_number": u.mobile_number,
            "first_name": u.first_name,
            "last_name": u.last_name,
            "date_of_birth": u.date_of_birth,
            "gender": u.gender,
            "email": u.email,
            "created_at": u.created_at,
            "updated_at": u.updated_at,
        })

    return listUsers
