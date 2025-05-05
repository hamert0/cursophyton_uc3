class Colaborador:
    def __init__(self, id, nome, salario):
        self.id = id
        self.nome = nome
        self.salario = salario

class SistemaColaboradores:
    def __init__(self):
        self.colaboradores = {}  # Dicionário para armazenar colaboradores, usando o ID como chave

    def adicionar_colaborador(self, colaborador):
        if colaborador.id in self.colaboradores:
            print(f"Erro: Colaborador com ID {colaborador.id} já existe.")
        else:
            self.colaboradores[colaborador.id] = colaborador
            print(f"Colaborador {colaborador.nome} (ID: {colaborador.id}) adicionado com sucesso.")

    def buscar_colaborador(self, id):
        if id in self.colaboradores:
            return self.colaboradores[id]
        else:
            print(f"Colaborador com ID {id} não encontrado.")
            return None

    def listar_colaboradores_salario_acima_de(self, salario_minimo):
        colaboradores_filtrados = [
            colaborador.nome
            for colaborador in self.colaboradores.values()
            if colaborador.salario > salario_minimo
        ]
        if colaboradores_filtrados:
            print(f"Colaboradores com salário acima de R$ {salario_minimo}:")
            for nome in colaboradores_filtrados:
                print(f"- {nome}")
        else:
            print(f"Não há colaboradores com salário acima de R$ {salario_minimo}.")


sistema = SistemaColaboradores()


colaborador1 = Colaborador(1, "Ana Silva", 3500)
colaborador2 = Colaborador(2, "Pedro Souza", 5000)
colaborador3 = Colaborador(3, "Carla Oliveira", 2800)
colaborador4 = Colaborador(2, "Novo Pedro", 6000) # Tentando adicionar com ID duplicado

sistema.adicionar_colaborador(colaborador1)
sistema.adicionar_colaborador(colaborador2)
sistema.adicionar_colaborador(colaborador3)
sistema.adicionar_colaborador(colaborador4)

print("-" * 20)


colaborador_encontrado = sistema.buscar_colaborador(1)
if colaborador_encontrado:
    print(f"Colaborador encontrado (ID: {colaborador_encontrado.id}): {colaborador_encontrado.nome}, Salário: R$ {colaborador_encontrado.salario}")

colaborador_nao_encontrado = sistema.buscar_colaborador(5)

print("-" * 20)


sistema.listar_colaboradores_salario_acima_de(3000)
sistema.listar_colaboradores_salario_acima_de(6000)