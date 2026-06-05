'''
Camila adora receber amigos para jantares temáticos. Para o próximo encontro, ela quer garantir que a ordem de chegada seja respeitada, mas ainda precisa fazer ajustes na lista de convidados. Camila quer adicionar novos nomes e organizá-los em posições específicas.

Como você criaria um programa que mostre a lista inicial, permita a inserção de um novo nome em uma posição escolhida e exiba a lista atualizada?
'''

class ListaDeConvidados:
    def __init__(self):
        self.convidados = []

    def adicionar_convidado(self, nome, posicao=None):
        if posicao is not None and 0 <= posicao < len(self.convidados):
            self.convidados.insert(posicao, nome)
        else:
            self.convidados.append(nome)

    def mostrar_lista(self):
        print('Lista de Convidados:')
        for index, convidado in enumerate(self.convidados):
            print(f'{index + 1}. {convidado}')

# Exemplo de uso
if __name__ == '__main__':
    lista = ListaDeConvidados()
    
    # Convidados iniciais
    convidados_iniciais = ['Alice', 'Bob', 'Charlie']
    
    # Adicionando convidados iniciais à lista
    for convidado in convidados_iniciais:
        lista.adicionar_convidado(convidado)
    
    # Mostrando a lista inicial
    lista.mostrar_lista()
    
    # Adicionando um novo convidado em uma posição específica
    nome_novo_convidado = input('\nDigite o nome do novo convidado: ')
    posicao_novo_convidado = int(input('Digite a posição onde o convidado será inserido: '))
    lista.adicionar_convidado(nome_novo_convidado, posicao_novo_convidado)
    
    # Mostrando a lista atualizada
    print('\nLista Atualizada:')
    lista.mostrar_lista()