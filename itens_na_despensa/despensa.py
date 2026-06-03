'''
Roberto está organizando sua despensa e quer verificar se determinados itens já estão armazenados antes de adicioná-los à lista de compras.

Ajude Roberto a criar um programa que pergunte o item desejado e verifique se ele está na lista de itens disponíveis na despensa. Caso o item não esteja na lista, o programa deve informar que ele precisa ser comprado.
'''

class Despensa:
    def __init__(self):
        self.itens = []

        self.itens = ['arroz', 'feijão', 'macarrão', 'óleo', 'sal', 'açúcar'] #Itens pré-definidos como exemplo.

    def mostrar_menu(self):
        return 'Bem-vindo à despensa de Roberto! O que você gostaria de fazer?\n 1. Listar itens na despensa\n 2. Adicionar item à despensa\n3. Verificar se um item está na despensa\n 4. Sair'
    
    def listar_itens(self):
        if not self.itens:
            return 'A despensa está vazia.'
        else:
            return 'Itens na despensa: ' + ', '.join(self.itens)

    def adicionar_item(self, item):
        self.itens.append(item)

    def verificar_item(self, item):
        if item in self.itens:
            return f'{item} já está na despensa.'
        else:
            return f'{item} não está na despensa. Você precisa comprá-lo.'
        
    def input_opcao(self):
        while True:
            print(self.mostrar_menu())
            opcao = input('Digite o número da opção desejada: ')
            if opcao == '1':
                print(self.listar_itens())
            elif opcao == '2':
                item = input('Digite o nome do item que deseja adicionar: ')
                self.adicionar_item(item)
                print(f'{item} foi adicionado à despensa.')
            elif opcao == '3':
                item = input('Digite o nome do item que deseja verificar: ')
                print(self.verificar_item(item))
            elif opcao == '4':
                print('Saindo do programa. Até mais!')
                break
            else:
                print('Opção inválida. Por favor, tente novamente.')
                
def main():
    despensa = Despensa()
    despensa.input_opcao()


if __name__ == '__main__':
    main()




