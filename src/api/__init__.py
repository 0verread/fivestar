from api.routes.auth import router as auth_router
from api.routes.hotel import router as hotel_router

__all__ = [
	"auth_router",
	"hotel_router",
]