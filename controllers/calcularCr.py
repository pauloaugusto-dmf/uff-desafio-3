from typing import TypeVar
from model.cadastro import Cadastro
from view.impresao import Impressao

I = TypeVar('I', bound=Impressao)
C = TypeVar('C', bound=Cadastro)

class CalcularCr():
    """Classe de controle responsavel por fazer as solicitações para o model e enviar a resposta para view"""
    def __init__(self, nomeDoCsv: str, impressao: I = Impressao, cadastro: C = Cadastro) -> None:
        self.nomeDoCsv: str = nomeDoCsv
        self.impressao: I = impressao()
        self.cadastro: C = cadastro

    def cadastrar_csv(self) -> bool:
        """Envia um csv para ser processado e cadastrado pelo model. Retorna uma exceção caso o arquivo não possa ser carregado"""
        try:
            self.cadastro = self.cadastro(self.nomeDoCsv)
            return True
        except FileNotFoundError:
            self.impressao.error_arquivo_nao_encontrado(self.nomeDoCsv)
            return False
        except ValueError:
            self.impressao.error_arquivo_nao_suportado(self.nomeDoCsv)
            return False


    def imprimir_cr_dos_aluno(self) -> None:
        """Envia os dados que recebeu do model para quea view possar apresenta-los"""
        self.impressao.imprimir_cr(self.cadastro.receber_matricula_e_cr())

    def imprimir_media_de_cr_por_curso(self) -> None:
        """Envia os dados que recebeu do model para quea view possar apresenta-los"""
        self.impressao.imprimir_media(self.cadastro.receber_cod_curso_e_todas_as_notas())


if __name__ == "__main__":
    ...