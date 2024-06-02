from classes import CarrinhoDeCompras, Produto

carrinho = CarrinhoDeCompras()

product_1 = Produto('Camiseta', 50)
product_2 = Produto('Caneca', 15)
product_3 = Produto('Mouse', 150)
product_4 = Produto('Teclado', 250)

carrinho.insere_produtos(product_1)
carrinho.insere_produtos(product_2)
carrinho.insere_produtos(product_4)

carrinho.lista_produtos()
print(carrinho.soma_total())