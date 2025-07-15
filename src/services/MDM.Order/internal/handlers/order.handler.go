package handler

import (
	"net/http"

	"github.com/gin-gonic/gin"

	service "github.com/binpqh/MDM.Order/internal/services"
)

type OrderHandler struct {
	orderService *service.OrderService
}

func NewOrderHandler() *OrderHandler {
	return &OrderHandler{
		orderService: service.NewOrderService(),
	}
}

func (oh *OrderHandler) CreateOrder(c *gin.Context) {
	// Handler logic for creating an order
	messageResponse, err := oh.orderService.CreateOrder("Sample Order Data")
	if err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": err.Error(),
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"message": messageResponse,
	})
}
