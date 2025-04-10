from fastapi import APIRouter, Query, Request, Body
from http import HTTPStatus
from src.valueObjects.ResponseBody import ResponseBody

router = APIRouter()


@router.post("",
             response_model=ResponseBody,
             status_code=HTTPStatus.OK,
             tags=["login"],
             response_description="Retorna o token do usuario logado",
             summary="Logar",
             )
async def login(request: Request,
                body: dict = Body(...,
                                  description="Corpo da requisicao para fazer o login.",
                                  example={
                                      "login": "teste@gmail.com",
                                      "password": "123456",
                                  }
                                  )):
    """

    Realiza o login
    - **login**: login do usuario
    - **password**: senha do usuario

    """
    body = await request.json()
    from src.services.login.login import service
    return service.login(body)
