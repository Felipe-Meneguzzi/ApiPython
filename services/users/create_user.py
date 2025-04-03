from services.BaseService import BaseService, HTTPStatus
from repositories.UserRepository import UserRepository
from entities.UserEntity import UserEntity 
from enums.UserTypeEnum import UserTypeEnum
repository = UserRepository()

class service():
    def create_user(body):
        try:
            user = UserEntity(
                name = body['name'],
                password = body['password'],
                user_type = UserTypeEnum.from_value(body['user_type']),
                active = 1,
            )
        except ValueError:
            return BaseService.send_exception("Tipo de usuario invalido, confira a documentacao", HTTPStatus.BAD_REQUEST)
        except:
            return BaseService.send_exception("Dados de usuario invalidos, confira a documentacao", HTTPStatus.BAD_REQUEST)
        
        if user.name == None or user.name == "":
            return BaseService.send_exception("Nome do usuario nao informado", HTTPStatus.BAD_REQUEST)
        
        if user.password == None or user.password == "":
            return BaseService.send_exception("Senha do usuario nao informada", HTTPStatus.BAD_REQUEST)
        
        if user.active == None:
            return BaseService.send_exception("Usuario ativo nao informado", HTTPStatus.BAD_REQUEST)
        
        repository.create_user(user)

        repository.connection.commit()


        response = {
            "mensagem": "Usuario criado com sucesso",
            "user": user.model_dump()
        }

        return BaseService.send_response(response, HTTPStatus.CREATED)
