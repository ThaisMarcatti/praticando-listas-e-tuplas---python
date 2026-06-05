'''
Armano trabalha com a gestão de dois estoques de mercadorias que são representados como tuplas. Agora, ele precisa criar um relatório unificado com os produtos dos dois estoques juntos.

Para ajudá-lo, como você criaria um programa que ler as informações dos estoques e gera um relatório com todos os produtos juntos?
'''

class Estoque:
    def __init__(self, estoque1, estoque2):
        self.estoque1 = estoque1
        self.estoque2 = estoque2

    def gerar_relatorio_unificado(self):
        relatorio_unificado = self.estoque1 + self.estoque2
        return relatorio_unificado


# Exemplo de uso
estoque1 = ("Produto A", "Produto B", "Produto C")  
estoque2 = ("Produto D", "Produto E", "Produto F")
if __name__ == "__main__":
    estoque = Estoque(estoque1, estoque2)
    print(estoque.gerar_relatorio_unificado())
    


