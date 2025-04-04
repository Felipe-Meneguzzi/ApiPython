from fastapi import APIRouter, Query, Request, Body
from services.ResponseBody import ResponseBody
from http import HTTPStatus

router = APIRouter()


@router.get("/users", response_model=object, status_code=HTTPStatus.OK, tags=["users"])
async def get_users():
    from services.users.get_users import service
    return service.get_users()


@router.get("/users/with-id", response_model=object, status_code=HTTPStatus.OK, tags=["users"])
async def get_user_with_id(id=Query(None, description="ID do usuario consultado")):
    from services.users.get_user_with_id import service
    return service.get_user_with_id(id)


@router.post("/users",
             response_model=ResponseBody,
             status_code=HTTPStatus.CREATED,
             tags=["users"],
             response_description="Retorna o usuario criado",
             summary="Criar usuario",
             )
async def create_user(request: Request,
                      body: dict = Body(...,
                                        description="Corpo da requisicao para criar um usuario. Deve conter os campos: name, password, user_type, ele ja e Ativo por padrao.",
                                        example={
                                            "name": "John Doe",
                                            "password": "123456",
                                            "user_type": 1,
                                        }
                                        )):
    """
    -------------
    Criar um usuario. O usuario e criado com o status ativo por padrao.
    - **name**: nome do usuario
    - **password**: senha do usuario
    - **user_type**: tipo do usuario (1 - Admin | 2 - Comum | 3 - Observador)
    -------------
    """
    body = await request.json()
    from services.users.create_user import service
    return service.create_user(body)
