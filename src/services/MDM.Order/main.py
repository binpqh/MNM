"""FastAPI application for MDM Order service."""
from contextlib import asynccontextmanager

from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
from app.database import client, db

@asynccontextmanager
async def lifespan(app_builder: FastAPI):
    app_builder.mongodb_client = client
    app_builder.database = db
    yield
    app_builder.mongodb_client.close()

# Create FastAPI application instance
app = FastAPI(
    lifespan=lifespan,
    title="MDM Order",
    version="1.0",
    description="Order management service for MDM system",
)

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint that returns a welcome message."""
    return {"message": "Hello World"}

@app.get("/scalar", include_in_schema=False)
async def scalar():
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
