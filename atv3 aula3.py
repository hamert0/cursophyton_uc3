pedidos = [
    {"id": 1, "item": "Camiseta", "quantidade": 2},
    {"id": 2, "item": "Calça", "quantidade": 1},
    {"id": 1, "item": "Camiseta", "quantidade": 2},  
    {"id": 3, "item": "Tênis", "quantidade": 1},
    {"id": 2, "item": "Calça", "quantidade": 1},  
    {"id": 4, "item": "Meias", "quantidade": 3},
]


pedidos_unicos_tuplas = set(tuple(pedido.items()) for pedido in pedidos)


pedidos_unicos = [dict(tupla) for tupla in pedidos_unicos_tuplas]

print(pedidos_unicos)