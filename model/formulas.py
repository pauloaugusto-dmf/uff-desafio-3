from typing import List

class CrCalc():
    """Classe responsalvel por calcular o cr de um aluno"""
    def __init__(self, cr = 0) -> None:
        self._cr: float = cr

    def atualizar(self, notas: float, cargaHoraria: int) -> None:
        """
        Atualiza o cr com base na formula onde o cr = Nota(i)*CargaHoraria(i)/TotalCargaHoraria
        Onde i é a i-ésima turma de um aluno
        """
        cr = 0
        for i in range(0, len(notas)):
            cr += (notas[i] * cargaHoraria[i])
            self._cr = cr/sum(cargaHoraria)

    @property
    def cr(self) -> float:
        return self._cr

    def __str__(self) -> str:
        return f"{self._cr}"

class CursoCrMedia():
    """Classe responsalvel por calcular a media do cr de um curso"""
    def __init__(self) -> None:
        self._mediaCr: float = 0

    def atualizar(self, notas: List[float]) -> None:
        """
        Atualiza a media de cr com base na formula onde a media de cr é igual 
        ao somatorio de todas as notas dividido pela quantidade de notas
        """
        self._mediaCr = sum(notas)/len(notas)

    @property
    def mediaCr(self) -> float:
        return self._mediaCr

    def __str__(self) -> str:
        return f"{self._mediaCr}"
    