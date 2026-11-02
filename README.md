# finance-fraud-detection-databricks
Real-time financial transaction ingestion and fraud risk scoring engine built with Azure Databricks, PySpark Structured Streaming, Delta Lake, and dbt.
# Real-Time Financial Fraud Detection & Risk Pipeline
[![Databricks](https://img.shields.io/badge/Azure_Databricks-PySpark-red)](https://databricks.com) [![dbt](https://img.shields.io/badge/dbt-Data_Build_Tool-orange)](https://getdbt.com) [![Delta Lake](https://img.shields.io/badge/Delta_Lake-Streaming-00ADF0)](https://delta.io)

High-performance real-time financial transaction risk-scoring pipeline designed to detect fraud patterns and feed executive monitoring dashboards.

## 🏗️ Architecture & Pipeline Flow
- **Ingestion:** Structured Streaming in **Azure Databricks** reading high-frequency transaction streams from NoSQL (MongoDB) and Kafka endpoints.
- **Transformation:** PySpark streaming notebooks compute risk velocity triggers and isolate cross-border high-value transaction anomalies.
- **Modeling (dbt):** **dbt (Data Build Tool)** SQL transformations build Gold layer customer risk profiles and audit feeds.
- **Analytics:** Power BI reporting with automated alerts for high-risk accounts.

## 🛠️ Tech Stack
Azure Databricks, PySpark Structured Streaming, dbt, MongoDB, Delta Lake, Power BI, T-SQL.
