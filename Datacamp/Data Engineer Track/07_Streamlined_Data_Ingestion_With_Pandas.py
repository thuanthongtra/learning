# Databricks notebook source
# MAGIC %md
# MAGIC # Importing Data from Flat Files
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ## Read flat files

# COMMAND ----------

# Import pandas as pd
import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

# Read the CSV and assign it to the variable data
data = pd.read_csv('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/vt_tax_data_2016.csv')

# View the first few lines of data
print(data.head())

# Plot the total number of tax returns by income group
counts = data.groupby("agi_stub").N1.sum()
counts.plot.bar()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Modfiy flat files
# MAGIC Limit Columns:
# MAGIC - **`usecols`** keyword argument to choose column
# MAGIC - Accept list of column numbers or names, or function to filter column names
# MAGIC
# MAGIC
# MAGIC Limit Rows:
# MAGIC - **`nrows`** and **`skiprows`** together to process file in chunks
# MAGIC - **`skiprows`** accepts a lists of row numbers, number of rows, or function to filter rows
# MAGIC - Set **`header=None`** so Pandas knows there are no clumn names

# COMMAND ----------

# DBTITLE 1,Load with selected column
# Create list of columns to use
cols = ['zipcode','agi_stub','mars1','MARS2','NUMDEP']

# Create dataframe from csv using only selected columns
data = pd.read_csv('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/vt_tax_data_2016.csv', usecols = cols)

# View counts of dependents and tax returns by income level
print(data.groupby("agi_stub").sum())

# COMMAND ----------

# DBTITLE 1,Load with limited rows
vt_data_first500 = pd.read_csv('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/vt_tax_data_2016.csv', nrows=500)

# Create dataframe of next 500 rows with labeled columns
vt_data_next500 = pd.read_csv("/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/vt_tax_data_2016.csv", 
                       		  nrows=500,
                       		  skiprows=500,
                       		  header=None,
                       		  names=list(vt_data_first500)) #Thong: use list() to get column name of other dataframe

# View the Vermont dataframes to confirm they're different
print(vt_data_first500.head())
print(vt_data_next500.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Handling errors and missing data
# MAGIC Specify Data Type:
# MAGIC - **`dtype`** keyword argument to specify column data types
# MAGIC
# MAGIC Customize Missing Data Values:
# MAGIC - **`na_values`** keyword argument to set custom missing values
# MAGIC   - Can pass: single value, list, dictionary of columns and values
# MAGIC
# MAGIC Line with Errors:
# MAGIC - Set **`error_bad_lines=False`** to skip unparseble records
# MAGIC - Set **`warn_bad_lines=True`** to see messages when records are skipped

# COMMAND ----------

# DBTITLE 1,Convert Datatype
# Create dict specifying data types for agi_stub and zipcode
data_types = {'agi_stub': "category",
			  'zipcode': str}

# Load csv using dtype to set correct data types
data = pd.read_csv("/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/vt_tax_data_2016.csv", dtype=data_types)

# Print data types of resulting frame
print(data.dtypes.head())

# COMMAND ----------

# DBTITLE 1,Set customer NA
# Create dict specifying that 0s in zipcode are NA values
null_values = {'zipcode': 0}

# Load csv using na_values keyword argument
data = pd.read_csv("/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/vt_tax_data_2016.csv", 
                   na_values=null_values)

# View rows with NA ZIP codes
print(data[data.zipcode.isna()])

# COMMAND ----------

# MAGIC %md
# MAGIC # Importing Data From Excel Files
# MAGIC Similar to import data from csv, import data from excel we can define range of columns, i.e. B:E 

# COMMAND ----------

pip install openpyxl

# COMMAND ----------

# Load pandas as pd
import pandas as pd

# Read spreadsheet and assign it to survey_responses
survey_responses = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx')

# View the head of the dataframe
print(survey_responses.head())

# COMMAND ----------

# Create string of lettered columns to load column AD and the range AW through BA
col_string = "AD, AW:BA"

# Load data with skiprows and usecols set
survey_responses = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx', 
                        skiprows=2, 
                        usecols=col_string)

# View the names of the columns selected
print(survey_responses.columns)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Get Data From Multiple Worksheets
# MAGIC - **`sheet_name:`** keyword argument to lead other sheets
# MAGIC     - Specify spreadsheets by name and/or (zero-indexed) position number
# MAGIC     - Pass list of names/numbers to load more than 1 sheet at a time
# MAGIC     - **`sheet_name=None`** = load all sheets, return dictionary, key = sheet_name, value = dataframe

# COMMAND ----------

# Create df from second worksheet by referencing its name
responses_2017 = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                               sheet_name='2017',
                               skiprows=2)

# Check the column names in the DataFrame
print(responses_2017.columns)

# # Graph where people would like to get a developer job
job_prefs = responses_2017.groupby("JobPref").JobPref.count()
job_prefs.plot.barh()
plt.show()

# COMMAND ----------

# DBTITLE 1,loop dictionary with values()
responses = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                               sheet_name=None,
                               skiprows=2)

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for df in responses.values():
  # Print the number of rows being added
  print("Adding {} rows".format(df.shape[0]))
  # Concatenate all_responses and df, assign result
  all_responses = pd.concat([all_responses, df])

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

# COMMAND ----------

# DBTITLE 1,loop dictionary with items()
responses = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                               sheet_name=None,
                               skiprows=2)

# Create an empty dataframe
all_responses = pd.DataFrame()

# Set up for loop to iterate through values in responses
for sheet_name, df in responses.items():
  # Print the number of rows being added
  print("Adding {} for {} rows".format(sheet_name, df.shape[0]))
  # Concatenate all_responses and df, assign result
  all_responses = pd.concat([all_responses, df])

# Graph employment statuses in sample
counts = all_responses.groupby("EmploymentStatus").EmploymentStatus.count()
counts.plot.barh()
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Modify Import Data: True/False
# MAGIC - **`pandas`** loads **`True`** / **`False`** columns as float data by default
# MAGIC - Specify a column should be **`bool`** with **`read_excel()`** 's **`dtype`** argument
# MAGIC - Boolean columns can only have True and False values
# MAGIC - **NA/missing values in Boolean columns are changed to True**
# MAGIC - **`pandas`** automatically recognizes some values as **`True`** / **`False`** in Boolean columns
# MAGIC - Unrecognized values in a Boolean column are also changed to **`True`**

# COMMAND ----------

# MAGIC %md
# MAGIC ### Setting Custom True/False Values
# MAGIC - Use **`read_excel()`** 's 
# MAGIC   - **`true_values`** to set custom True values
# MAGIC   - **`false_values`** to set custom False values
# MAGIC - Custom **`True`** / **`False`** values are only applied to columns set as Boolean

# COMMAND ----------

# Load file with Yes as a True value and No as a False value
survey_subset = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                                sheet_name=0,
                                skiprows=2,
                                dtype={"HasDebt": bool,
                                "AttendedBootCampYesNo": bool},
                                true_values=['Yes'],
                                false_values=['No'])

# View the data
print(survey_subset.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Modify Import Data: Parsing Date
# MAGIC - Datetime columns are loaded as objects (strings) by default
# MAGIC - Specify that columns have datetimes with the **`parse_dates`** argument (not **`dtype`** !)
# MAGIC - **`parse_dates`** can accept:
# MAGIC   - a list of column names or numbers to parse
# MAGIC   - a list containing lists of columns to combine and parse
# MAGIC   - a dictionary where keys are new column names and values are lists of columns to parse together

# COMMAND ----------

# MAGIC %md
# MAGIC ### Non-Standard Dates
# MAGIC - **`parse_dates`** doesn't work with non-standard datetime formats
# MAGIC - Use **`pd.to_datetime()`** after loading data if **`parse_dates`** won't work
# MAGIC - **`to_datetime()`** arguments:
# MAGIC   - Dataframe and column to convert
# MAGIC   - **`format`** : string representation of datetime format
# MAGIC - Datetime Formatting
# MAGIC   - %Y = Year (4-digit) i.e. 1999
# MAGIC   - %m = Month (zero-padded) i.e .03
# MAGIC   - %d = Day (zero-padded) i.e. 01
# MAGIC   - %H = Hour (24-hour clock) i.e. 21
# MAGIC   - %M = Minute (zero-padded) i.e. 09
# MAGIC   - %S = Second (zero-padded) i.e. 05

# COMMAND ----------

# DBTITLE 1,Simple Date
# Load file, with Part1StartTime parsed as datetime data
survey_data = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                                sheet_name=0,
                                skiprows=2,
                                parse_dates=['Part1StartTime'])

# Print first few values of Part1StartTime
print(survey_data.Part1StartTime.head())

# COMMAND ----------

# DBTITLE 1,Date of multiple columns
# Create dict of columns to combine into new datetime column
datetime_cols = {"Part3Start": ['Part3StartDate','Part3StartTime']} #Thong: it auto combines date + time


# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                                sheet_name=0,
                                skiprows=2,
                                parse_dates=datetime_cols)

# View summary statistics about Part3Start
print(survey_data.Part3Start.describe())
print(survey_data.Part3Start)

# COMMAND ----------

# Load file, supplying the dict to parse_dates
survey_data = pd.read_excel('/Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/fcc-new-coder-survey.xlsx',
                                sheet_name=0,
                                skiprows=2,
                                parse_dates=datetime_cols)

print(survey_data["Part4StartTime"].head())

# Parse datetimes and assign result back to Part4StartTime
survey_data["Part4StartTime"] = pd.to_datetime(survey_data["Part4StartTime"], 
                                             format="%m%d%Y %H:%M:%S")

# Print first few values of Part4StartTime
print(survey_data["Part4StartTime"].head())

# COMMAND ----------

# MAGIC %md
# MAGIC # Importing Data from Databases

# COMMAND ----------

pip install sqlalchemy

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# Load libraries
import pandas as pd
from sqlalchemy import create_engine, inspect, text

# Create the database engine
engine = create_engine('sqlite:////Volumes/learning_datacamp/de_associate/07_streamlined_data_ingestion_with_pandas/data.db')

# COMMAND ----------

# Save the table names to a list: table_names
inspection = inspect(engine)
table_names = inspection.get_table_names()

# Print the table names to the shell
print(table_names)

# Print the column names to the shell
for table_name in inspection.get_table_names():
    print("----Table: %s----" % table_name)
    for column in inspection.get_columns(table_name):
        print("Column: %s" % column['name'])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Querying Data SQL

# COMMAND ----------

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute(text("SELECT * FROM Weather"))

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
# df.columns = rs.keys()

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Using Pandas to Directly Query Data

# COMMAND ----------

with engine.connect() as con:
    # Execute query and store records in DataFrame: df
    df = pd.read_sql_query(text("SELECT * FROM Weather"), con)

# Print head of DataFrame
print(df.head())

# COMMAND ----------

import matplotlib.pyplot as plt

# Query the database and assign result to safety_calls
with engine.connect() as con:
    # Execute query and store records in DataFrame: df
    safety_calls = pd.read_sql(text('''SELECT * 
                            FROM hpd311calls 
                            WHERE complaint_type = 'SAFETY'
                            '''), con)

# Graph the number of safety calls by borough
call_counts = safety_calls.groupby('borough').unique_key.count()
call_counts.plot.barh()
plt.show()

# COMMAND ----------

# Query database and assign result to wintry_days
with engine.connect() as con:
    # Create query for records with max temps <= 32 or snow >= 1
    wintry_days = pd.read_sql(text('''SELECT *
                                        FROM weather
                                        WHERE  tmax <= 32
                                        OR snow >=1;
                                    '''), con)

# View summary stats about the temperatures
print(wintry_days.describe())

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md
# MAGIC # Importing JSON Data and Working with APIs

# COMMAND ----------

# MAGIC %md
# MAGIC ## Get Data from API

# COMMAND ----------

# MAGIC %md
# MAGIC ### requests.get()
# MAGIC - requests.get(url_string) to get data from a URL
# MAGIC - Keyword 
# MAGIC   - argumentsparams keyword: takes a dictionary of parameters and values to customize API request
# MAGIC   - headers keyword: takes a dictionary, can be used to provide user authentication to API
# MAGIC - Result: a response object, containing data and metadata
# MAGIC   - response.json() will return just the JSON data
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### response.json() and pandas
# MAGIC - response.json() returns a dictionary
# MAGIC - read_json() expects strings, not dictionaries
# MAGIC - Load the response JSON to a dataframe with pd.DataFrame()
# MAGIC   - read_json() will give an error!
# MAGIC

# COMMAND ----------

import requests
import pandas as pd
api_url = "https://api.yelp.com/v3/businesses/search"

# Set up parameter dictionary according to documentation
params = {"term": "bookstore", "location": "San Francisco"}

# Set up header dictionary w/ API key according to documentation
api_key = 'mhmt6jn3SFPVC1u6pfwgHWQvsa1wmWvCpKRtFGRYlo4mzA14SisQiDjyygsGMV2Dm7tEsuwdC4TYSA0Ai_GQTjKf9d5s5XLSNfQqdg1oy7jcBBh1i7iQUZBujdA_XHYx'
headers = {"Authorization": "Bearer {}".format(api_key)}

# Call the API
response = requests.get(api_url, params=params, headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data['businesses'])
print(cafes.head())

# Thong: The result
#                                   alias ...                                            url
# 0 city-lights-bookstore-san-francisco   ... https://www.yelp.com/biz/city-lights-bookstore...
# 1 alexander-book-company-san-francisco  ... https://www.yelp.com/biz/alexander-book-compan...
# [2 rows x 16 columns]

# COMMAND ----------

# MAGIC %md
# MAGIC ## Nested JSON

# COMMAND ----------

# MAGIC %md
# MAGIC ### pandas.io.json
# MAGIC - pandas.io.json submodule has tools for reading and writing JSON
# MAGIC   - Needs its own import statement
# MAGIC - json_normalize()
# MAGIC   - Takes a dictionary/list of dictionaries (like pd.DataFrame() does)
# MAGIC   - Returns a flattened dataframe
# MAGIC   - Default flattened column name pattern: attribute.nestedattribute
# MAGIC   - Choose a different separator with the sep argument
# MAGIC

# COMMAND ----------

import pandas as pd
import requests
from pandas.io.json import json_normalize

# Set up headers, parameters, and API endpoint
api_url = "https://api.yelp.com/v3/businesses/search"
api_key = 'mhmt6jn3SFPVC1u6pfwgHWQvsa1wmWvCpKRtFGRYlo4mzA14SisQiDjyygsGMV2Dm7tEsuwdC4TYSA0Ai_GQTjKf9d5s5XLSNfQqdg1oy7jcBBh1i7iQUZBujdA_XHYx'
headers = {"Authorization": "Bearer {}".format(api_key)}
params = {"term": "bookstore", "location": "San Francisco"}

# Make the API call and extract the JSON data
response = requests.get(api_url,headers=headers,params=params)
data = response.json()

# Flatten data and load to dataframe, with _ separators
bookstores = json_normalize(data["businesses"], sep="_")
print(list(bookstores))

# Thong: the result:
# ['alias',  'categories', 'coordinates_latitude', 'coordinates_longitude', ... 'location_address1', 'location_address2', 'location_address3', 'location_city', 'location_country', 'location_display_address', 'location_state', 'location_zip_code', ... 'url']

print(bookstores.categories.head())

# Thong: the result:
# 0   [{'alias': 'bookstores', 'title': 'Bookstores'}]
# 1   [{'alias': 'bookstores', 'title': 'Bookstores'...
# 2   [{'alias': 'bookstores', 'title': 'Bookstores'}]
# 3   [{'alias': 'bookstores', 'title': 'Bookstores'}]
# 4    [{'alias': 'bookstores', 'title': 'Bookstores'...
# Name: categories, dtype: object

# COMMAND ----------

# MAGIC %md
# MAGIC ### Deeply Nested Data
# MAGIC - json_normalize()
# MAGIC   - record_path: string/list of string attributes to nested data
# MAGIC   - meta: list of other attributes to load to dataframe
# MAGIC   - meta_prefix: string to prefix to meta column names
# MAGIC

# COMMAND ----------

# Flatten categories data, bring in business details
df = json_normalize(data["businesses"]
                    ,sep="_"
                    ,record_path="categories",
                    meta=["name",
                          "alias",
                          "rating",
                          ["coordinates", "latitude"],
                          ["coordinates", "longitude"]],
                    meta_prefix="biz_")

print(df.head(4))

# Thong: The result
#         alias               title                biz_name  \
# 0  bookstores          Bookstores   City Lights Bookstore   
# 1  bookstores          Bookstores  Alexander Book Company   
# 2  stationery  Cards & Stationery  Alexander Book Company   
# 3  bookstores          Bookstores       Borderlands Books                                 

#                               biz_alias  biz_rating  biz_coordinates_latitude  \
# 0   city-lights-bookstore-san-francisco         4.5                 37.797600   
# 1  alexander-book-company-san-francisco         4.5                 37.788585   
# 2  alexander-book-company-san-francisco         4.5                 37.788585   
# 3       borderlands-books-san-francisco         5.0                 37.758984      

#    biz_coordinates_longitude  
# 0                -122.406578  
# 1                -122.400631  
# 2                -122.400631  
# 3                -122.421638


# COMMAND ----------

# MAGIC %md
# MAGIC ## Combine Multiple Dataset

# COMMAND ----------

# MAGIC %md
# MAGIC ### Concatenating
# MAGIC - Use case: adding rows from one dataframe to another
# MAGIC - concat()
# MAGIC   - pandas function
# MAGIC   - Syntax: pd.concat([df1,df2])
# MAGIC   - Set ignore_index to True to renumber rows

# COMMAND ----------

# Get first 20 bookstore results
params = {"term": "bookstore", "location": "San Francisco"}  
first_results = requests.get(api_url,
                             headers=headers,
                             params=params).json()
first_20_bookstores = json_normalize(first_results["businesses"],
                                     sep="_")

print(first_20_bookstores.shape)

# Thong: The result
# (20, 24)

# COMMAND ----------

# Get the next 20 bookstores
params["offset"] = 20
next_results = requests.get(api_url,                            
                            headers=headers,                            
                            params=params).json()

next_20_bookstores = json_normalize(next_results["businesses"],                                    
                                    sep="_")

print(next_20_bookstores.shape)

# Thong: The result
# (20, 24)

# COMMAND ----------

# Put bookstore datasets together, renumber rows
bookstores = pd.concat([first_20_bookstores, next_20_bookstores],                        
                       ignore_index=True)
print(bookstores.name)

# Thong: The result
# 0                             City Lights Bookstore
# 1                            Alexander Book Company
# 2                                 Borderlands Books
# 3                                   Alley Cat Books
# 4                                   Dog Eared Books
# ...                                             ...
# 35                                     Forest Books
# 36                San Francisco Center For The Book
# 37                           KingSpoke - Book Store
# 38                            Eastwind Books & Arts
# 39                                      My Favorite
# Name: name, dtype: object

# COMMAND ----------

# MAGIC %md
# MAGIC ### Merging
# MAGIC - Use case: combining datasets to add related columns
# MAGIC - Datasets have key column(s) with common values
# MAGIC - merge(): pandas version of a SQL join
# MAGIC   -Both a pandas function and a dataframe method
# MAGIC - df.merge() arguments
# MAGIC   - Second dataframe to merge
# MAGIC   - Columns to merge on
# MAGIC     - on if names are the same in both dataframes
# MAGIC     - left_on and right_on if key names differ
# MAGIC     - Key columns should be the same data type

# COMMAND ----------

call_counts.head()  
# Thong: The result
#   created_date  call_counts
# 0   01/01/2018         4597
# 1   01/02/2018         4362
# 2   01/03/2018         3045
# 3   01/04/2018         3374
# 4   01/05/2018         4333

weather.head()  
# Thong: The result       
#         date    tmax  tmin  
# 0  12/01/2017      52    42  
# 1  12/02/2017      48    39  
# 2  12/03/2017      48    42  
# 3  12/04/2017      51    40  
# 4  12/05/2017      61    50

# COMMAND ----------

# Merge weather into call counts on date columns
merged = call_counts.merge(weather,
                           left_on="created_date",                            
                           right_on="date")
print(merged.head())  

# Thong: the result
#   created_date  call_counts        date  tmax  tmin
# 0   01/01/2018         4597  01/01/2018    19     7
# 1   01/02/2018         4362  01/02/2018    26    13
# 2   01/03/2018         3045  01/03/2018    30    16
# 3   01/04/2018         3374  01/04/2018    29    19
# 4   01/05/2018         4333  01/05/2018    19     9
