from repositorios import obtener_email, UserRepository
class UserService():
    @staticmethod
    def login(email):
        user = UserRepository.obtener_email(
            data.email
        )
        if usuario is None:
            return {}