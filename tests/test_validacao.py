import pytest
from app.validacao import validar_cpf

#testar se e cpf valido
def test_validacao_cpf_valido():
    # Testa um CPF válido
    assert validar_cpf("12345678909") == True

#testar se e cpf invalido
def test_validacao_cpf_invalido():
    # Testa um CPF inválido
    assert validar_cpf("12345678900") == False

#testar se e cpf vazio
def test_validacao_cpf_vazio():
    # Testa um CPF vazio
    assert validar_cpf("") == False

#testar se e cpf com caracteres especiais
def test_validacao_cpf_caracteres_especiais():
    # Testa um CPF com caracteres especiais
    assert validar_cpf("12@.456.789-09") == False

#testar se e cpf com letras
def test_validacao_cpf_com_letras():
    # Testa um CPF com letras
    assert validar_cpf("1234a67e90a") == False

#testar cpf digitos igauais
def test_validacao_cpf_digitos_iguais():
    # Testa um CPF com dígitos iguais
    assert validar_cpf("11111111111") == False

#testar cpf com menos de 11 digitos
def test_validacao_cpf_menos_de_11_digitos():
    # Testa um CPF com menos de 11 dígitos
    assert validar_cpf("123456789") == False

#testar cpf com mais de 11 digitos
def test_validacao_cpf_mais_de_11_digitos():
    # Testa um CPF com mais de 11 dígitos
    assert validar_cpf("123456789012") == False

#testar cpf formatado
def test_validacao_cpf_formatado():
    # Testa um CPF formatado
    assert validar_cpf("123.456.789-09") == True

#testar cpf com numeros sequenciais
def test_validacao_cpf_numeros_sequenciais():
    # Testa um CPF com números sequenciais
    assert validar_cpf("12345678900") == False