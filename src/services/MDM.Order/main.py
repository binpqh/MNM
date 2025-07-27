"""FastAPI application for greeting endpoints."""
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

# Create FastAPI application instance
app = FastAPI(
    title="MDM Order",
    version="1.0",

)


# Root endpoint
@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Hello World"}

@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    """
    Serve the Scalar API reference documentation.
    
    This endpoint returns an interactive API documentation interface using Scalar.
    The documentation is generated from the FastAPI application's OpenAPI schema.
    
    Returns:
        HTML content: The Scalar API reference interface
    """
    return get_scalar_api_reference(
        title=app.title, # type: ignore
        openapi_url=app.openapi_url, # type: ignore
    )

# Endpoint that greets the user by name
@app.get("/hello/{name}")
async def say_hello(name: str):
    """Endpoint that greets the user by name."""
    return {"message": f"Hello {name}"}