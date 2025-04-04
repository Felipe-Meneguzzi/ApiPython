from services.BaseService import BaseService, HTTPStatus
from repositories.UserRepository import UserRepository
repository = UserRepository()


class service():
    def login(body):
        if not body:
            return BaseService.send_response(data="Corpo da requisicao vazio.", status_code=HTTPStatus.BAD_REQUEST)
        if not body.get('login'):
            return BaseService.send_response(data="Login nao informado.", status_code=HTTPStatus.BAD_REQUEST)
        if not body.get('password'):
            return BaseService.send_response(data="Senha nao informada.", status_code=HTTPStatus.BAD_REQUEST)

        login = body['login']
        user = repository.get_user_by_login(login)

        if not user:
            return BaseService.send_response(data="Usuario nao encontrado.", status_code=HTTPStatus.NOT_FOUND)

        if not user.active:
            return BaseService.send_response(data="Usuario inativo.", status_code=HTTPStatus.UNAUTHORIZED)

        if user.password != body['password']:
            return BaseService.send_response(data="Senha incorreta.", status_code=HTTPStatus.UNAUTHORIZED)

        return BaseService.send_response(data={"mensagem": "Logado", "usuario": user.model_dump()}, status_code=HTTPStatus.OK)
