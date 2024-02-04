-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC 
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>

-- COMMAND ----------

-- MAGIC %md
-- MAGIC # Connecting to an ADLS Gen2 Storage Account
-- MAGIC 
-- MAGIC In this demo you will learn how to:
-- MAGIC * Add data to Azure Databricks Unity Catalog metastore.
-- MAGIC * Read data from and write to an external storage location in Azure.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Prerequisites
-- MAGIC 
-- MAGIC If you would like to follow along with this demo, you will need:
-- MAGIC * Access to your Azure Portal with the ability to create a ADLS Gen2 storage account and an Azure Databricks Access Connector. 
-- MAGIC * Account administrator capabilities in your Databricks account with access to your Unity Catalog Data Explorer.
-- MAGIC 
-- MAGIC The resources you will need include:
-- MAGIC * An Azure Databricks Access Connector resource in Azure.
-- MAGIC * An Azure Data Lake Storage Gen2 Storage Account.
-- MAGIC * A CSV file with sample data to practice with.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Overview
-- MAGIC 
-- MAGIC Many use cases require the use of external storage. These use cases are often related to the storage of data assets outside the metastore bucket. These use cases include, but are not limited to:
-- MAGIC 
-- MAGIC * Migrating large datasets from a traditional Hive metastore to Unity Catalog. If there is a need to avoid the cost and time required to move this data, accessing them in place as a collection of external tables provides a viable alternative.
-- MAGIC * Use of external writers: that is, ongoing processes outside of your Azure Databricks deployment that write to the storage.
-- MAGIC * Strict business or regulalatory requirements that impose a hierarchy or naming convention on your storage.
-- MAGIC * Hard requirement for data isolation at the infrastructural level.
-- MAGIC * Requirement to manage data in a format that isn't Delta.
-- MAGIC 
-- MAGIC In this demonstration, we'll walk through how to add data files directly into the metastore and how to work with data in external storage.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Upload a file to Unity Catalog Data Explorer
-- MAGIC 
-- MAGIC Unity Catalog provides the option to upload a data file directly to Data Explorer. The steps are as listed below:
-- MAGIC 1. Create a new catalog in the metastore.
-- MAGIC 2. Create a new schema in the catalog.
-- MAGIC 3. Upload a CSV to create a table.
-- MAGIC 4. Grant appropriate permissions as necessary. 

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ###View table in a notebook
-- MAGIC Using the code below, you can view the table created in the metastore here in the notebook. Fill in the catalog name, schema name, and table name as it appears in the Data Explorer. 

-- COMMAND ----------

USE CATALOG <catalog_name>;
USE SCHEMA <schema_name>;
SELECT * from <table_name>;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Next, you can do work with the table and the results will be saved back to the catalog indicated previously. You can view the results from the Data Explorer window. 
-- MAGIC 
-- MAGIC The example below demonstrates creating a silver table using the `customers.csv` data filtered on the `loyalty_segment` column.

-- COMMAND ----------

CREATE TABLE silver_customers_highloyalty AS SELECT * FROM customers WHERE loyalty_segment=3

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Adding an External Location
-- MAGIC 
-- MAGIC External locations require a storage credential that is authroized with the ADLS Gen2 Storage Account as a Storage Blob Data Contributor in the Azure Portal. These two resources must exist in the Azure Portal before you begin. For this example, a demo-content container will be used from the trainingdemostorage storage account. 
-- MAGIC 
-- MAGIC To add an external data location to Unity Catalog, follow these steps in the Data Explorer:
-- MAGIC 1. In Unity Catalog, select Storage Credentials.
-- MAGIC 2. Select Create credential and complete the form using the details of your Azure Databricks Access Connector that has the Storage Blob Data Contributor role for your storage account in the Azure Portal. 
-- MAGIC 3. Click Create to complete the form.
-- MAGIC 4. Select External Locations.
-- MAGIC 5. Click Create location and complete the details for the storage account that will be the external location, including the URL that matches to the root path for the container. 
-- MAGIC 6. Select the appropriate storage credential that has permissions with the storage account and click Create to complete the form. 
-- MAGIC 
-- MAGIC It will verify the Storage Credential has appropriate permissions. Once complete, you can view your External Location from the Data Explorer. Once the external location is available, the appropriate permissions to users, service principals, and groups can be provided through Unity Catalog.

-- COMMAND ----------

-- MAGIC %md
-- MAGIC The following commands display the Storage Credentials and External Locations from Unity Catalog.

-- COMMAND ----------

SHOW STORAGE CREDENTIALS

-- COMMAND ----------

SHOW EXTERNAL LOCATIONS

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Next, you can execute the following commands to display the contents of the external location. Fill in your data for `<container-name>`, `<storage-account-name>`, and `<path>`, where the path leads to the folder containing your data file, starting at the first directory foler in your container.

-- COMMAND ----------

LIST 'abfss://<container-name>@<storage-account-name>.dfs.core.windows.net/<path>'

-- COMMAND ----------

-- MAGIC %md
-- MAGIC To view a table created using the data file, you can use the command below. The value of `<abfss://path>` is the same as the cell above. 

-- COMMAND ----------

SELECT * FROM CSV.`<abfss://path>`;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC As you can see, SQL does not give you the ability to infer the schema of the data into the column headers, so instead you can also create a data frame using Python, as seen below. 

-- COMMAND ----------

-- MAGIC %python
-- MAGIC df = (spark.read
-- MAGIC   .format("csv")
-- MAGIC   .option("header", "true")
-- MAGIC   .option("inferSchema", "true")
-- MAGIC   .load("abfss://<path>/<file>.csv")
-- MAGIC )
-- MAGIC display(df)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ## Dropping a table that was saved to external storage
-- MAGIC 
-- MAGIC This example points out that data persists even if the table is dropped when it is saved to the external location. 
-- MAGIC 
-- MAGIC The command below, creates a new external table in the storage account in Azure. If you review the Data Explorer, you will see that the table's meta data is stored in the Unity Catalog metastore. By viewing the storage account in Azure Portal, you can see the new table is now present. 

-- COMMAND ----------

CREATE TABLE silver_customers_highloyalty_external 
  LOCATION 'abfss://<path>/silver/'
  AS SELECT * FROM customers WHERE loyalty_segment=3

-- COMMAND ----------

-- MAGIC %md
-- MAGIC Now if we drop the table with the command below, you will see that it is no longer available in the metastore.

-- COMMAND ----------

DROP TABLE silver_customers_highloyalty_external

-- COMMAND ----------

-- MAGIC %md
-- MAGIC However, even though we dropped the table, the data files still remain in the Azure Portal (as seen with the command below or through viewing the storage account in the portal). This is intrinsic behaviour of an external table, which is the main differentiator between managed and external tables. When we drop a managed table, the data files are deleted as well. As it stands, you could recreate the table if desired, without having to specify source data again.

-- COMMAND ----------

LIST 'abfss://<path>/'

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
