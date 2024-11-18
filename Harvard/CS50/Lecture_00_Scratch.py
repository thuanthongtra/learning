# Databricks notebook source
# MAGIC %md
# MAGIC URL: ```https://www.youtube.com/watch?v=3LPJfIKxwWc&list=PLhQjrBD2T381WAHyx1pq-sBfykqMBI7V4&index=1```

# COMMAND ----------

# MAGIC %md
# MAGIC #Binary
# MAGIC - Bit = **Bi**nary Digi**t**
# MAGIC - base-2 = exponent of 2.
# MAGIC   - For example, ### can be calculated as (from right to left):
# MAGIC     - 1st # = 2^0
# MAGIC     - 2nd # = 2^1
# MAGIC     - 3rd # = 2^2
# MAGIC     - ...
# MAGIC   - Then 
# MAGIC     - 100 represents 2^2 + 0 + 0 = 4
# MAGIC     - 101 represents 2^2 + 0 + 2^0 = 5
# MAGIC - Byte = ######## = 8 bits
# MAGIC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # ASCII 
# MAGIC ASCII (American Standard Code for Information Interchange) uses **8 bit** per character the represents letters
# MAGIC   - Letter **A** = 65 = 01000001

# COMMAND ----------

# MAGIC %md
# MAGIC # Unicode
# MAGIC Unicode is a superset of ASCII. It sometimes uses **16 bits (2 bytes)** or **24 bits (3 bytes)** or even **32 bits (4 bytes)** per character ~4mil characters
# MAGIC - For non-English characters such as emoji
# MAGIC - However, it is not for people to recognize long - 32 bits characters. Hence, Unicode uses another system called **base-16** or **hexadecimal** e.g. U+1F602
# MAGIC - Unicode can be combined to get defined display of combination of emoji, color, etc. e.g. thumb up, black thumb up

# COMMAND ----------

# MAGIC %md
# MAGIC # Color RGB
# MAGIC - Color has combination of Red, Green, Blue, e.g. 72 | 73 | 33 = 72/255 Red | 73/255 Green | 33/255 Blue
# MAGIC - Each point of color is **1 pixel = 3 bytes**, e.g. a picture has 3000 bytes = 1000 pixel
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC # Algorithm
# MAGIC - Input -> **Algorithm** -> Output
# MAGIC - Example, find name John in yellow book, 1000 pages
# MAGIC   - Algorithm 1: turn each page -> **1000 steps**
# MAGIC   - Algorithm 2: turn 2 page nad reverse 1 page if same J -> **500 + 1 steps**
# MAGIC   - Algorithm 3: go to middle of book, then letter M (J in the left of M), then go to the middle of left half of book, continue... -> just 3 steps, we reduce 1000 to 500, then to 250 pages... we could do it gor roughly **10 steps**

# COMMAND ----------

# MAGIC %md
# MAGIC # Artificial Intelligence
# MAGIC - There needs to be a way to get algorithm more generally, 
# MAGIC   - to feed input from all of the internet, all of the www, all of the pages and textual content and 
# MAGIC   - let it **figure out** based on the input how to answer
# MAGIC - Large Language Model (LLM): 
# MAGIC   - take input of lots of languages and 
# MAGIC   - infer from **the patterns** of English words or any human language to answer

# COMMAND ----------

# MAGIC %md
# MAGIC # Scratch
# MAGIC https://scratch.mit.edu/
