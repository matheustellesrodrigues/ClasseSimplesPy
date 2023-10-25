class Carrinho():
    def __init__(self, nome, preco, produto):
        self.nome = nome
        self.preco = float(preco)
        self.produto = produto
itens = Carrinho("Fanta", 5.99, "Liquido")
print(f"O nome do produto é: {itens.nome} ")
print(f"O preço do produto é: {itens.preco}")
print(f"O tipo do produto é: {itens.produto}")