from fastapi import FastAPI
from app.routes import registration, participants, stats

app = FastAPI(
    title="Event Registration Service API",
    description="""
A specialized microservice for managing participant registrations for large-scale events.
This API provides endpoints for registering participants and retrieving participant lists with metadata.
""",
    version="1.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Include routers
app.include_router(registration.router)
app.include_router(participants.router)
app.include_router(stats.router)

@app.get("/", tags=["Health"])
async def health_check():
    """Service health check endpoint."""
    return {"status": "healthy", "service": "event-registration-service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
