produtos = [
    {"nome": "Notebook", "preco": 1200},
    {"nome": "Mouse", "preco": 25},
    {"nome": "Teclado", "preco": 75},
    {"nome": "Monitor", "preco": 900},
    {"nome": "Impressora", "preco": 1500},
]

produtosmaisdemil = [produto for produto in produtos if produto["preco"] > 1000]

print(produtosmaisdemil)