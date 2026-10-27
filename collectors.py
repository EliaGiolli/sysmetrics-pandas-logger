import psutil

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
