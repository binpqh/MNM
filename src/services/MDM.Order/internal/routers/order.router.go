package routers

import (
	handler "github.com/binpqh/MDM.Order/internal/handlers"
	"github.com/gin-gonic/gin"
)

func NewOrderRouter() *gin.Engine {
	r := gin.Default()

	orderHandler := handler.NewOrderHandler()

	v1 := r.Group("/api/v1/orders")
	{
		v1.POST("/", orderHandler.CreateOrder)
	}

	return r
}
