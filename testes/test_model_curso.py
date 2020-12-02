import pytest

from model.curso import Curso

@pytest.fixture
def curso_001():
    return Curso('001')

def test_que_codigo_do_curso_e_igual_001(curso_001):
    assert curso_001.codCurso == '001'

def test_que_disciplinas_e_notas_foram_cadastradas(curso_001):
    curso_001.add_disciplinas_e_notas({'MAT001', 'POR001', 'BIO001'}, [100, 100, 100])
    assert curso_001.disciplinas == {'MAT001', 'POR001', 'BIO001'} and curso_001.notas == [100, 100, 100]

def test_que_media_cr_igual_a_zero(curso_001):
    assert str(curso_001.mediaCr) == '0'

def test_que_media_cr_igual_a_100(curso_001):
    curso_001.add_disciplinas_e_notas({'MAT001', 'POR001', 'BIO001'}, [100, 100, 100])
    assert str(curso_001.mediaCr) == '100.0'
