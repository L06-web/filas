import heapq
import time

class Paciente:
    def __init__(self, nome, grav, chegada):
        self.nome = nome
        self.grav = grav
        self.chegada = chegada

    def __lt__(self, other):
        if self.grav == other.grav:
            return self.grav < other.grav
        return self.grav > other.grav


class Hospital: 
    def __init__(self):
        self.fila = []
        self.grav_map = {
            "1": 1,
            "2": 2,
            "3": 3
        }

    def agendar(self, nome, grav):
        chegada = time.time()
        gravidade = self.grav_map[grav]
        pac = Paciente(nome, gravidade, chegada)
        heapq.heappush(self.fila, pac)
        print(f"Paciente {nome} agendado com nível de gravidade {grav}.")

    def chamar(self):
        if self.fila:
            pac = heapq.heappop(self.fila)
            grav = [k for k, v in self.grav_map.items() if v == pac.grav][0]
            print(f"Paciente {pac.nome} chamado para atendimento (Gravidade: {grav}).")
        else:
            print("Fila vazia.")

    def excluir(self):
        self.fila.clear()
        print("Agendamentos excluídos.")

    def listar(self):
        if not self.fila:
            print("Sem pacientes agendados.")
            return
        print("Pacientes agendados:")
        for pac in sorted(self.fila):
            grav = [g for g, gp in self.grav_map.items() if gp == pac.grav][0]
            print(f"Nome: {pac.nome}, Gravidade: {grav}")

def menu():
    hospital = Hospital() 
    while True:
        print("\nMenu:")
        print("1 - Agendar")
        print("2 - Chamar")
        print("3 - Excluir")
        print("4 - Listar")
        print("5 - Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome: ")
            grav = input("""\nGravidade:
1 - Leve
2 - Grave
3 - Crítico
\nEscolha uma opção: """)
            hospital.agendar(nome, grav) 
        elif opcao == '2':
            hospital.chamar() 
        elif opcao == '3':
            hospital.excluir() 
        elif opcao == '4':
            hospital.listar() 
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Inválido.")

if __name__ == "__main__":
    menu()