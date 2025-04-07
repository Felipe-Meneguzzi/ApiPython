from services.users.get_users import service
from fastapi import APIRouter, Query, Request, Body
from valueObjects.ResponseBody import ResponseBody
from valueObjects.PageObject import PageObject
from http import HTTPStatus

router = APIRouter()


@router.get("", response_model=object, status_code=HTTPStatus.OK, tags=["users"])
async def get_users(
    page: int = Query(
        1, description="Numero da pagina"),
    page_size: int = Query(
        10, description="Tamanho da pagina"),
    sort: str = Query(
        "id", description="Campo para ordenacao"),
    sort_direction: str = Query(
        "asc", description="Direcao da ordenacao (asc ou desc)"),
    search: str = Query(
        None, description="Campos para busca, recebe um dict"),
    filters: str = Query(
        None, description="Campos para filtro, recebe um dict")
):
    page_obj = PageObject(page=page, page_size=page_size, sort=sort,
                          sort_direction=sort_direction, search=search, filters=filters)
    return service.get_users(page_obj)


@router.get("/with-id", response_model=object, status_code=HTTPStatus.OK, tags=["users"])
async def get_user_with_id(id=Query(None, description="ID do usuario consultado")):
    from services.users.get_user_with_id import service
    return service.get_user_with_id(id)


@router.post("",
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
    - **user_type**: tipo do usuario(1 - Admin | 2 - Comum | 3 - Observador)
    -------------
    """
    body = await request.json()
    from services.users.create_user import service
    return service.create_user(body)
