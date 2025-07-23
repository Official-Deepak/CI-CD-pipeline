from fastapi import APIRouter,Request
from app.services.register_service import RegisterService
from app.utils.common_utils import handle_response

router = APIRouter()

@router.post("/add_no")
async def add_no(request:Request):
    try:
        request_data = await request.json()
        add_service = RegisterService()
        response = add_service.add_no(request_data)
        return response
    except Exception as e:
        return handle_response(
            status=False,
            message=str(e),
            status_code=500
        )