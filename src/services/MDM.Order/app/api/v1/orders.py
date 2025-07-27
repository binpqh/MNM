# """Order API endpoints."""
#
# from typing import List, Optional
# from fastapi import APIRouter, Depends, HTTPException, Query, Path
# from sqlalchemy.orm import Session
#
# from app.db.database import get_db
# from app.services.order_service import OrderService
# from app.models.order import (
#     OrderCreate,
#     OrderUpdate,
#     OrderResponse,
#     OrderWithItemsResponse,
#     OrderStatus,
#     PaymentStatus,
# )
# from app.models.order_item import (
#     OrderItemCreate,
#     OrderItemUpdate,
#     OrderItemResponse,
# )
#
# router = APIRouter(prefix="/orders", tags=["orders"])
#
#
# @router.post("/", response_model=OrderResponse, status_code=201)
# async def create_order(
#     order_data: OrderCreate,
#     db: Session = Depends(get_db)
# ):
#     """Create a new order."""
#     try:
#         order = OrderService.create_order(db, order_data)
#         return order
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=f"Failed to create order: {str(e)}")
#
#
# @router.get("/", response_model=List[OrderResponse])
# async def get_orders(
#     skip: int = Query(0, ge=0, description="Number of records to skip"),
#     limit: int = Query(100, ge=1, le=1000, description="Number of records to return"),
#     customer_id: Optional[str] = Query(None, description="Filter by customer ID"),
#     status: Optional[OrderStatus] = Query(None, description="Filter by order status"),
#     db: Session = Depends(get_db)
# ):
#     """Get list of orders with optional filtering."""
#     orders = OrderService.get_orders(
#         db, skip=skip, limit=limit, customer_id=customer_id, status=status
#     )
#     return orders
#
#
# @router.get("/{order_id}", response_model=OrderWithItemsResponse)
# async def get_order(
#     order_id: int = Path(..., description="Order ID"),
#     db: Session = Depends(get_db)
# ):
#     """Get order by ID with items."""
#     order = OrderService.get_order(db, order_id)
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @router.get("/number/{order_number}", response_model=OrderWithItemsResponse)
# async def get_order_by_number(
#     order_number: str = Path(..., description="Order number"),
#     db: Session = Depends(get_db)
# ):
#     """Get order by order number with items."""
#     order = OrderService.get_order_by_number(db, order_number)
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @router.put("/{order_id}", response_model=OrderResponse)
# async def update_order(
#     order_id: int = Path(..., description="Order ID"),
#     order_data: OrderUpdate = None,
#     db: Session = Depends(get_db)
# ):
#     """Update an order."""
#     order = OrderService.update_order(db, order_id, order_data)
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @router.delete("/{order_id}", status_code=204)
# async def delete_order(
#     order_id: int = Path(..., description="Order ID"),
#     db: Session = Depends(get_db)
# ):
#     """Delete an order."""
#     success = OrderService.delete_order(db, order_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Order not found")
#
#
# @router.patch("/{order_id}/status", response_model=OrderResponse)
# async def update_order_status(
#     order_id: int = Path(..., description="Order ID"),
#     status: OrderStatus = Query(..., description="New order status"),
#     db: Session = Depends(get_db)
# ):
#     """Update order status."""
#     order = OrderService.update_order_status(db, order_id, status)
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# @router.patch("/{order_id}/payment-status", response_model=OrderResponse)
# async def update_payment_status(
#     order_id: int = Path(..., description="Order ID"),
#     payment_status: PaymentStatus = Query(..., description="New payment status"),
#     db: Session = Depends(get_db)
# ):
#     """Update payment status."""
#     order = OrderService.update_payment_status(db, order_id, payment_status)
#     if not order:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return order
#
#
# # Order Items endpoints
# @router.post("/{order_id}/items", response_model=OrderItemResponse, status_code=201)
# async def add_order_item(
#     order_id: int = Path(..., description="Order ID"),
#     item_data: OrderItemCreate = None,
#     db: Session = Depends(get_db)
# ):
#     """Add an item to an order."""
#     item = OrderService.add_order_item(db, order_id, item_data)
#     if not item:
#         raise HTTPException(status_code=404, detail="Order not found")
#     return item
#
#
# @router.put("/{order_id}/items/{item_id}", response_model=OrderItemResponse)
# async def update_order_item(
#     order_id: int = Path(..., description="Order ID"),
#     item_id: int = Path(..., description="Item ID"),
#     item_data: OrderItemUpdate = None,
#     db: Session = Depends(get_db)
# ):
#     """Update an order item."""
#     item = OrderService.update_order_item(db, order_id, item_id, item_data)
#     if not item:
#         raise HTTPException(status_code=404, detail="Order item not found")
#     return item
#
#
# @router.delete("/{order_id}/items/{item_id}", status_code=204)
# async def remove_order_item(
#     order_id: int = Path(..., description="Order ID"),
#     item_id: int = Path(..., description="Item ID"),
#     db: Session = Depends(get_db)
# ):
#     """Remove an item from an order."""
#     success = OrderService.remove_order_item(db, order_id, item_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Order item not found")