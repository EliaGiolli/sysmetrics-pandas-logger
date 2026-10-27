import logging
import os
from datetime import datetime
import psutil
import pandas as pd

# Configurazione di base del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SystemMetricsCollector:
    """Responsabile esclusivamente della raccolta delle metriche dal sistema operativo."""
    
    def get_cpu_usage(self) -> float:
        return psutil.cpu_percent(interval=1)

    def get_memory_usage(self) -> dict:
        mem = psutil.virtual_memory()
        return {
            "total": mem.total,
            "available": mem.available,
            "percent": mem.percent
        }

class MetricsReport:
    """Responsabile di elaborare, strutturare e applicare logiche di business (es. soglie di allarme)."""
    
    def __init__(self, cpu: float, memory: dict):
        self.timestamp = datetime.now().isoformat()
        self.cpu = cpu
        self.memory = memory

    def check_alerts(self, cpu_threshold: float = 80.0) -> None:
        if self.cpu > cpu_threshold:
            logging.warning(f"ATTENZIONE: Utilizzo CPU elevato! Rilevato al {self.cpu}%")

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp,
            "cpu_percent": self.cpu,
            "memory_percent": self.memory["percent"]
        }

class CSVMetricsRepository:
    """Responsabile della persistenza dei dati tramite Pandas."""
    
    def __init__(self, filename: str = "system_metrics.csv"):
        self.filename = filename

    def save(self, data: dict) -> None:
        cwd = os.getcwd()
        full_path = os.path.join(cwd, self.filename)
        
        # Verifichiamo se il file esiste già sul disco
        file_exists = os.path.exists(full_path)
        
        # Convertiamo il dizionario in un DataFrame di una singola riga
        df = pd.DataFrame([data])
        
        # Se il file esiste già: mode='a' (append) e header=False
        # Se non esiste: mode='a' crea il file, ma serve header=True per la prima riga
        df.to_csv(
            full_path, 
            mode='a', 
            index=False, 
            header=not file_exists
        )
        
        logging.info(f"Metriche salvate con successo in {full_path}")        

# Esecuzione del flusso orchestrato
if __name__ == "__main__":
    collector = SystemMetricsCollector()
    repository = CSVMetricsRepository()

    # Raccolta
    cpu = collector.get_cpu_usage()
    memory = collector.get_memory_usage()

    # Istanziazione dell'oggetto report (OOP)
    report = MetricsReport(cpu, memory)
    report.check_alerts()

    # Persistenza
    repository.save(report.to_dict())