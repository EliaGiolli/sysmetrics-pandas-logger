import os
import logging
import pandas as pd

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
