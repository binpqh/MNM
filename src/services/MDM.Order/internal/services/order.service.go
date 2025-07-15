package service

import (
	r "github.com/binpqh/MDM.Order/internal/repositories"
)

type OrderService struct {
	orderRepository *r.OrderRepository
}

func NewOrderService() *OrderService {
	return &OrderService{
		orderRepository: r.NewOrderRepository(),
	}
}

func (os *OrderService) CreateOrder(orderData interface{}) (string, error) {
	// Logic to create an order using the repository
	orderID, err := os.orderRepository.CreateOrder(orderData)
	if err != nil {
		return "", err
	}
	return orderID, nil
}
