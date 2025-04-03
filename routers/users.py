from fastapi import APIRouter, Query

router = APIRouter()

@router.get("/users", response_model=object)
def get_users():
    from services.users.get_users import service
    return service.get_users()

@router.get("/users/with-id", response_model=object)
def get_user_with_id(id=Query(None, description="ID do usuario consultado")):
    from services.users.get_user_with_id import service
    return service.get_user_with_id(id)