from fastapi.responses import JSONResponse

def handle_response(status: bool, message: str, data: dict = {}, status_code: int = 200):
    return JSONResponse(
        content={
            "status": status,
            "message": message,
            "data": data
        },
        status_code=status_code
    )