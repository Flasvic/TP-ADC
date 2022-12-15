
inicial = input("Bem-vindo!")
inicial2 = input("Deseja criar conta de utilizador?")

answer = input("Responda 'Sim' ou 'Não': ")
if answer == "Sim" or "sim":

    def registar_user():
          cadastro_user = input("\n\nUser: ")
    def registar_senha():
          cadastro_senha = input("\n\nSenha: ")
          print("Conta criada com sucesso!")


user = input("\n\nUser: ")
senha = input("Senha: ")

#O programa utiliza o username e a senha fornecida pelo cliente
if user == USER_SALVO and senha == SENHA_SALVA:
    print("Login realizado")
