from flaskmongo import db


class User(db.Document):
    uid=db.IntField(required=True,unique=True)
    name = db.StringField(required=True)
    email = db.StringField(required=True)
    password=db.StringField(required=True)