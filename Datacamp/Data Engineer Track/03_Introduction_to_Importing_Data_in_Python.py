# Databricks notebook source
# MAGIC %md
# MAGIC # Introduction to Importing Data in Python

# COMMAND ----------

# MAGIC %md
# MAGIC ## Text file

# COMMAND ----------

# DBTITLE 1,Importing entire text files
# Open a file: file
file = open("/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/moby_dick.txt", mode="r")

# Print it
print(file.read())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)

# COMMAND ----------

# DBTITLE 1,Importing text files line by line - using context manager "with"
# Read & print the first 3 lines
with open('/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Using Numpy

# COMMAND ----------

# Import package
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

# Assign filename to variable: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/mnist_kaggle_some_rows.csv'

# Load file as array: digits
digits = np.loadtxt(file, delimiter=',')

# Print datatype of digits
print(type(digits))

# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))

# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC There are a number of arguments that np.loadtxt() takes that you'll find useful:
# MAGIC
# MAGIC - delimiter changes the delimiter that loadtxt() is expecting.
# MAGIC   - You can use ',' for comma-delimited.
# MAGIC   - You can use '\t' for tab-delimited.
# MAGIC - skiprows allows you to specify how many rows (not indices) you wish to skip
# MAGIC - usecols takes a list of the indices of the columns you wish to keep.

# COMMAND ----------

# Import numpy
import numpy as np

# Assign the filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/mnist_kaggle_some_rows.csv'

# Load the data: skip the first row and import the first and third columns.
data = np.loadtxt(file, delimiter=',', skiprows=1, usecols=[0,3])

# Print data
print(data)

# COMMAND ----------

# Assign filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/seaslug.txt'

# Import file: data with setting the data type argument dtype equal to str
data = np.loadtxt(file, delimiter='\t', dtype=str)

# Print the first element of data
print(data[0])

# Import data as floats and skip the first row: data_float
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)

# Print the 10th element of data_float
print(data_float[9])

# Plot a scatterplot of the data
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()


# COMMAND ----------

# DBTITLE 1,Mixed datatype - np.genfromtxt()
#If we pass dtype=None to it, it will figure out what types each column should be
data = np.genfromtxt('/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/titanic_sub.csv', delimiter=',', names=True, dtype=None)

#print last 4 values of Survived column
print(data['Survived'][-4:])

# COMMAND ----------

# DBTITLE 1,Mixed datatype - np.recfromcsv()
#function np.recfromcsv() that behaves similarly to np.genfromtxt(), except that its default dtype is None

# Assign the filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/titanic_sub.csv'

# Import file using np.recfromcsv: d
d = np.recfromcsv(file, delimiter=',', names=True, dtype=None)

# Print out first three entries of d
print(d[:3])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Using Pandas

# COMMAND ----------

# Import pandas as pd
import pandas as pd

# Assign the filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/titanic_sub.csv'

# Read the file into a DataFrame: df
df = pd.read_csv(file)

# View the head of the DataFrame
print(df.head())

# COMMAND ----------

# Assign the filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/digits.csv'

# Read the first 5 rows of the file into a DataFrame: data
data = pd.read_csv(file, nrows = 5, header = None)
print(data)

# Build a numpy array from the DataFrame: data_array
data_array = data.values

# Print the datatype of data_array to the shell
print(type(data_array))

# COMMAND ----------

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/titanic_sub.csv'

# Import file: data
data = pd.read_csv(file, sep=',', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC # Importing data from other file types

# COMMAND ----------

# MAGIC %md
# MAGIC ### Listing sheets in Excel files

# COMMAND ----------

pip install openpyxl

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# Import pandas
import pandas as pd

# Assign spreadsheet filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/battledeath.xlsx'

# Load spreadsheet: xls
xls = pd.ExcelFile(file)

# Print sheet names
print(xls.sheet_names)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing sheets from Excel files

# COMMAND ----------

# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')

# Print the head of the DataFrame df1
print(df1.head())

# COMMAND ----------

# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)

# Print the head of the DataFrame df2
print(df2.head())

# COMMAND ----------

# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[1], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# COMMAND ----------

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[1], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing SAS files

# COMMAND ----------

pip install sas7bdat

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# Import sas7bdat package
import pandas as pd
import matplotlib.pyplot as plt
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histogram of DataFrame features (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing Stata files

# COMMAND ----------

# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing HDF5 files

# COMMAND ----------

pip install h5py

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# Import packages
import numpy as np
import h5py
import matplotlib.pyplot as plt

# Assign filename: file
file = '/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/L-L1_LOSC_4_V1-1126259446-32.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)


# COMMAND ----------

# Get the HDF5 group: group
group = data['strain']

# Check out keys of group
for key in group.keys():
    print(key)

# Set variable equal to time series data: strain
strain = np.array(data['strain']['Strain'])

# Set number of time points to sample: num_samples
num_samples = 10000

# Set time vector
time = np.arange(0, 1, 1/num_samples)

# Plot data
plt.plot(time, strain[:num_samples])
plt.xlabel('GPS Time (s)')
plt.ylabel('strain')
plt.show()

# COMMAND ----------

print(group)
print(strain)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Importing Matlab files

# COMMAND ----------

# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('/Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/ja_data2.mat')

# Print the datatype type of mat
print(type(mat))

# COMMAND ----------

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC # Working with relational databases in Python

# COMMAND ----------

pip install sqlalchemy

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Examining Schema

# COMMAND ----------

# Import necessary module
from sqlalchemy import create_engine, inspect

# Create engine: engine
engine = create_engine('sqlite:////Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/Chinook.sqlite')

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
# MAGIC ## Querying Data

# COMMAND ----------

# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:////Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/Chinook.sqlite')

# Open engine connection: con
con = engine.connect()

# Perform query: rs
rs = con.execute(text("SELECT * FROM Album"))

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())
# df.columns = rs.keys()

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())

# COMMAND ----------

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute(text("SELECT LastName, Title FROM Employee"))
    df = pd.DataFrame(rs.fetchmany(3))
    # df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Using Pandas to Directly Query Data

# COMMAND ----------

# Import packages
from sqlalchemy import create_engine, text
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:////Volumes/learning_datacamp/de_associate/03_introduction_to_importing_data_in_python/Chinook.sqlite')

with engine.connect() as con:
    # Execute query and store records in DataFrame: df
    df = pd.read_sql_query(text("SELECT * FROM Album"), con)

# Print head of DataFrame
print(df.head())

# COMMAND ----------

# Open engine in context manager and store query result in df1
with engine.connect() as con:
    rs = con.execute(text("SELECT * FROM Album"))
    df1 = pd.DataFrame(rs.fetchall())
    df1.columns = rs.keys()

# Confirm that both methods yield the same result
print(df.equals(df1))
