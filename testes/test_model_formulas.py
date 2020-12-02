import pytest

from model.formulas import CrCalc, CursoCrMedia

@pytest.fixture
def cr_calc_instancia():
    return CrCalc()

def test_cr_inicial_igual_zero(cr_calc_instancia):
    assert cr_calc_instancia.cr == 0

notas_cr_de_teste = [
                    ([[100],[60]], 100), 
                    ([[100, 100],[60, 60]], 100)
                    ]

@pytest.mark.parametrize('lista_de_notas, cr', notas_cr_de_teste)
def test_atualizacao_do_cr(cr_calc_instancia, lista_de_notas, cr):
    cr_calc_instancia.atualizar(lista_de_notas[0], lista_de_notas[1])
    assert cr_calc_instancia.cr == cr

@pytest.fixture
def cr_media_instancia():
    return CursoCrMedia()

def test_media_cr_inicial_igual_zero(cr_media_instancia):
    assert cr_media_instancia.mediaCr == 0

notas_media_cr_teste = [
                       ([100], 100),
                       ([100, 100], 100)
                       ]

@pytest.mark.parametrize('lista_de_notas, cr', notas_media_cr_teste)
def test_atualizacao_do_mediaCr(cr_media_instancia, lista_de_notas, cr):
    cr_media_instancia.atualizar(lista_de_notas)
    assert cr_media_instancia.mediaCr == cr