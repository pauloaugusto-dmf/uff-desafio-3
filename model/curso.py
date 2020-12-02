from model.formulas import CursoCrMedia
from typing import Set, List, TypeVar

C = TypeVar('C', bound=CursoCrMedia) #tipo responsavel por calcular a media de cr de cada curso

class Curso():
    """Classe responsavel por reprensentar um curso"""
    def __init__(self, CodCurso: str, formulaDaMediaCr: C = CursoCrMedia) -> None:
        self._codCurso: str = CodCurso
        self._disciplinas: Set[str] = {0}
        self._notas: List[float] = []
        self._mediaCr: C = formulaDaMediaCr()

    def add_disciplinas_e_notas(self, disciplinas: Set[str], notas: List[float]) -> None:
        """Adiciona as disciplinas e todas as notas que os alunos dessas disciplinas obtiveram"""
        self._disciplinas = disciplinas
        self._notas = notas
        self.atualizar_media()

    def atualizar_media(self) -> None:
        """Atualiza a media do cr dos cursos"""
        self._mediaCr.atualizar(self._notas)

    @property
    def codCurso(self) -> str:
        return self._codCurso

    @property
    def disciplinas(self) -> Set[str]:
        return self._disciplinas

    @property
    def notas(self) -> List[float]:
        return self._notas

    @property
    def mediaCr(self) -> float:
        return self._mediaCr

if __name__ == "__main__":
    ...