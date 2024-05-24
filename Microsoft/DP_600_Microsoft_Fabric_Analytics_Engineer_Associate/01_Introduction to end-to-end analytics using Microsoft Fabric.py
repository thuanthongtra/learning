# Databricks notebook source
# MAGIC %md
# MAGIC # Introduction
# MAGIC **Microsoft Fabric** is an end-to-end analytics platform that provides a **single**, **integrated environment** for data professionals and the business to collaborate (ingest, store, process, and analyze) on data projects
# MAGIC
# MAGIC Fabric is built on **Power BI** and **Azure Data Lake Storage**, and includes capabilities from **Azure Synapse Analytics**, **Azure Data Factory**, **Azure Databricks**, and **Azure Machine Learning**.

# COMMAND ----------

# MAGIC %md
# MAGIC # OneLake
# MAGIC **OneLake** is Fabric's lake-centric architecture that provides a single, integrated environment
# MAGIC - It eliminaties the need to move and copy data between different systems and teams
# MAGIC   - **`OneCopy`** is a key component of OneLake that allows you to read data from a **single copy**, without moving or duplicating data
# MAGIC - All the compute workloads in Fabric are **preconfigured** to work with OneLake. 
# MAGIC   - Fabric's data warehousing, data engineering (Lakehouses and Notebooks), data integration (pipelines and dataflows), real-time intelligence, and Power BI all use OneLake as their native store without needing any extra configuration.
# MAGIC
# MAGIC ![One Lake](./images/01/fabric-introduction.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## OneLake Storage
# MAGIC
# MAGIC ![One Lake Storage](./images/01/onelake-storage.png)
# MAGIC
# MAGIC - OneLake is built on top of **Azure Data Lake Storage (ADLS)** and data can be stored in any format, including Delta, Parquet, CSV, JSON, and more.
# MAGIC   - All of the compute engines in Fabric automatically **store their data in OneLake**. 
# MAGIC   - Data that is stored in OneLake is then **directly accessible** by all of the compute engines without needing to be moved or copied. 
# MAGIC   - For tabular data, the analytical engines in Fabric will write data in **delta-parquet format** and all engines interact with the format seamlessly.
# MAGIC
# MAGIC - One important feature of OneLake is the ability to **create shortcuts**, which are embedded references within OneLake that point to other files or storage locations. 
# MAGIC   - Shortcuts allow you to quickly source your existing cloud data without having to copy it, and enables Fabric experiences to derive data from the same source to **always be in sync**.

# COMMAND ----------

# MAGIC %md
# MAGIC # Enable and use Microsoft Fabric
# MAGIC The permissions required to enable Fabric are either:
# MAGIC - Fabric admin
# MAGIC - Power Platform admin
# MAGIC - Microsoft 365 admin

# COMMAND ----------

# MAGIC %md
# MAGIC ## Enable Microsoft Fabric
# MAGIC If you have admin privileges, you can access **Admin center** from **Settings** menu in the upper right corner of Power BI service. From here, you enable Fabric in the **Tenant settings**.
# MAGIC   - Admins can make Fabric available to either 
# MAGIC     - the entire organization or 
# MAGIC     - specific groups of users, who can be organized based on their Microsoft 365 or Microsoft Entra security groups. 
# MAGIC   - Admins can also delegate the ability to enable Fabric to other users, at the capacity level.
# MAGIC
# MAGIC ![Enable Microsoft Fabric](./images/01/enable-fabric.png)
# MAGIC
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png" alt="Note"> If your organization isn't using Fabric or Power BI today, you can sign up for a [free Fabric trial](https://learn.microsoft.com/en-us/fabric/get-started/fabric-trial) to explore the different workloads.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create Fabric enabled workspaces
# MAGIC All Fabric items (lakehouses, notebooks, pipelines, etc.) are stored in OneLake and accessed via Fabric workspaces. To enable Fabric in a workspace, choose a Trial or Fabric Capacity license mode.
# MAGIC
# MAGIC ![Create Fabric enabled workspaces](./images/01/workspace-settings-license.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create items in Fabric
# MAGIC You can create items in Fabric using the **Create menu** in the upper left corner of the Power BI service.
# MAGIC
# MAGIC ![Create items in Fabric](./images/01/fabric-create.png)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Explore Fabric workloads
# MAGIC Fabric workloads refer to the different capabilities included in Fabric. You can switch between workloads using the workload switcher in the bottom left corner of the navigation pane.
# MAGIC
# MAGIC ![Create items in Fabric](./images/01/workspace-switcher.png)
