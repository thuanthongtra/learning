# Databricks notebook source
# MAGIC %md
# MAGIC # Charts

# COMMAND ----------

# MAGIC %md
# MAGIC ## Determine 1 Items in Multiple Categories
# MAGIC In a hierarchy, there could be cases when 1 item belongs to multiple hierarchies. So how can we determine this item?
# MAGIC
# MAGIC ![](./images/Tips/Tip_Grap_Chart.png)
# MAGIC 1. **_Product Family Hierarchy_** has levels: Product Family > Product Department > Product Category
# MAGIC 2. We can use **_Force-Directed Graph_** chart to illustrate which items belong to which higher hierachies
# MAGIC 3. We can see: 
# MAGIC     - **_Dairy_** belongs to Drink and Food
# MAGIC     - **_Specialty_** belongs to Food and Non-Consum
