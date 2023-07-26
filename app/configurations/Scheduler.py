from apscheduler.schedulers.background import BackgroundScheduler
from ..extensions.FuncoesScheduler import teste

class Scheduler:

    def __init__(self):
        self.scheduler = BackgroundScheduler()

    def start(self):
        self.scheduler.start()
        self.testeScheduler()
        
    def testeScheduler(self):
        self.scheduler.add_job(func=teste, trigger="interval", seconds=10)  # Executa a cada 30 minutos
    
