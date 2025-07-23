# Demo_API

A simple FastAPI project demonstrating a modular API structure with service and utility layers, containerization support, and automated testing.

## Features
- **Addition API**: Add two numbers via a POST endpoint (`/add_no`).
- **Service Layer**: Business logic separated from routing.
- **Utility Layer**: Standardized JSON responses.
- **Testing**: Automated tests using pytest and FastAPI's TestClient.
- **Docker Support**: Ready for containerized deployment.

## Project Structure
```
Demo_API/
├── app/
│   ├── api/routes/
│   │   ├── __init__.py
│   │   └── register_routes.py      # Defines /add_no endpoint
│   ├── database.py                 # (Empty) Placeholder for DB logic
│   ├── services/
│   │   └── register_service.py     # Business logic for addition
│   ├── utils/
│   │   └── common_utils.py         # Utility for JSON responses
│   └── workers/                    # (Empty) For background tasks
├── config.py                       # (Empty) For configuration
├── docker-compose.yml              # Docker Compose config
├── Dockerfile                      # Dockerfile for app
├── index.py                        # FastAPI app entry point
├── requirements.txt                # Python dependencies
├── tests/
│   └── test_add.py                 # Automated tests
└── README.md                       # Project documentation
```

## API Usage
### Add Two Numbers
- **Endpoint:** `POST /add_no`
- **Request Body:**
  ```json
  {
    "num1": 5,
    "num2": 3
  }
  ```
- **Response:**
  - Success (200):
    ```json
    {
      "status": true,
      "message": "Addition successful",
      "data": { "total": 8 }
    }
    ```
  - Error (400/500):
    ```json
    {
      "status": false,
      "message": "Error message",
      "data": {}
    }
    ```

## Setup & Running
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```bash
   uvicorn index:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000`.

3. **Docker (optional):**
   - Build and run with Docker Compose:
     ```bash
     docker-compose up --build
     ```

## Testing
Run all tests using pytest:
```bash
pytest
```

## Extending the Project
- Add more endpoints in `app/api/routes/`.
- Implement business logic in `app/services/`.
- Add utility functions in `app/utils/`.
- Add database logic in `app/database.py`.
- Add background workers in `app/workers/`.

---

**Author:** _Deepak Kumar_

---

This project is a template for building scalable FastAPI applications with clear separation of concerns and easy extensibility.
