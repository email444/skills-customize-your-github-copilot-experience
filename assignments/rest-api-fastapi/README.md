# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a complete REST API using the FastAPI framework. You'll create endpoints for reading and writing data, implement request validation, handle errors properly, and learn how to structure a modern web service.

## 📝 Tasks

### 🛠️ Create a Basic FastAPI Application

#### Description
Set up a FastAPI application with a basic HTTP server and implement your first GET endpoint.

#### Requirements
Completed program should:

- Install FastAPI and Uvicorn dependencies
- Create a FastAPI application instance
- Implement a GET endpoint at `/` that returns a welcome message
- Implement a GET endpoint at `/items/{item_id}` that returns item details based on the ID
- Run the server using Uvicorn on port 8000
- Example response for `/items/1`: `{"item_id": 1, "name": "Item 1", "price": 9.99}`


### 🛠️ Add Data Validation with Pydantic Models

#### Description
Create request and response models using Pydantic to validate incoming data and ensure consistent API responses.

#### Requirements
Completed program should:

- Define a Pydantic model for an `Item` with fields: `name` (string), `price` (float), `description` (optional string)
- Implement a POST endpoint at `/items/` that accepts an Item object and returns the created item
- Implement a GET endpoint at `/items/` that returns a list of all items
- Validate that `price` is a positive number
- Example POST request: `{"name": "Laptop", "price": 999.99, "description": "A powerful laptop"}`


### 🛠️ Implement Error Handling and Status Codes

#### Description
Handle errors gracefully and return appropriate HTTP status codes for different scenarios.

#### Requirements
Completed program should:

- Return 404 status code when an item is not found
- Return 400 status code for invalid request data
- Raise `HTTPException` with proper status codes and error messages
- Implement a DELETE endpoint at `/items/{item_id}` that removes an item and returns appropriate status
- Example error response: `{"detail": "Item with id 5 not found"}`


### 🛠️ Add Advanced Features (Stretch Goal)

#### Description
Extend your API with query parameters, filtering, and documentation features.

#### Requirements
Completed program should:

- Add query parameters to the GET `/items/` endpoint to filter by price range (e.g., `?min_price=10&max_price=100`)
- Implement an update endpoint (PUT) at `/items/{item_id}` to modify existing items
- Add Uvicorn auto-reload for development
- View the auto-generated API documentation at `/docs` (Swagger UI)
- Example: `GET /items/?min_price=50&max_price=500` returns only items in that price range
