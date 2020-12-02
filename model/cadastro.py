import pandas as pd
from model.aluno import Aluno
from model.curso import Curso
from typing import List, Dict, Tuple, TypeVar

A = TypeVar('A', bound=Aluno) #tipo que representa um aluno
C = TypeVar('C', bound=Curso) #tipo que representa um curso 

class Cadastro:
    """
    Classe responsavel por cadastrar os alunos e cursos com base em um arquivo csv
    """
    def __init__(self, nomeDoArquivo: str, aluno: A = Aluno, curso: C = Curso) -> None:
        self.dados = ''
        self.aluno = aluno
        self.curso = curso
        self.alunos: List[A] = []
        self.cursos: List[C] = []
        self._carregar_arq_csv(nomeDoArquivo)

    def _carregar_arq_csv(self, nomeDoArquivo: str) -> bool:
        """Carrega os dados do arquivo csv para a classe Cadastro"""
        try:
            dados = pd.read_csv(nomeDoArquivo)
            if self._validar_arq_csv(dados): 
                self.dados = dados
                self._cadastrar_alunos_do_csv()
                self._cadastrar_cursos_do_csv()
            else: 
                raise ValueError('csv carregado não é suportado pelo sistema')
        except FileNotFoundError:
            raise
        except ValueError:
            raise
            

    def _validar_arq_csv(self, dados) -> bool:
        """Valida se o csv carregado é suportado pelo sistema"""
        if not(tuple(dados.columns) == ('MATRICULA', 'COD_DISCIPLINA', 'COD_CURSO', 'NOTA', 'CARGA_HORARIA', 'ANO_SEMESTRE')):
            return False
        return True

    def _cadastrar_alunos_do_csv(self) -> None:
        """Cadastra todos os alunos lidos no csv"""
        matriculas = self.dados['MATRICULA'].unique()
        for matricula in matriculas:
            dadosDoAluno =  self.dados[self.dados['MATRICULA'] == matricula]
            disciplinas: List[str] = list(dadosDoAluno['COD_DISCIPLINA'])
            nota: List[int] = list(dadosDoAluno['NOTA'])
            cargaHoraria: List[int] = list(dadosDoAluno['CARGA_HORARIA'])
            aluno: A = self.aluno(matricula)
            for i in range(0, len(disciplinas)):
                aluno.addNotas(disciplinas[i], nota[i], cargaHoraria[i])
            self.alunos.append(aluno)

    def _cadastrar_cursos_do_csv(self) -> None:
        """Cadastra todos os cursos lidos no csv"""
        cursos = self.dados['COD_CURSO'].unique()
        for curso in cursos:
            disciplinas = self.dados[self.dados['COD_CURSO'] == curso]
            objCurso = self.curso(curso)
            objCurso.add_disciplinas_e_notas(set(disciplinas['COD_DISCIPLINA']), list(disciplinas['NOTA']))
            self.cursos.append(objCurso)

            
    def receber_matricula_e_cr(self) -> Tuple[str, float]:
        """Devolve a matricula e o cr de todos os alunos cadastrados"""
        return [(aluno._matricula, aluno.cr.cr) for aluno in self.alunos]

    def receber_cod_curso_e_todas_as_notas(self) -> Dict[str, float]:
        """Devolve o codigo de curso e a media de cr de todos os curso cadastrados"""
        return {curso.codCurso: curso.mediaCr.mediaCr for curso in self.cursos}
        


if __name__ == "__main__":
    ...
    