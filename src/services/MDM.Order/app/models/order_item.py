import datetime
from typing import Optional

from bson import ObjectId


class OrderItem:
    order_item_id: ObjectId = None
    product_id: ObjectId = None
    quantity: int = 1
    total_mount: float = 0
    created_on: datetime = None
    created_by: ObjectId = None
    deleted_by: ObjectId = None
    updated_on: Optional[datetime] = None
    deleted_on: Optional[datetime] = None
    updated_by: Optional[ObjectId] = None
    is_deleted: bool = False

    @classmethod
    def create(cls, product_id, quantity, total_mount):
        instance = cls()
        instance.product_id = product_id
        instance.quantity = quantity
        instance.total_mount = total_mount
        return instance

# orderItem01 = OrderItem.create(1,1,1)