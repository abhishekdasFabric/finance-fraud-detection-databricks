# ==============================================================================
# PIPELINE: Azure Databricks Streaming Transaction Ingestion & Anomaly Filter
# AUTHOR: Abhishek Das (Senior Data & Analytics Engineer)
# DESCRIPTION: Stream ingestion from Kafka/MongoDB into Delta Lake with risk scoring
# ==============================================================================

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr

# Structured Streaming from Transaction Queue
streaming_df = (
    spark.readStream
    .format("delta")
    .table("finance_lakehouse.bronze_transactions_stream")
    .filter(col("transaction_amount") > 0)
    .withColumn("high_risk_flag", expr("CASE WHEN transaction_amount > 10000 AND foreign_country = 1 THEN 1 ELSE 0 END"))
)

query = (
    streaming_df.writeStream
    .format("delta")
    .outputMode("append")
    .option("checkpointLocation", "/mnt/delta/checkpoints/fraud_silver")
    .table("finance_lakehouse.silver_transactions")
)

print("Databricks Structured Streaming Fraud Filter Active.")
