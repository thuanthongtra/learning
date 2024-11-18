# Databricks notebook source
# MAGIC %md
# MAGIC # Getting to know PySpark

# COMMAND ----------

# MAGIC %md
# MAGIC ##What is Spark, anyway?
# MAGIC
# MAGIC Spark is a platform for cluster computing. Spark lets you spread data and computations over _**clusters**_ with multiple _**nodes**_ (think of each node as a separate computer). Splitting up your data makes it easier to work with very large datasets because each node only works with a small amount of data.
# MAGIC
# MAGIC As each node works on its own subset of the total data, it also carries out a part of the total calculations required, so that both data processing and computation are performed _**in parallel**_ over the nodes in the cluster. It is a fact that parallel computation can make certain types of programming tasks much faster.

# COMMAND ----------

# MAGIC %md
# MAGIC ##Using Spark in Python
# MAGIC The first step in using Spark is connecting to a cluster.
# MAGIC
# MAGIC In practice, the cluster will be hosted on a remote machine that's connected to all other nodes. There will be one computer, called the _**master**_ that manages splitting up the data and the computations. The master is connected to the rest of the computers in the cluster, which are called _**worker**_. The master sends the workers data and calculations to run, and they send their results back to the master.
# MAGIC
# MAGIC Creating the connection is as simple as creating an instance of the **`SparkContext`** class. The class constructor takes a few optional arguments that allow you to specify the attributes of the cluster you're connecting to.
# MAGIC
# MAGIC An object holding all these attributes can be created with the **`SparkConf()`** constructor. Take a look at the [documentation](https://spark.apache.org/docs/2.1.0/api/python/pyspark.html) for all the details!

# COMMAND ----------

# Import necessary libraries
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder \
    .appName() \
    .getOrCreate()

# Create spark context
sc = spark.sparkContext

print(spark)
print(sc)
print(sc.version)

# COMMAND ----------

# DBTITLE 1,Spark Session to read CSV
# Define the path to your CSV file
file_path = "/Volumes/learning_datacamp/big_data_with_pyspark/01_introduction_to_pyspark/flights_small.csv"

# Read the CSV file into a DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Show the first few rows of the DataFrame
df.show()

# Define the table name to be used for querying
table_name = "flights"

# Save the DataFrame to the cluster as a table for further querying
df.write.mode("overwrite").saveAsTable(table_name)

# COMMAND ----------

# Execute a SQL query to retrieve the location of the "flights" table
result = spark.sql("DESCRIBE EXTENDED flights").filter("col_name = 'Location'")

# Retrieve the location from the result
location = result.select("data_type").collect()[0][0]

# Print the storage location of the "flights" table
print(location)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Using DataFrames
# MAGIC
# MAGIC Spark's core data structure is the Resilient Distributed Dataset (RDD). This is a low level object that lets Spark work its magic by splitting data across multiple nodes in the cluster. However, RDDs are hard to work with directly, so in this course you'll be using the _**Spark DataFrame**_ abstraction built on top of _**RDDs**_.
# MAGIC
# MAGIC The Spark DataFrame was designed to behave a lot like a SQL table (a table with variables in the columns and observations in the rows). Not only are they easier to understand, DataFrames are also more optimized for complicated operations than RDDs.
# MAGIC
# MAGIC When you start modifying and combining columns and rows of data, there are many ways to arrive at the same result, but some often take much longer than others. When using RDDs, it's up to the data scientist to figure out the right way to optimize the query, but the DataFrame implementation has much of this optimization built in!
# MAGIC
# MAGIC To start working with Spark DataFrames, you first have to create a **`SparkSession`** object from your **`SparkContext`**. You can think of the **`SparkContext`** as your connection to the cluster and the **`SparkSession`** as your interface with that connection.

# COMMAND ----------

# DBTITLE 1,Spark df
# Don't change this query
query = "FROM flights SELECT * LIMIT 10"

# Get the first 10 rows of flights
flights10 = spark.sql(query)

# Show the results
flights10.show()

# COMMAND ----------

# DBTITLE 1,Spark df to Pandas df
# Don't change this query
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"

# Run the query
flight_counts = spark.sql(query)

# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# Print the head of pd_counts
print(pd_counts.head())

# COMMAND ----------

# DBTITLE 1,Pandas df to Spark df
import numpy as np
import pandas as pd

# Create pd_temp
pd_temp = pd.DataFrame(np.random.random(10))

# Create spark_temp from pd_temp
spark_temp = spark.createDataFrame(pd_temp) 
# Thong: 
# The .createDataFrame() method takes a pandas DataFrame and returns a Spark DataFrame. The output of this method is stored locally, not in the SparkSession catalog. This means that you can use all the Spark DataFrame methods on it, but you can't access the data in other contexts.
# For example, a SQL query (using the .sql() method) that references your DataFrame will throw an error. To access the data in this way, you have to save it as a temporary table.

# Examine the tables in the catalog
print(spark.catalog.listTables()) #Thong: only flights table

# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView("temp")
# Thong:
# This method registers the DataFrame as a table in the catalog, but as this table is temporary, it can only be accessed from the specific SparkSession used to create the Spark DataFrame.

# Examine the tables in the catalog again
print(spark.catalog.listTables()) #Thong: flights + temp tables

# COMMAND ----------

# MAGIC %md
# MAGIC # Manipulating data

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Getting started with machine learning pipelines

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Model tuning and selection

# COMMAND ----------



# COMMAND ----------


