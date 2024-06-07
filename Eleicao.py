from Coordenador import Coordenador

def algoritmo_valentao(processos, falha_id):
    candidatos = [p for p in processos if p.id > falha_id and p.active]
    if candidatos:
        novo_coordenador = max(candidatos, key=lambda p: p.id)
        novo_coordenador_coordenador = Coordenador(novo_coordenador.id)
        for p in processos:
            p.coordenador = novo_coordenador_coordenador
        print(f"Novo coordenador eleito: Processo {novo_coordenador.id}")
    else:
        print("Nenhum coordenador disponível.")
