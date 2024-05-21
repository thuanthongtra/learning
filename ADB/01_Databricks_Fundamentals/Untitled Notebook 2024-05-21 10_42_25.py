# Databricks notebook source
# MAGIC %md
# MAGIC # History of Data Mgmt Platform

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Warehouse
# MAGIC - In late 1980s, businesses need more than relational databases --> data warehouse
# MAGIC
# MAGIC **Pros:**
# MAGIC - Business Intelligence (BI)
# MAGIC - Analytics
# MAGIC - Structured & clean data
# MAGIC - Predefined schemas
# MAGIC
# MAGIC **Cons:**
# MAGIC - No support for semi or unstructured data
# MAGIC - Inflexible schemas
# MAGIC - Struggle with volumne and velocity upsticks
# MAGIC - Long processing time

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Lakes
# MAGIC - In early 2000s, Big Data explosion --> Data Lake
# MAGIC
# MAGIC **Pros:**
# MAGIC - Flexible data storage
# MAGIC - Streaming support
# MAGIC - Cost efficient in the cloud
# MAGIC - Support for AI and ML
# MAGIC
# MAGIC **Cons:**
# MAGIC - No transactional support
# MAGIC   - Poor data reliability, data quality
# MAGIC - Slow analysis performance
# MAGIC - Data Gov concerns security, privacy
# MAGIC - Data warehouses still needed

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Lakehouse
# MAGIC - In 2021, advent of Lakehouse architect paradigm
# MAGIC - An opent unified foundation for all data
# MAGIC ![Data Lakehouse Overview](./images/Data_Lakehouse_Overview.npg)
# MAGIC
# MAGIC - It combines the benefits of Data Lake and analytical power of Data Warehouse
# MAGIC - It is built on top of Data Lake = all datatypes to be stored together = **1 unified source of truth**
# MAGIC - It provides direct access for BI and AI to work together with **unified security, governance and cataloging components**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Key features:
# MAGIC - **Transactional support:** access transactions for concurent read/write interactions
# MAGIC - **Schema enforcement and governance:** for data integrity and auditing needs
# MAGIC - **Data governance:** for data privacy regulations and data use metrics
# MAGIC - **BI support:** reduces latency of obtaining data and drawing insights
# MAGIC - **Decouple storage from compute:** each operation on its own cluster, allowing to scale independently
# MAGIC - **Open storage formats:** apache parquet, so variety of tools can access and manipulate data
# MAGIC - **Support for diverse data types:** structured, semi-structured, unstructured
# MAGIC - **Support for diverse workloads:** DE, ML, AI workloads
# MAGIC - **End-to-end streaming**: for real-time reports, remove the need of intermediate systems
