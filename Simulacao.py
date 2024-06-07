import time
import threading
from Processo import Processo
from Coordenador import Coordenador
from Eleicao import algoritmo_valentao

if __name__ == "__main__":
    # Inicializar processos
    processos = [Processo(i) for i in range(5)]
    
    # Inicializar coordenador
    coordenador = Coordenador(0)
    for p in processos:
        p.coordenador = coordenador
    
    # Inicializar threads para processos
    threads = []
    for p in processos:
        t = threading.Thread(target=p.run)
        threads.append(t)
        t.start()
    
    # Deixar os processos rodarem por um tempo
    time.sleep(10)
    
    # Simular falha do coordenador
    print("Coordenador falhou.")
    coordenador.stop()
    algoritmo_valentao(processos, coordenador.id)
    
    # Deixar os processos rodarem por mais um tempo
    time.sleep(10)
    
    # Parar todos os processos
    for p in processos:
        p.stop()
    for t in threads:
        t.join()

    print("Simulação terminada.")
