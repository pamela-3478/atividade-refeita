import pytest
import sys

from valida_login import validaLogin, validaUsuario, validaSenha

# Configuração do pytest-cov
sys.argv.extend(['--cov', 'valida_login'])

class TestValidacaoLogin:
    def test_validaUsuario(self):
        # Testes para validar o usuário
        assert validaUsuario("Usuario123") == True
        assert validaUsuario("usuario123") == False
        assert validaUsuario("Usuário@123") == False
        assert validaUsuario("Usuário 123") == False
        assert validaUsuario("UsuarioComMaisDe30CaracteresInvalido123456") == False

    def test_validaSenha(self):
        # Testes para validar a senha
        assert validaSenha("Senha123#!") == True
        assert validaSenha("Senha12!") == False
        assert validaSenha("senha123!") == False
        assert validaSenha("SENHA123!") == False
        assert validaSenha("Senha123") == False

    def test_validaLogin(self):
        # Testes para validar o login
        assert validaLogin("Usuario123", "Senha123!#") == True
        assert validaLogin("usuario123", "Senha123!") == False
        assert validaLogin("Usuario123", "senha123!") == False
        assert validaLogin("usuario123", "senha123!") == False
