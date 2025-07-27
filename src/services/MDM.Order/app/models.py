from datetime import datetime, timezone
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field
from enum import Enum


class PyObjectId(ObjectId):
    """Custom Pydantic-compatible ObjectId Type"""

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return ObjectId(v)


class Entity(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    created_on: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_on : Optional[datetime] = None
    deleted_on : Optional[datetime] = None
    created_by : Optional[PyObjectId] = None
    updated_by : Optional[PyObjectId] = None
    deleted_by : Optional[PyObjectId] = None
    is_deleted : bool = False

    class Config:
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}
        use_enum_values = True

class OrderState(Enum):
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELED = "canceled"

class OrderItem(Entity):
    order_id : PyObjectId
    product_id : PyObjectId
    quantity : int

    @classmethod
    def create(cls, order_id, product_id, quantity):
        return OrderItem(
            order_id=order_id,
            product_id=product_id,
            quantity=quantity,
            created_by= PyObjectId(ObjectId()),
        )

    def attach_to_order(self, order_id):
        self.order_id = order_id
        return self

class Order(Entity):
    customer_id: PyObjectId
    state : OrderState = OrderState.PROCESSING

    def complete(self):
        self.state = OrderState.COMPLETED

    def cancel(self):
        self.state = OrderState.CANCELED

    def failure(self):
        self.state = OrderState.FAILED