from datetime import datetime
import logging

# Configurazione di base del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


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
