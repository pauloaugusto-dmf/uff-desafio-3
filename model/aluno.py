from model.formulas import CrCalc
from typing import List, Dict, TypeVar

C = TypeVar('C', bound=CrCalc) #tipo responsavel por calcular o cr

class Aluno():
    """Classe responsavel por reprensentar um aluno"""
    def __init__(self, matricula: str, formulaDoCr: C = CrCalc) -> None:
        self._matricula: str = matricula
        self._notas: Dict[str, List[int]]= {}
        self._cr: C = formulaDoCr()

    def addNotas(self, codDic: str, nota: float, cargaHoraria: int) -> None:
        """Adiciona uma disciplina e a nota e carga horaria que esse aluno obteve nessa disciplina"""
        self._notas[codDic] = [nota, cargaHoraria]
        self.atualizar_cr()

    def removeNotas(self, codDic: str) -> List[int]:
        """Remove uma nota com basse no codigo da disciplina. Se a disciplina não estiver cadastrada levanta uma exceção"""
        return self._notas.pop(codDic)
        
    def atualizarNotas(self, codDic: str, Nota: float) -> None:
        """Atualiza uma nota com basse no codigo da disciplina. Se a disciplina não estiver cadastrada levanta uma exceção"""
        if(codDic in self._notas): self._notas[codDic][0] = Nota
        else: raise KeyError

    def atualizar_cr(self) ->  None:
        """Atualiza o cr do aluno"""
        nota: List[float] = [] 
        cargaHoraria: List[int] = []
        for i in self._notas:
            nota.append(self._notas[i][0])
            cargaHoraria.append(self._notas[i][1])
        self._cr.atualizar(nota, cargaHoraria)

    @property
    def matricula(self) -> str:
        return self._matricula

    @property
    def cr(self) -> C:
        return self._cr

    @property
    def notas(self) -> Dict[str, List[int]]:
        return self._notas

    def __str__(self) -> str:
        return f"Matricula {self._matricula} \nCR {self._cr} \nNotas {self._notas}"

if __name__ == "__main__":
    ...