class AuthController:
    @staticmethod
    def verificar_credenciais(usuario, senha):
        # Simulação de autenticação (pode ser substituído por banco de dados)
        usuarios_validos = {
            "admin": "1234",
            "usuario": "abcd"
        }
        return usuarios_validos.get(usuario) == senha

    @staticmethod
    def autenticar_usuario(usuario, senha):
        # Reutilizar o método de verificar credenciais
        if AuthController.verificar_credenciais(usuario, senha):
            return True
        return False
