import pytest

from controllers.calcularCr import CalcularCr

@pytest.fixture
def calcularCr_arquivo_nao_existe():
    return CalcularCr('doc.csv')

@pytest.fixture
def calcularCr_arquivo_existe():
    return CalcularCr('notas.csv')

def test_que_o_nome_do_csv_e_igual_a_doc(calcularCr_arquivo_nao_existe):
    assert calcularCr_arquivo_nao_existe.nomeDoCsv == 'doc.csv'

def test_cadastrar_arquivo_que__existe_retorna_true(calcularCr_arquivo_existe):
    assert calcularCr_arquivo_existe.cadastrar_csv() == True

def test_cadastrar_arquivo_que_nao_existe_retorna_false(calcularCr_arquivo_nao_existe):
    assert calcularCr_arquivo_nao_existe.cadastrar_csv() == False