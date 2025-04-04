from fastapi import APIRouter, Query, Request, Body
from services.ResponseBody import ResponseBody
from http import HTTPStatus

router = APIRouter()


@router.post("/login",
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

    """
    # body = await request.json()
    # from services.users.create_user import service
    # return service.create_user(body)
    return ResponseBody(status_code=HTTPStatus.OK,
                        success=True,
                        data={
                            "token": "token"
                        },
                        metadata=None)
