from app import db
from datetime import datetime

class Users(db.Model):
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    mobile_number = db.Column(db.String(255), index=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    date_of_birth = db.Column(db.Date)
    gender = db.Column(db.String(255))
    email = db.Column(db.String(255), index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return "<User {}>".format(self)