# Event Registration Service

A robust microservice built with FastAPI for managing event participant registrations. This service follows a clean modular architecture and provides high-performance in-memory storage.

## Project Overview

The **Event Registration Service** is designed to handle high volumes of participant sign-ups for large-scale events. It features a simplified internal architecture focusing on core registration flows and participant management.

## API Documentation

The service automatically generates OpenAPI documentation available at:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints

#### 1. POST `/register`
Registers a new participant.

**Request Body:**
```json
{
  "name": "Rahul",
  "email": "rahul@example.com",
  "age": 15
}
```

**Success Response (201 Created):**
```json
{
  "message": "Registration successful",
  "participant_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

#### 2. GET `/participants`
Lists all registered participants.

**Success Response (200 OK):**
```json
[
  {
    "participant_id": "550e8400-e29b-41d4-a716-446655440000",
    "name": "Rahul",
    "email": "rahul@example.com",
    "age": 15
  }
]
```

## Behavioral Guarantees

- Users under 18 must be rejected
- Duplicate email registrations are not allowed
- Missing required fields return 422
- Participant listing endpoints should support pagination
- Successful registrations return a generated participant ID

## Architecture Summary

The project follows a clean separation of concerns:
- **Routes**: Handle HTTP requests and response formatting (`app/routes`)
- **Services**: Implement business logic and orchestration (`app/services`)
- **Models**: Define data structures and validation schemas using Pydantic v2 (`app/models`)
- **Storage**: Abstracted data persistence layer (`app/storage`)

## Getting Started

### Prerequisites
- Python 3.11+

### Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start the service using Uvicorn:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
   ```

### Running with Docker (Optional)
The service is lightweight and can be easily containerized for deployment.
