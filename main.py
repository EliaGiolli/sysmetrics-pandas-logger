# Internal imports
from collectors import SystemMetricsCollector
from models import MetricsReport
from repository import CSVMetricsRepository


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