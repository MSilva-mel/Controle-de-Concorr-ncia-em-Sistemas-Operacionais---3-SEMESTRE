import threading

class Coordenador:
    def __init__(self, id):
        self.id = id
        self.lock = threading.Lock()
        self.active = True

    def grant_access(self, processo):
        with self.lock:
            print(f"Coordenador {self.id} concedendo acesso ao processo {processo.id}")
            processo.access_section_critical()

    def stop(self):
        self.active = False
