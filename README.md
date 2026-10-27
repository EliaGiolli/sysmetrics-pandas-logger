# sysmetrics-pandas-logger

![Python](https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Psutil](https://img.shields.io/badge/Psutil-System_Monitoring-orange?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)

## Overview
`sysmetrics-pandas-logger` is a lightweight, object-oriented system metrics collector designed to practice modern Python architecture. It periodically queries core operating system metrics (such as CPU and memory usage) using `psutil` and handles incremental data persistence to CSV files leveraging `pandas`.

## Features
* Object-Oriented Programming (OOP) design separating concerns between data collection, business logic/reporting, and persistence.
* Automated safe CSV appending with dynamic header management to prevent data duplication.
* Built-in error logging and system threshold alerting.

## Next Steps
* **Network Monitoring**: Implement a new dedicated class to track network interface statistics and traffic.
* **Linux Migration**: Transition the execution environment from Windows 11 to a Linux virtual machine.
* **Advanced Persistence**: Evolve from local CSV files to a lightweight relational database (like SQLite) or expose metrics through an API endpoint.