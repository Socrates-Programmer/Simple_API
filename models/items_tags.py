from db import db

class ItemsTags(db.Model):

    __table__ = "items_tags"

    id = db.Column(db.Integer, primery_key=True)
    item_id = db.Column(db.Integer, db.Foreignkey("items.id"))
    tag_id = db.Column(db.Integer, db.Foreignkey("tags.id"))
    