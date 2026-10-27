# Internal imports
from collectors import SystemMetricsCollector, NetworkMonitor
from models import MetricsReport
from repository import CSVMetricsRepository


# Esecuzione del flusso orchestrato
if __name__ == "__main__":
    collector = SystemMetricsCollector()
    net_stats = NetworkMonitor()

    system_repository = CSVMetricsRepository("system_metrics.csv")
    network_repository = CSVMetricsRepository("network_metrics.csv")

    # Raccolta
    cpu = collector.get_cpu_usage()
    memory = collector.get_memory_usage()
    net_metrics = net_stats.get_network_io()

    # Report di sistema
    report = MetricsReport(cpu, memory)
    report.check_alerts()

    # Persistenza separata
    system_repository.save(report.to_dict())
    network_repository.save(net_metrics)