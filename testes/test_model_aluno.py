import pytest

from model.aluno import Aluno

@pytest.fixture
def aluno_001():
    return Aluno('001')

@pytest.fixture
def aluno_002():
    aluno = Aluno('002')
    aluno.addNotas('MAT001', 100, 60)
    aluno.addNotas('POR001', 100, 60)
    aluno.addNotas('BIO001', 100, 60)
    return aluno

def test_que_matricula_e_igual_a_001(aluno_001):
    assert aluno_001.matricula == '001'

def test_que_nota_foi_cadastrada(aluno_001):
    aluno_001.addNotas('MAT001', 80, 60)
    assert aluno_001.notas == {'MAT001': [80, 60]}

def test_que_aluno_002_esta_castrado(aluno_002):
    assert aluno_002.notas == {'MAT001': [100, 60], 'POR001': [100, 60], 'BIO001': [100, 60]}

def test_aluno_002_quando_se_retira_uma_materia(aluno_002):
    aluno_002.removeNotas('MAT001')
    assert aluno_002.notas == {'POR001': [100, 60], 'BIO001': [100, 60]}

def test_aluno_002_quando_se_atualiza_uma_nota(aluno_002):
    aluno_002.atualizarNotas('MAT001', 70)
    assert aluno_002.notas == {'MAT001': [70, 60], 'POR001': [100, 60], 'BIO001': [100, 60]}

def test_cr_aluno_001_igual_a_zero(aluno_001):
    assert str(aluno_001.cr) == '0'   

def test_cr_aluno_002_igual_a_100(aluno_002):
    assert str(aluno_002.cr) == '100.0'   

