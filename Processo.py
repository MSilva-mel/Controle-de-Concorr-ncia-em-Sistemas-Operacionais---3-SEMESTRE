import threading
import time
import random

class Processo:
    def __init__(self, id, coordenador=None):
        self.id = id
        self.coordenador = coordenador
        self.is_coordinator = False
        self.active = True
        self.lock = threading.Lock()

    def request_access(self):
        if self.coordenador and self.coordenador.active:
            print(f"Processo {self.id} solicitando acesso ao coordenador {self.coordenador.id}")
            self.coordenador.grant_access(self)
        else:
            print(f"Processo {self.id}: Coordenador {self.coordenador.id if self.coordenador else 'N/A'} inativo ou não definido.")

    def access_section_critical(self):
        print(f"Processo {self.id} acessando a seção crítica.")
        time.sleep(random.uniform(0.1, 1))
        print(f"Processo {self.id} saindo da seção crítica.")

    def run(self):
        while self.active:
            time.sleep(random.uniform(1, 5))
            self.request_access()

    def stop(self):
        self.active = False
