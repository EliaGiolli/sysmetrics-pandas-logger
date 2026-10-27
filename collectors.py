import psutil
import logging

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


class NetworkMonitor:
    """Responsabile della raccolta delle metriche di rete e delle interfacce."""
    
    def get_network_io(self) -> list:
        try:
            # pernic=True restituisce un dizionario con chiave=interfaccia e valore=statistiche
            net_io = psutil.net_io_counters(pernic=True, nowrap=True)
            network_data = []
            
            for interface_name, stats in net_io.items():
                network_data.append({
                    "interface_name": interface_name,
                    "bytes_sent": stats.bytes_sent,
                    "bytes_recv": stats.bytes_recv,
                    "packets_sent": stats.packets_sent,
                    "packets_recv": stats.packets_recv
                })
            return network_data
            
        except Exception as e:
            logging.error(f"Errore nel recupero delle metriche di rete: {e}")
            return []
            
    def get_ip_nic_addresses(self) -> dict:
        try:
            return psutil.net_if_addrs()
        except Exception as e:
            logging.error(f"Impossibile recuperare gli indirizzi delle interfacce di rete: {e}")
            return {}