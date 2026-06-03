'''
Uma escola realizou um concurso de redação, e o próximo passo é organizar as notas dos participantes para definir a ordem de premiação. Para garantir transparência, as notas precisam ser classificadas em ordem crescente, do menor para o maior valor.

Com base nisso, desenvolva um programa que receba como entrada uma lista contendo as notas de todos os participantes e exiba, ao final, essa lista ordenada em ordem crescente.
'''

class ClassificandoNotas:
    def __init__(self, notas):
        self.notas = notas

    def ordenar_notas(self):
        return sorted(self.notas)
    
    def exibir_notas_ordenadas(self):
        notas_ordenadas = self.ordenar_notas()
        print("Notas ordenadas em ordem crescente:")
        for nota in notas_ordenadas:
            print(nota)

# Exemplo de uso
if __name__ == "__main__":
    notas_participantes = [85, 92, 78, 90, 88]
    classificador = ClassificandoNotas(notas_participantes)
    classificador.exibir_notas_ordenadas()