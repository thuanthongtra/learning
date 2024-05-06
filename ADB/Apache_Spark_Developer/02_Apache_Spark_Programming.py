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
# MAGIC ### Clusters
# MAGIC - Example with a Cluster has 1 Driver, 6 Workers. Each Worker has 1 Executor and 2 Cores.
# MAGIC   - Driver: brain of cluster which allocate tasks and data to worker nodes
# MAGIC   - Worker: receives tasks and data, performs and return result to Deiver

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
# MAGIC ![Narrow vs Wide Transformation](./images/Narrow_And_Wide_Transformation.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Process of Narrow Transformation
# MAGIC Example: Filter color != "brown". We have 12-16 memory partitions of data
# MAGIC - Step 1: Driver puts data files into 12-16 equal sized parition
# MAGIC - Step 2: Driver allocates 12 partitions to 12 Cores, each Core gets 1 partition --> Opps we still have 4 partitions left
# MAGIC - Step 3: 4 Cores finish early and return result to Driver. The other Cores are still processing
# MAGIC - Step 4: Driver allocates 4 partitions for another iteration to the 4 Cores. The other Cores finish
# MAGIC - Step 5: 4 Cores finish the 2nd iteration and return resul to Driver
# MAGIC - Step 6: Driver collects the result and delivers to the client
# MAGIC
# MAGIC ![Process of Narrow Transformation](./images/Narrow_Transformation_Example.png)

# COMMAND ----------

# MAGIC %md
# MAGIC #### Process of Wide Transformation
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
# MAGIC ![Process of Wide Transformation](./images/Wide_Transformation_Example.png)

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
# MAGIC
# MAGIC ![Query Optimization](./images/Query_Optimization.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Explain
# MAGIC ![Explain](./images/Explain.png)
# MAGIC
# MAGIC For each step, read from bottom to top
# MAGIC
# MAGIC **Step 1: Parsed Logical Plan**
# MAGIC - It is shown as the script is wrote: Inner Join then Filter
# MAGIC - Check the schema, e.g. lastname, firstname. dept... (no data types)
# MAGIC
# MAGIC **Step 2: Analyzed Logical Plan**
# MAGIC - Add data type to each column of schema in step 1
# MAGIC - Add CAST to ```dept``` to double as it is string
# MAGIC
# MAGIC It does not display all possible plans, but a optimized plan
# MAGIC
# MAGIC **Step 3: Optimized Logical Plan**
# MAGIC - Move the Filter before Join, to get less rows to join
# MAGIC
# MAGIC **Step 4: Physical PLan**
# MAGIC - Pick the best plan: Filter before Join and choose "Sort Merge Join" instead of "Inner Join"
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Cost Based Optimization (CBO): Smaller Tables Join
# MAGIC ![Cost Based Optimization (CBO)](./images/CBO.png)
# MAGIC
# MAGIC - Enable configurations: CBO, join reorder
# MAGIC - In script, (2) we join **```large```** table to **```medium```** table, then (1) we join **```small```** table
# MAGIC - In CBO step, it chooses to:
# MAGIC   - (1) get **```small```** table join with **```medium```** table then join with **```large```** table last
# MAGIC   - Afterward, (2) it does shuffle/exchange
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Adaptive Query Execution (AQE)
# MAGIC ![Adaptive Query Execution (AQE)](./images/AQE.png)
# MAGIC - After RDD created, Spark will look at Statistics and shuffle count to see how big they are. Then, it will turn back to Analyzed Logical Plan to see whether it can fine-tune the number of shuffle.
# MAGIC
# MAGIC
# MAGIC ![With And Without AQE](./images/With_Without_AQE.png)
# MAGIC - **Without AQE:** we (1) start with 4 memory partitions and (2) end up with 200 memory partitions. **_But why does it need to shuffle 200 partitions for only 568B?_**, which mean 2B foreach partition --> too small
# MAGIC - **With AQE:** we (1) start with 4 memory partitions and (2) end up with 1 partition, and much faster, even without parallism
# MAGIC
# MAGIC
# MAGIC ![Number of Jobs of AQE](./images/AQE_Number_Of_Jobs.png)
# MAGIC - Number of jobs **increase** from 1 to 3 (job #3, #4, #5)
# MAGIC   - Job #3 filters at WHERE clause to reduce size.
# MAGIC   - Job #4 with AQE, needs 1 Shuffle
# MAGIC - Hence, it **has cost overhead** with it, but it has benefit in long run

# COMMAND ----------

# MAGIC %md
# MAGIC ### Predicate Pushdown on RDDs
# MAGIC - Predicate Pushdown is when the data source actively **limits the number** of rows returned to Spark reader vi SELECT/WHERE/FILTER
# MAGIC - Predicate Pushdown filters the data in the database query,
# MAGIC   - Reducing the number of entries retrieved from the source database and 
# MAGIC   - Improving query performance
# MAGIC   - By default, the Spark Dataset API will automatically push down valid WHERE clauses to the database
# MAGIC - **Cast** function cannot be Pushed down
# MAGIC
# MAGIC ![Predicate Pushdown](./images/Predicate_Pushdown.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Caching - Best Practices
# MAGIC - Don't cach unless you're sure a DataFrame will be **used multiple times**
# MAGIC   - e.g. EDA (Exploratory Data Analysis), ML traning dataset
# MAGIC - Omit unneeded columns to reduce the storage footprint
# MAGIC - After calling `.cache()` which is **lazy transformation**, ensure all partitions are accessed with **Action**
# MAGIC   - e.g. `count()` - put RDD into Cache
# MAGIC - Manually evict cache when not needed
# MAGIC   - e.g. `unpersist()` - remove RDD from Cache

# COMMAND ----------

# MAGIC %md
# MAGIC ## Memory Partitioning

# COMMAND ----------

# MAGIC %md
# MAGIC ### Guidelines
# MAGIC - Error on the side of **too many small** than to few large Memory Partitions. If so large memory, then the core does not have enough memory, leading 2 possible consequences:
# MAGIC   - Spill to disk, waiting for more RAM, then bring it back
# MAGIC   - OOM: out of memory error
# MAGIC - Sweet spot initial size: **128MB and 1GB**
# MAGIC - Calculate the size of Shuffle partitions by dividing Shuffle stage input (4TB) by the target partition size (200MB).
# MAGIC   - e.g. 4TB / 200MB = 20,000 Shuffle Partition count
# MAGIC   - By default, it is 200 `spark.conf.get("spark.sql.shuffle.partitions")`
# MAGIC - Can manually set number of Shuffle Partitions on case-by-case basis
# MAGIC   - `spark.conf.set("spark.sql.shuffle.partitions", "20000")`
# MAGIC   - This setting is Local for **1 session** only.
# MAGIC
# MAGIC ![200_Default_Partitions](./images/200_Default_Partitions.png)
# MAGIC - Example: 
# MAGIC   - It starts with 8 partitions, then spawns 200 shuffle partitions
# MAGIC   - But there are only 42KB (~no thing) to write
# MAGIC   - Even some of tasks which means memory partitions reside has 0 bytes (blank)
# MAGIC   - It looks like AEQ turned off --> turn it on

# COMMAND ----------

# MAGIC %md
# MAGIC ### Cores in Cluster
# MAGIC - Initially, the Driver determines the number of Memory Partitions and its size. It decides based on:
# MAGIC   - Number of Cores in Cluster. 
# MAGIC   - More Cores, more Patitions.
# MAGIC - Get to number of Cores by 2 ways:
# MAGIC   - `sc.defaultParallelism` or `spark.sparkContext.defaultParallelism`
# MAGIC   - Spark UI -> Cores
# MAGIC   
# MAGIC   ![Spark UI](./images/Spark_UI_Cores.png)
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### No. of Memory Partition for DataFrame
# MAGIC - If Memory Partitions are sized too large (> 1GB), we can manually change in No. of Partitions (to higher number) to get them into a more reasonable size rang (**128MB** to **1GB**)
# MAGIC - AQE can resolve some Partitions issues
# MAGIC   - e.g. for small dataset, AQE won't create default 200 Shuffle Partitions, but rather a far lower number
# MAGIC - We need to **convert DataFrame into RDD** to get number of Partitions used for the DataFrame
# MAGIC   - `df.rdd.getNumPartitions()`

# COMMAND ----------

# MAGIC %md
# MAGIC ### Re-Partition a DataFrame
# MAGIC There are 2 ways:
# MAGIC 1. **`coalesce(int)`:**
# MAGIC     - Returns new DF with exactly N partitions when N < current No. of Partitions
# MAGIC     - **Narrow** transformation
# MAGIC     - Retain sort order
# MAGIC     - Only decrease No. of Partitions
# MAGIC
# MAGIC 2. **`repartition(int, [col])`:**
# MAGIC     - Return new DF with exactly N partitions
# MAGIC     - Evenly balanced partition sizes
# MAGIC     - **Wide** transformation
# MAGIC     - Not retain sort order
# MAGIC     - Both increase/decrease No. of Partition
# MAGIC
# MAGIC **Notes:**
# MAGIC   - More No. of Partition, less size
# MAGIC   - Less No. of Paritions, more size
