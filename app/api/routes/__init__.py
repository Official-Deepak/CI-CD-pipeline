from fastapi import APIRouter
from .register_routes import router as register_router

router = APIRouter()

# Register routes
router.include_router(
    register_router,
    tags=["register"]
)