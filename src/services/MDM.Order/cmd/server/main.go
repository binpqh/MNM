package main

import (
	orderRouter "github.com/binpqh/MDM.Order/internal/routers"
)

func main() {
	r := orderRouter.NewOrderRouter()

	r.Run() // listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
}
