-- ==============================================================================
-- MODEL: dbt Gold Risk Scoring Model (finance_gold_risk_scores.sql)
-- AUTHOR: Abhishek Das (Senior Data & Analytics Engineer)
-- DESCRIPTION: Generates customer risk profiles and fraud audit feeds
-- ==============================================================================

{{ config(materialized='table', schema='gold') }}

SELECT 
    customer_id,
    account_type,
    COUNT(transaction_id) AS total_transactions_24h,
    SUM(transaction_amount) AS total_volume_usd,
    SUM(high_risk_flag) AS risk_trigger_count,
    CASE 
        WHEN SUM(high_risk_flag) >= 3 THEN 'CRITICAL_LOCK'
        WHEN SUM(high_risk_flag) >= 1 THEN 'SUSPICIOUS'
        ELSE 'NORMAL'
    END AS risk_status
FROM {{ ref('silver_transactions') }}
GROUP BY customer_id, account_type
