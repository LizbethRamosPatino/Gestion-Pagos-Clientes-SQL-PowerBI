# Sistema de Gestión de Pagos y Cartera de Clientes

Este proyecto presenta un pipeline de datos integral (*end-to-end*) diseñado para la gestión, procesamiento y visualización del estado de cartera y pagos de clientes empresariales.

## 🛠️ Tecnologías Utilizadas
* **Base de Datos:** SQL Server (Vistas, Stored Procedures, CTEs)
* **Automatización / ETL:** Python (`pyodbc`)
* **Visualización:** Power BI (Dashboards interactivos)

## 📊 Arquitectura del Proyecto
1. **SQL Backend:** Creación de Vistas avanzadas (`V_ResumenPagos`, `Vista_UltimosPagosClientes`) para centralizar las reglas de negocio de saldos y montos solicitados.
2. **Procedimientos Almacenados:** Implementación de consultas parametrizadas para la extracción dinámica de datos por cliente.
3. **Power BI Reporting:** Conexión directa a las vistas de SQL Server para reflejar cobros y saldos pendientes en tiempo real.

> **Nota de confidencialidad:** Los datos utilizados en este proyecto corresponden a un escenario sintético/simulado para proteger información confidencial e identidades corporativas.
