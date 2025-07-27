from enum import Enum

from bson import ObjectId
from typing import List, Optional
from datetime import datetime

from app.models.order_item import OrderItem


class OrderStatus(Enum):
    PENDING = "Pending"
    PROCESSING = "Processing"
    COMPLETED = "Completed"
    CANCELED = "Canceled"


def to_dict():
    return {
        "items" : 1,
    }

class Order:
    order_id: ObjectId = None
    customer_id: ObjectId = None
    status: OrderStatus = OrderStatus.PENDING
    items: List[OrderItem] = []
    total_mounts: int = 0
    created_by: ObjectId = None
    created_on: datetime = None
    updated_on: datetime = None
    deleted_on: datetime = None
    updated_by: Optional[ObjectId] = None
    deleted_by: Optional[ObjectId] = None
    is_deleted: bool = None

    @classmethod
    def create(cls, customer_id, status): # static method
        instance = cls()
        instance.order_id = ObjectId()
        instance.customer_id = customer_id
        instance.status = status
        return instance


    def add_item(self, item1): # normal method
        self.items.append(item1)

    def complete(self):
        self.status = OrderStatus.COMPLETED

    def cancel(self):
        self.status = OrderStatus.CANCELED

    def delete(self, current_user):
        self.deleted_by = current_user
        self.deleted_on = datetime.utcnow()


# Use case handling
# Walk
# about + noun
# about walking ->
item = OrderItem.create(1, 1, 2000)

order = Order.create(
    customer_id= ObjectId(),
    status = OrderStatus.PROCESSING
)

Order.add_item(item)

order.add_item(item)

none = [item,order]
for item in none:
    print(f"Item {item.id},")

# run main.py? run order.py -> missing order_item.py?
# -> the logic should be called by main.py (API Root/ Root modules / App Initialization Module)

