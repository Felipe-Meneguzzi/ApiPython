from fastapi import APIRouter, Query, Request
from entities.UserEntity import UserEntity

router = APIRouter()

@router.get("/users", response_model=object)
async def get_users():
    from services.users.get_users import service
    return service.get_users()

@router.get("/users/with-id", response_model=object)
async def get_user_with_id(id=Query(None, description="ID do usuario consultado")):
    from services.users.get_user_with_id import service
    return service.get_user_with_id(id)

@router.post("/users", response_model=object)
async def create_user(request: Request):
    body = await request.json()
    from services.users.create_user import service
    return service.create_user(body)