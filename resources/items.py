from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db

import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort

from schema import ItemSchema, ItemUpdateSchema

from models import ItemModel

bp = Blueprint("Items", __name__, description="Operations on items")


@bp.route("/item/<string:item_id>")
class Item(MethodView):
    @bp.response(200, ItemSchema)
    def get(self, item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
    
    def delete(self, item_id):
        item = ItemModel.query.get_or_404(item_id)

        db.session.delete(item)
        db.session.commit()

        return {"message": "Item deleted"}

    @bp.arguments(ItemUpdateSchema)
    @bp.response(200, ItemSchema)
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)

        if item:
            item.price = item_data["price"]
            item.name = item_data["name"]
        else:
            item = ItemModel(id=item_id, **item_data)
        
        db.session.add(item)
        db.session.commit()

        return item
    
#Ejemplo:

    #item = item | item_data

    #Es decir: actualiza item con las claves y valores de item_data.
    #item = {"name": "Laptop", "price": 1000}
    #item_data = {"price": 899.99, "stock": 5}
    #item |= item_data
    # Resultado:
    # item == {'name': 'Laptop', 'price': 899.99, 'stock': 5}



@bp.route("/item")
class ItemList(MethodView):
    @bp.response(200, ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()

    @bp.arguments(ItemSchema)
    @bp.response(201, ItemSchema)
    def post(self, item_data):
        item = ItemModel(**item_data)
        
        try:
            db.session.add(item)
            db.session.commit()

        except SQLAlchemyError:
            abort(500, message = "An error occured while inserting the item.")

        return item