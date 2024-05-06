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
# MAGIC   - Start with 1 memory partition, do transformations and data stay within the **same** memory partition
# MAGIC - Wide Transformation: Causes Shuffle/Exchange
# MAGIC   - distinct, groupBy, sort, join
# MAGIC   - Redistribute data and then create **new** memory partitions
# MAGIC   - Redistibuting or re-partitioning data so the data is grouped differently across partitions
# MAGIC     - Based on data size we may need to decrease/increase the number of Shuffle partitions via ```spark.sql.shffle.patitions```
# MAGIC
# MAGIC ![Narrow vs Wide Transformation](/images/Narrow_And_Wide_Transformation.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Clusters
# MAGIC - Example with a Cluster has 1 Driver, 6 Workers. Each Worker has 1 Executor and 2 Cores.
# MAGIC   - Driver: brain of cluster which allocate tasks and data to worker nodes
# MAGIC   - Worker: receives tasks and data, performs and return result to Deiver

# COMMAND ----------

# MAGIC %md
# MAGIC ### Process of Narrow Transformation
# MAGIC Example: Filter color != "brown". We have 12-16 memory partitions of data
# MAGIC - Step 1: Driver puts data files into 12-16 equal sized parition
# MAGIC - Step 2: Driver allocates 12 partitions to 12 Cores, each Core gets 1 partition --> Opps we still have 4 partitions left
# MAGIC - Step 3: 4 Cores finish early and return result to Driver. The other Cores are still processing
# MAGIC - Step 4: Driver allocates 4 partitions for another iteration to the 4 Cores. The other Cores finish
# MAGIC - Step 5: 4 Cores finish the 2nd iteration and return resul to Driver
# MAGIC - Step 6: Driver collects the result and delivers to the client
# MAGIC
# MAGIC ![Process of Narrow Transformation](/images/Narrow_Transformation_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Process of Wide Transformation
# MAGIC Example: Count total rows for each color. We have **19.5 MiB** data size, with 6 initial partitions
# MAGIC - Stage 1: Local cCount
# MAGIC   - Step 1: Driver allocates 6 partitions to 6 Cores, each Core gets 1 partition
# MAGIC   - Step 2: 6 Cores finish early and **write** the result into Disk in dictionary key:value, so the file is only **568B**. For example:
# MAGIC     - Core 2: Red:3, Blue:5, Yellow:7
# MAGIC     - Core 3: Red:4, Blue:4, Yellow:8
# MAGIC     - ...
# MAGIC     - Core 12: Red:7, Blue:5, Yellow:5
# MAGIC - Stage 2: Global Count
# MAGIC   - Step 1: Driver allocates Core 7 to read the counts and do the "Global Count", then send the result
# MAGIC   - Step 2: Core 7 **read** and sum the Local Counts and return the result to Driver
# MAGIC   - Step 3: Driver collects the result and delivers to the client
# MAGIC
# MAGIC ![Process of Wide Transformation](/images/Wide_Transformation_Exmaple.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Performance and Query Optimization
# MAGIC There are 5 plans:
# MAGIC
# MAGIC **Input: Query, no matter programming language -->**
# MAGIC 1. Unresolved Logical Plan
# MAGIC     - Drive reviews and confirms the **```schema correct?```**
# MAGIC
# MAGIC 2. Analyzed Logical Plan
# MAGIC     - Drive looks at **[Metadata Catalog] for ANALYSIS** and **```add data types```** to the columns
# MAGIC
# MAGIC 3. Optimized Logical Plan
# MAGIC     - Driver looks at **[Catalyst Catalog] for LOGICAL OPTIMIZATION** and check to apply number of rules-based (Filter, Join, etc.) to determine whether to **```move Filter before Join?```**
# MAGIC
# MAGIC 4. Physical Plan
# MAGIC     - Driver comes up with several ways (plans) to address the query **for PHYSICAL PLANNING** to determine **```which Join strategy to use, Data Skipping, Predicate Pushdown?```**
# MAGIC
# MAGIC 5. Selected Physical Plan
# MAGIC     - Driver puts ways in **[Cost Model] for WHOLE-STAGE CODE GENERATION** to see which way (plan) needs lowest cost = the best
# MAGIC     - The plan would be **```Java bytecode and sent to Executors```**
# MAGIC
# MAGIC **--> Output: RDD, no matter dataframe, sql table or view**

# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC ## Memory Partitioning