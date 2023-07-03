def validaLogin(usuario, senha):
    if validaUsuario(usuario) and validaSenha(senha): return True
    return False

def validaUsuario(usuario):
    # Salva em uma variavel o tamanho inicial do usuario
    tamanho_string_bruto = len(usuario)

    # Valida se a primeira letra e maiscula
    if not (usuario[0]).isupper(): return False

    # Valida se contém caracter especial
    for letra in usuario:
        if not letra.isalnum(): return False
    
    # Valida a diferença da string bruta para a sem espaços
    if len(usuario.strip()) != tamanho_string_bruto: return False
    # Valida se a senha e maior de 30 caracteres
    if len(usuario) > 30 : return False

    return True

def validaMensagem(mensagem) :
    if len(mensagem) > 70: return False
    return True

def validaSenha(senha):
    # Valida se o tamanho não é menor que 10
    if len(senha) < 10:
        return False

    # Cria as variáveis de controle
    caractere_especial = False 
    numero = False
    letra_maiuscula = False
    letra_minuscula = False

    # Valida se a senha contém os requisitos acima
    for caractere in senha:
        if caractere.isnumeric():
            numero = True
        elif caractere.isupper():
            letra_maiuscula = True
        elif caractere.islower():
            letra_minuscula = True
        elif not caractere.isalnum():
            caractere_especial = True

    # Se todos os requisitos forem válidos, retorna True
    if caractere_especial and numero and letra_maiuscula and letra_minuscula:
        return True
    return False