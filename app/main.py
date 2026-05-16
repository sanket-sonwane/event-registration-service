from fastapi import FastAPI
from app.routes import registration, participants

app = FastAPI(
    title="Event Registration Service",
    description="A microservice for managing event registrations. Designed for high-performance and scalability.",
    version="1.0.0",
)

# Include routers
app.include_router(registration.router)
app.include_router(participants.router)

@app.get("/", tags=["Health"])
async def health_check():
    """Service health check endpoint."""
    return {"status": "healthy", "service": "event-registration-service"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
