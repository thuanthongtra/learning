# Databricks notebook source
# MAGIC %md
# MAGIC # Common data problems

# COMMAND ----------

# Import pandas as pd
import pandas as pd
import datetime as dt

# COMMAND ----------

file = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/ride_sharing_new.csv'
ride_sharing = pd.read_csv(file)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Type Constraints

# COMMAND ----------

# MAGIC %md
# MAGIC ### Numeric or Category
# MAGIC The user_type column contains information on whether a user is taking a free ride and takes on the following values:
# MAGIC - 1 for free riders.
# MAGIC - 2 for pay per ride.
# MAGIC - 3 for monthly subscribers.

# COMMAND ----------

# Print the information of ride_sharing
print('----------info()----------')
print(ride_sharing.info())
print('')

# Print summary statistics of user_type column
print('----------descbrie()----------')
print(ride_sharing['user_type'].describe())
print('')

# Convert user_type from integer to category
ride_sharing['user_type_cat'] = ride_sharing['user_type'].astype('category')

# Write an assert statement confirming the change
assert ride_sharing['user_type_cat'].dtype == 'category'

# Print new summary statistics
print('----------descbrie() with new datatype----------')
print(ride_sharing['user_type_cat'].describe())
print('')

# COMMAND ----------

# MAGIC %md
# MAGIC ### Summing strings and concatenating numbers
# MAGIC Column duration has string 'minutes' and we need to convert datatype to int. Hence, we first need to use **_strip()_** to eliminate the word 'minutes'.
# MAGIC
# MAGIC

# COMMAND ----------

# Strip duration of minutes
ride_sharing['duration_trim'] = ride_sharing['duration'].str.strip("minutes")

# Convert duration to integer
ride_sharing['duration_time'] = ride_sharing['duration_trim'].astype('int')

# Write an assert statement making sure of conversion
assert ride_sharing['duration_time'].dtype == 'int'

# Print formed columns and calculate average ride duration 
print(ride_sharing[['duration','duration_trim','duration_time']])
print(ride_sharing['duration_time'].mean())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Data Range Constraints

# COMMAND ----------

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing['tire_sizes'] > 27, 'tire_sizes'] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('category')

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

# COMMAND ----------

# Convert ride_date to date
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date']).dt.date

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Uniqueness Constraints

# COMMAND ----------

# DBTITLE 1,Finding duplicates
# Find duplicates
duplicates = ride_sharing.duplicated(subset = ['ride_id'], keep = False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values(by = 'ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])

# COMMAND ----------

# DBTITLE 1,Treating duplicates
# Drop complete duplicates from ride_sharing
ride_dup = ride_sharing.drop_duplicates()

# Create statistics dictionary for aggregation function
statistics = {'user_birth_year': 'min', 'duration_time': 'mean'}

# Group by ride_id and compute new statistics
ride_unique = ride_dup.groupby(by = 'ride_id').agg(statistics).reset_index()

# Find duplicated values again
duplicates = ride_unique.duplicated(subset = 'ride_id', keep = False)
duplicated_rides = ride_unique[duplicates == True]

# Assert duplicates are processed
assert duplicated_rides.shape[0] == 0

# COMMAND ----------

# MAGIC %md
# MAGIC # Text and categorical data problems

# COMMAND ----------

file2 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/airlines_final.csv'
airlines = pd.read_csv(file2)

file3 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/categories.csv'
categories = pd.read_csv(file3)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Membership Constraints

# COMMAND ----------

# Print categories DataFrame
print(categories)

# Print unique values of survey columns in airlines
print('Cleanliness: ', airlines['cleanliness'].unique(), "\n") #Thong: It has 'Unacceptable'
print('Safety: ', airlines['safety'].unique(), "\n")
print('Satisfaction: ', airlines['satisfaction'].unique(), "\n")

# COMMAND ----------

# DBTITLE 1,Finding inconsistency
# Find the cleanliness category in airlines not in categories
cat_clean = set(airlines['cleanliness']).difference(categories['cleanliness'])

# Find rows with that category
cat_clean_rows = airlines['cleanliness'].isin(cat_clean)

# Print rows with inconsistent category
print(airlines[cat_clean_rows][['cleanliness','safety','satisfaction']])

# COMMAND ----------

# DBTITLE 1,Finding consistency
# Print rows with consistent categories only
print(airlines[~cat_clean_rows][['cleanliness','safety','satisfaction']])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Categorical variables

# COMMAND ----------

# MAGIC %md
# MAGIC ### Inconsistent categories

# COMMAND ----------

# Print unique values of both columns
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# COMMAND ----------

# Lower dest_region column and then replace "eur" with "europe"
airlines['dest_region'] = airlines['dest_region'].str.lower()
airlines['dest_region'] = airlines['dest_region'].replace({'eur':'europe'})

# Remove white spaces from `dest_size`
airlines['dest_size'] = airlines['dest_size'].str.strip()

# Verify changes have been effected
print(airlines['dest_region'].unique())
print(airlines['dest_size'].unique())

# COMMAND ----------

# MAGIC %md
# MAGIC ### Remapping categories

# COMMAND ----------

import numpy as np

# COMMAND ----------

# Create ranges for categories
label_ranges = [0, 60, 180, np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, 
                                labels = label_names)

print(airlines[['wait_min','wait_type']])

# COMMAND ----------

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 
            'Thursday': 'weekday', 'Friday': 'weekday', 
            'Saturday': 'weekend', 'Sunday': 'weekend'}

airlines['day_week'] = airlines['day'].replace(mappings)

print(airlines[['day','day_week']])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Cleaning text data

# COMMAND ----------

# DBTITLE 1,Removing titles and taking names
# #Thong: comment out because source does not have column full_name
# # Replace "Dr." with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Dr.","")

# # Replace "Mr." with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Mr.","")

# # Replace "Miss" with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Miss.","")

# # Replace "Ms." with empty string ""
# airlines['full_name'] = airlines['full_name'].str.replace("Ms.","")

# # Assert that full_name has no honorifics
# assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

# COMMAND ----------

# DBTITLE 1,Keeping it descriptive (short)
# #Thong: comment out because source does not have column survey_response
# # Store length of each row in survey_response column
# resp_length = airlines['survey_response'].str.len()

# # Find rows in airlines where resp_length > 40
# airlines_survey = airlines[resp_length > 40]

# # Assert minimum survey_response length is > 40
# assert airlines_survey['survey_response'].str.len().min() > 40

# # Print new survey_response column
# print(airlines_survey['survey_response'])

# COMMAND ----------

# MAGIC %md
# MAGIC # Advanced data problems

# COMMAND ----------

file4 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/banking_dirty.csv'
banking = pd.read_csv(file4)

# COMMAND ----------

print(banking.head())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Uniformity

# COMMAND ----------

print(banking[['acct_cur','acct_amount']])

# COMMAND ----------

# DBTITLE 1,Uniform currencies
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1

# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'

print(banking[['acct_cur','acct_amount']])

# COMMAND ----------

# DBTITLE 1,Uniform dates
# Print the header of account_opened
print(banking['account_opened'].head())

# COMMAND ----------

# Convert account_opened to datetime
banking['account_opened'] = pd.to_datetime(banking['account_opened'],
                                           # Attempt to infer format of each date
                                           infer_datetime_format = True,
                                           # Return NA for rows where conversion failed
                                           errors = 'coerce')

print(banking['account_opened'].head())

# COMMAND ----------

# Get year of account opened
banking['acct_year'] = banking['account_opened'].dt.strftime('%Y')

# Print acct_year
print(banking['acct_year'])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Cross field validation

# COMMAND ----------

# DBTITLE 1,Check Sum rows
# Store fund columns to sum against
fund_columns = ['fund_A', 'fund_B', 'fund_C', 'fund_D']

# Find rows where fund_columns row sum == inv_amount
inv_equ = banking[fund_columns].sum(axis = 1) == banking['inv_amount']

# Store consistent and inconsistent data
consistent_inv = banking[inv_equ]
inconsistent_inv = banking[~inv_equ]

# Store consistent and inconsistent data
print("Number of inconsistent investments: ", inconsistent_inv.shape[0])

print(inconsistent_inv[['fund_A', 'fund_B', 'fund_C', 'fund_D', 'inv_amount']])

# COMMAND ----------

# DBTITLE 1,Check Age
import pandas as pd
import datetime as dt

# Convert birth_date column to datetime
banking['birth_date'] = pd.to_datetime(banking['birth_date'])

# Store today's date and find ages
today = dt.date.today()
ages_manual = today.year - banking['birth_date'].dt.year

# Find rows where age column == ages_manual
age_equ = banking['Age'] == ages_manual

# Store consistent and inconsistent data
consistent_ages = banking[age_equ]
inconsistent_ages = banking[~age_equ]

# Store consistent and inconsistent data
print("Number of inconsistent ages: ", inconsistent_ages.shape[0])

print(inconsistent_ages[['birth_date','Age']])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Completeness

# COMMAND ----------

pip install missingno

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import missingno as msno
import pandas as pd
import matplotlib.pyplot as plt

# COMMAND ----------

file5 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/banking_dirty.csv'
banking = pd.read_csv(file5)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Check Missing Investor's Age

# COMMAND ----------

# Print number of missing values in banking
print(banking.isna().sum())

# Visualize missingness matrix
msno.matrix(banking)
plt.show()

# Isolate missing and non missing values of inv_amount
missing_investors = banking[banking['inv_amount'].isna()]
investors = banking[~banking['inv_amount'].isna()]

# COMMAND ----------


investors.describe()

# COMMAND ----------

missing_investors.describe() #Thong: missing value occur for investors whose age is min 3 and max 28

# COMMAND ----------

# Sort banking by age and visualize
banking_sorted = banking.sort_values(by = 'Age')
msno.matrix(banking_sorted)
plt.show() #Thong: then we can confirm missing values for age from 0 to 28 can be change to 0

# COMMAND ----------

# MAGIC %md
# MAGIC ### Add replacement for null

# COMMAND ----------

# Drop missing values of cust_id
banking_fullid = banking.dropna(subset = ['cust_id'])

# Compute estimated acct_amount
acct_imp = banking_fullid['inv_amount'] * 5

# Impute missing acct_amount with corresponding acct_imp
banking_imputed = banking_fullid.fillna({'acct_amount':acct_imp})

# Print number of missing values
print(banking_imputed.isna().sum())

# COMMAND ----------

# MAGIC %md
# MAGIC # Record linkage

# COMMAND ----------

# MAGIC %md
# MAGIC ## String Similarity & Minimum Edit Distiance

# COMMAND ----------

# MAGIC %md
# MAGIC **`Minimum edit distance:`** least possible amount of steps needed to transition from **_String A_** to **_String B_**
# MAGIC - Steps can be: Insert / Deletion / Subtitution / Transposition
# MAGIC - Packages: nltk, `thefuzz`, textdistance...
# MAGIC - Algorithm:
# MAGIC   - Damerau-Levenshtein: insertion, subtitution, deletion, transposition
# MAGIC   - `Levenshtein: insertion, subtitution, deletion`
# MAGIC   - Hamming: subtitution only
# MAGIC   - Jaro distance: transposition only

# COMMAND ----------

pip install thefuzz

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd

# COMMAND ----------

file6 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/restaurants_L2_dirty.csv'
restaurants = pd.read_csv(file6)
print(restaurants)

# COMMAND ----------

# Import process from thefuzz
from thefuzz import process

# Store the unique values of cuisine_type in unique_types
unique_types = restaurants['type'].unique()

# Calculate similarity of 'asian' to all values of unique_types
print(process.extract('asian', unique_types, limit = len(unique_types)))

# COMMAND ----------

# Calculate similarity of 'american' to all values of unique_types
print(process.extract('american', unique_types, limit = len(unique_types)))

# COMMAND ----------

# Calculate similarity of 'italian' to all values of unique_types
print(process.extract('italian', unique_types, limit = len(unique_types)))

# COMMAND ----------

# MAGIC %md
# MAGIC Thong: 80 is that sweet spot where you convert all incorrect typos without remapping incorrect categories

# COMMAND ----------

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['type'], limit = restaurants.shape[0])

# Inspect the first 5 matches
print(matches[0:5])

# COMMAND ----------

# Create a list of matches, comparing 'italian' with the cuisine_type column
matches = process.extract('italian', restaurants['type'], limit=restaurants.shape[0])

# Iterate through the list of matches to italian
for match in matches:
  # Check whether the similarity score is greater than or equal to 80
  if match[1] >= 80:
    # Select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
    restaurants.loc[restaurants['type'] == match[0], 'type'] = 'italian'

# COMMAND ----------

categories = ['italian', 'asian', 'american']

# Iterate through categories
for cuisine in categories:  
  # Create a list of matches, comparing cuisine with the cuisine_type column
  matches = process.extract(cuisine, restaurants['type'], limit=restaurants.shape[0])

  # Iterate through the list of matches
  for match in matches:
     # Check whether the similarity score is greater than or equal to 80
    if match[1] >= 80:
      # If it is, select all rows where the cuisine_type is spelled this way, and set them to the correct cuisine
      restaurants.loc[restaurants['type'] == match[0], 'type'] = cuisine
      
# Inspect the final result
print(restaurants['type'].unique())

# COMMAND ----------

# MAGIC %md
# MAGIC ## Record linkage

# COMMAND ----------

# MAGIC %md
# MAGIC **`Record linkage:`** is the act of linking data from different sources regarding the same entity
# MAGIC - Package: `recordlinkage`

# COMMAND ----------

pip install recordlinkage

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import pandas as pd
import recordlinkage

# COMMAND ----------

file6 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/restaurants_L2.csv'
restaurants = pd.read_csv(file6)
print(restaurants)

file7 = '/Volumes/learning_datacamp/de_associate/05_cleaning_data_in_python/restaurants_L2_dirty.csv'
restaurants_new = pd.read_csv(file7)
print(restaurants_new)

# COMMAND ----------

# Create an indexer and object and find possible pairs
indexer = recordlinkage.Index()

# Block pairing on cuisine_type
indexer.block('type')

# Generate pairs
pairs = indexer.index(restaurants, restaurants_new)


# COMMAND ----------

# Create a comparison object
comp_cl = recordlinkage.Compare()

# Find exact matches on city, cuisine_types - 
comp_cl.exact('city', 'city', label='city')
comp_cl.exact('type', 'type', label='type')

# Find similar matches of rest_name
comp_cl.string('name', 'name', label='name', threshold = 0.8) 

# Get potential matches and print
potential_matches = comp_cl.compute(pairs, restaurants, restaurants_new)
print(potential_matches)

# COMMAND ----------

potential_matches[potential_matches.sum(axis = 1) >= 3] #Thong: 3 is the number of columns

print(potential_matches)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Linking Dataframe

# COMMAND ----------

# Isolate potential matches with row sum >=3
matches = potential_matches[potential_matches.sum(axis = 1) >= 3]
print(matches.index)
# Get values of second column index of matches
matching_indices = matches.index.get_level_values(1)

# Subset restaurants_new based on non-duplicate values
non_dup = restaurants_new[~restaurants_new.index.isin(matching_indices)]

# Append non_dup to restaurants
full_restaurants = restaurants.append(non_dup)
print(full_restaurants)
