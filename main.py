from controllers.calcularCr import CalcularCr

if __name__ == "__main__":
    notas = CalcularCr('notas.csv')
    controle = notas.cadastrar_csv()
    if(controle):
        notas.imprimir_cr_dos_aluno()
        notas.imprimir_media_de_cr_por_curso()