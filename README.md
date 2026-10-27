# python-sys-mon

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Psutil](https://img.shields.io/badge/Psutil-System_Monitoring-orange?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)

## Overview
`python-sys-mon` is a lightweight, object-oriented system metrics collector designed following modern backend architecture principles. It periodically queries core operating system metrics (such as CPU, memory usage, and network interface I/O statistics) using `psutil` and handles incremental data persistence to structured CSV files leveraging `pandas`.

## Project Structure
```text
python-sys-mon/
│
├── collectors.py          # Handles OS data querying (CPU, Memory, Network I/O)
├── models.py              # Business logic, data formatting, and threshold alerts
├── repository.py          # Persistence layer handling dynamic CSV appending
├── main.py                # Application entry point and orchestrator
├── system_metrics.csv     # Log storage for CPU and memory usage
├── network_metrics.csv    # Log storage for network interface statistics
└── README.md              # Project documentation
```
## Features
- **Separation of Concerns (SoC)**: Modular OOP design dividing responsibilities across dedicated components for collection, business logic, and persistence.

- **Resilient Data Collection**: Defensive programming patterns using try-except blocks and error logging to ensure stability during system queries.

- **Tabular Flattening**: Automatic conversion of nested dictionary structures (such as multi-nic network statistics) into clean tabular formats via pandas.

- **Dynamic Persistence**: Smart CSV appending logic with automatic header management and dynamic routing for system and network data streams.

## Next Steps
- **Linux Migration**: Transition the execution environment from Windows 11 to a Linux virtual machine to validate cross-platform compatibility.

- **Database Integration**: Evolve from local CSV files to a lightweight relational database like `SQLite`.

- **API Exposure**: Expose collected metrics through a RESTful API endpoint using a modern web framework.