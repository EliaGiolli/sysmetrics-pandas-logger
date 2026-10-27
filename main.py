import logging
from datetime import datetime
import psutil

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
    """Responsabile della persistenza dei dati (riprendendo le tue basi con i file)."""
    
    def __init__(self, filename: str = "system_metrics.csv"):
        self.filename = filename

    def save(self, data: dict) -> None:
        # Qui implementerai la logica di scrittura su file CSV
        logging.info(f"Salvataggio metriche su {self.filename}: {data}")

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