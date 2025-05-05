produtos = [
    {"nome": "Notebook", "preco": 1200, "categoria": "Eletrônicos"},
    {"nome": "Mouse", "preco": 25, "categoria": "Eletrônicos"},
    {"nome": "Teclado", "preco": 75, "categoria": "Eletrônicos"},
    {"nome": "Camiseta", "preco": 50, "categoria": "roupas"},
    {"nome": "Calça", "preco": 120, "categoria": "roupas"},
    {"nome": "Livro", "preco": 80, "categoria": "Livros"},
    {"nome": "Impressora", "preco": 1500, "categoria": "Eletrônicos"},
    {"nome": "tenis", "preco": 90, "categoria": "roupas"},
    
]

contagem_por_categoria = {}

for produto in produtos:
    categoria = produto["categoria"]
    if categoria in contagem_por_categoria:
        contagem_por_categoria[categoria] += 1
    else:
        contagem_por_categoria[categoria] = 1

print(contagem_por_categoria)