from typing import List

from bson import ObjectId

from app.models import OrderItem
from app.models.order import OrderStatus, Order


class OrderServices:
    pass

def create_order(customer_id: ObjectId, items : List[OrderItem] ):
    ## put logic create order right here.
    order = Order.create(customer_id, OrderStatus.PROCESSING)

    order.add_item(items)

    # save new order into database

    return None

# Use case handling
# pay order handler
def pay_order(order_id : ObjectId, customer_id: ObjectId):
    # get order by order_id
    # database -> 50 records
    # khach so 1 -> thanh toan order_id = 02_abc
    # system -> call method pay_order -> find order by id 02_abc
    # change value -> status -> PROCESSING -> COMPLETED
    order = db.getById(order_id)
    order = Order()
    if pay_sucfessful:
        order.complete()
    else
        return pay_failed
    return None

def cancel_order
    (order_id : ObjectId, customer_id: ObjectId):
    # get order by order_id
    # database -> 50 records
    # khach so 1 -> thanh toan order_id = 02_abc
    # system -> call method pay_order -> find order by id 02_abc
    # change value -> status -> PROCESSING -> COMPLETED
    order = db.getById(order_id)
    order = Order()
    order.cancel()
    return None

def delete_order(order_id : ObjectId):
    order = db.getById(order_id)
    order = Order()
    order.delete(order_id)
    return None