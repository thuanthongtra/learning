# Databricks notebook source
# MAGIC %md
# MAGIC # Databricks and Apache Spark

# COMMAND ----------

# MAGIC %md
# MAGIC - **Row-Oriented data on disk (CSV):** data is stored in row wise basis (each record, ordered by column)
# MAGIC - **Column-Oriented data on disk (Parquet, Delta, ORC):** data is stored in column wise basis (all data in column 1, all data in column 2... ordered by row)
# MAGIC   - When we want to query column 1, 2, 3 then it only fetch those 3 column, not all like Row-Orientied
# MAGIC   - It keeps statistics, metadata, etc. has compression built-in

# COMMAND ----------

# DBTITLE 1,Parameterize via Widgets - Python
dbultils.widgets.text("Text", "Hello World!")
dbultils.widgets.dropdown("Dropdown", "1", [str (x) for x in rang(1,10)])
dbultils.widgets.combobox("Combobox", "A", ["A", "B", "C"])
dbultils.widgets.multiselect("Multiselect", "Yes", ["Yes", "No", "Maybe"])

# COMMAND ----------

# DBTITLE 1,Parameterize via Widgets - SQL
# MAGIC %sql
# MAGIC CREATE WIDGET TEXT state DEFAULT "CA"

# COMMAND ----------

# MAGIC %md
# MAGIC # Apache Spark Core

# COMMAND ----------

# MAGIC %md
# MAGIC ## SparkSQL
# MAGIC - It is a **module** for Structured data processing with multiple interfaces.
# MAGIC - It includes any object that has a Schema or Structure, including SQL tables, DataFrames API for Python, Scala, Java and R

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transformations
# MAGIC - DataFrame Transformations are **lazily** eveluated (Job won't start until having **Action**)
# MAGIC   - Schema eagerly evaludated by Driver, but Job not spawned
# MAGIC   - Benefit of "Lazy Evaludation": Spark can make Optimization decisions after it look at the DAG (Directed Acyclic Graph)
# MAGIC - Actions: are methods that trigger
# MAGIC   - Job is spawned
# MAGIC   - Examples: df.count(), df.collect(), df.show(), display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ## DataFrameReader
# MAGIC - Interface used to load a DataFrame from external storage
# MAGIC   - ```spark.read.csv("/Filestore/tables/LifeExp_headers.csv")```
# MAGIC - Explicit vs Implicit vs Infer Schema
# MAGIC   1. **Explicitly** define Schema _**without reading**_ data files
# MAGIC       ```
# MAGIC       DDL_schema = ("coutry STRING, lifeexp DOUBLE, region STRING)
# MAGIC       userDF = spark.read.option("header", True).schema(DDL_schema).csv("/Filestore/tables/LifeExp_headers.csv")
# MAGIC       ```
# MAGIC   2. **Implicitly** create default Column names and Data types _**without reading**_ data files
# MAGIC       ```
# MAGIC       df1 = spark.read.load("/Filestore/tables/LifeExp_headers.csv", format = "csv", header = False)
# MAGIC       display(df1)
# MAGIC       ```
# MAGIC   3. **Infer** column names and data types _**by reading**_ data files
# MAGIC       ```
# MAGIC       df2 = spark.read.load("/Filestore/tables/LifeExp_headers.csv", format = "csv", header = True, inferSchema = True)
# MAGIC       display(df2)
# MAGIC       ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## DataFrameWriter
# MAGIC - Write DataFrame to external storage
# MAGIC     ```
# MAGIC     df.write
# MAGIC       .format("delta)
# MAGIC       .mode("append")
# MAGIC       .save(outPath)
# MAGIC     ```
# MAGIC - Write as SQL table
# MAGIC     ```
# MAGIC     df.write
# MAGIC       .mode("overwrite")
# MAGIC       .saveAsTable("evants_p")
# MAGIC     ```

# COMMAND ----------

# MAGIC %md
# MAGIC ## Query Execution
# MAGIC We can express the same query using any interface. The Spark SQL engine generates the same query plan used to optimize and execute on our Spark cluster.
# MAGIC
# MAGIC ![query execution engine](https://files.training.databricks.com/images/aspwd/spark_sql_query_execution_engine.png)
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png" alt="Note"> Resilient Distributed Datasets (RDDs) are the low-level representation of datasets processed by a Spark cluster. In early versions of Spark, you had to write <a href="https://spark.apache.org/docs/latest/rdd-programming-guide.html" target="_blank">code manipulating RDDs directly</a>. In modern versions of Spark you should instead use the higher-level DataFrame APIs, which Spark automatically compiles into low-level RDD operations.

# COMMAND ----------

# MAGIC %md
# MAGIC # Spark Architect and Performance

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transformation

# COMMAND ----------

# DBTITLE 1,Narrow vs Wide Transformation
# MAGIC %md
# MAGIC ### Narrow vs Wide Transformation
# MAGIC - Narrow Transformation: 1-1 Partition
# MAGIC   - select, filter, cast, union
# MAGIC - Wide Transformation: Causes Shuffle/Exchange (Redistribution of data to new Partitions)
# MAGIC   - distinct, groupBy, sort, join
# MAGIC
# MAGIC ![Narrow vs Wide Transformation](Narrow_And_Wide_Transformation.png)
# MAGIC
# MAGIC ADB/Apache_Spark_Developer/images/Narrow_And_Wide_Transformation.png
# MAGIC https://adb-6218663240151630.10.azuredatabricks.net/?o=6218663240151630#files/3585101443092954

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ## Performance and Query Optimization

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ## Memory Partitioning
