from pprint import pprint
from typing import Tuple, Dict, List

class Impressao():
    def imprimir_cr(self, matricula_cr:  Tuple[str, float]) -> None:
        """Mostra na tela uma lista com a matricula e o cr dos alunos"""
        print('------- O CR dos alunos é: --------')
        for i in matricula_cr:
            print(f'  {i[0]}  -  {i[1]:.2f}')
        print('-----------------------------------\n')
        

    def imprimir_media(self,  codCurso_Notas: Dict[str, float]) -> None:
        """Mostra na tela uma lista com os codigos dos cursos e a media de cr deles"""
        print('----- Média de CR dos cursos ------')
        for i in codCurso_Notas:
            print(f'  {i} - { codCurso_Notas[i]:.2f}')
        print('-----------------------------------\n')

    def error_arquivo_nao_encontrado(self, nomeDoCsv: str) -> None:
        """Mensagem de erro que é disparada caso o arquivo csv não seja encontrado"""
        print('--------------- Error ---------------')
        print(f' Arquivo \'{nomeDoCsv}\' não encontrado\n Verifique se o arquivo existe ou\n se foi corretamente digitado')
        print('-------------------------------------\n')

    def error_arquivo_nao_suportado(self, nomeDoCsv: str) -> None:
        """Mensagem de erro que é disparada caso o arquivo csv não seja compativel com o sistema"""
        print('---------------------- Error ----------------------')
        print(f' Arquivo \'{nomeDoCsv}\' não é suportado pelo sistema')
        print('---------------------------------------------------\n')