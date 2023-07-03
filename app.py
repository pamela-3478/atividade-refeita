from valida_login import validaLogin, validaMensagem
from cryptographyFramework import encryptMessage, saveNewLine

def criptografar_mensagem():
    user = input("Digite o usuario: ")
    password = input("Digite a senha: ")
    mensagem = input("Digite a mensagem: ")

    if validaLogin(user, password):
        # Verificar se a mensagem possui no máximo 70 caracteres
        if not validaMensagem(mensagem): print("A mensagem deve ter no máximo 70 caracteres.")
        
        # Criptografar a mensagem
        encrypted_message = encryptMessage(user, password, mensagem)
        # Salvar a mensagem criptografada em um arquivo
        saveNewLine(encrypted_message)
        print("Mensagem criptografada e salva com sucesso!")
    else:
        print("Usuário ou senha inválidos.")

criptografar_mensagem()