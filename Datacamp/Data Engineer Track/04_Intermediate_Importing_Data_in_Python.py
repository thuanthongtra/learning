# Databricks notebook source
# MAGIC %md
# MAGIC # Import Data From Internet

# COMMAND ----------

# MAGIC %md
# MAGIC ## Flat Files

# COMMAND ----------

# Import package
from urllib.request import urlretrieve
import matplotlib.pyplot as plt
import pandas as pd

# Assign url of file: url
url = 'https://assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'

# Save file locally
urlretrieve(url, 'winequality-red.csv')

# Read file into a DataFrame and print its head
df = pd.read_csv('winequality-red.csv', sep=';')
print(df.head())

# Plot first column of df
df.iloc[:, 0].hist()
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()


# COMMAND ----------

# MAGIC %md
# MAGIC ## Non-flat Files

# COMMAND ----------

pip install xlrd

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

# Import package
import pandas as pd
from urllib.request import urlretrieve

# Assign url of file: url
url = 'https://assets.datacamp.com/course/importing_data_into_r/latitude.xls'

# Save file locally
urlretrieve(url, 'latitude.xls')

# Read in all sheets of Excel file: xls
xls = pd.read_excel('latitude.xls', None) # Thong: pass None to import all sheets in sheet_name argument

# Print the sheetnames to the shell
print(xls.keys())

# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())


# COMMAND ----------

# MAGIC %md
# MAGIC ## HTTP Requests

# COMMAND ----------

# DBTITLE 1,Use urllib
# Import packages
from urllib.request import urlopen, Request

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Extract the response: html
html = response.read()

# Print the html
print(html)

# Be polite and close the response!
response.close()


# COMMAND ----------

# DBTITLE 1,Use requests
# Import package
import requests

# Specify the url: url
# url = "http://www.datacamp.com/teach/documentation"
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# Packages the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Scraping the Web

# COMMAND ----------

# DBTITLE 1,Parsing HTML
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Prettify the BeautifulSoup object: pretty_soup
pretty_soup = soup.prettify()

# Print the response
print(pretty_soup)

# COMMAND ----------

# DBTITLE 1,Getting the text
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title

# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)

# COMMAND ----------

# DBTITLE 1,Getting the hyperlinks
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
print(soup.title)

# Find all 'a' tags (which define hyperlinks): a_tags
a_tags = soup.find_all('a')

# Print the URLs to the shell
for link in a_tags:
    print(link.get('href'))

# COMMAND ----------

# MAGIC %md
# MAGIC # Use API to Import Data

# COMMAND ----------

# MAGIC %md
# MAGIC ## API & JSON

# COMMAND ----------

# Load JSON: json_data
import json
with open("/Volumes/learning_datacamp/de_associate/04_intermediate_importing_data_in_python/a_movie.json") as json_file:
    json_data = json.load(json_file)

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])

# COMMAND ----------

# MAGIC %md
# MAGIC ## API & WWW

# COMMAND ----------

# Import requests package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network' #Thong: ? for query string

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Print the text of the response
print(r.text)


# COMMAND ----------

# Import package
import requests

# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=social+network'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print each key-value pair in json_data
for k in json_data.keys():
    print(k + ': ', json_data[k])


# COMMAND ----------

# Import package
import requests

# Assign URL to variable: url
url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&format=json&exintro=&titles=pizza'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Decode the JSON data into a dictionary: json_data
json_data = r.json()

# Print the Wikipedia page extract
pizza_extract = json_data['query']['pages']['24768']['extract']
print(pizza_extract)


# COMMAND ----------

# MAGIC %md
# MAGIC # Twitter API

# COMMAND ----------

pip install git+https://github.com/tweepy/tweepy.git

# COMMAND ----------

dbutils.library.restartPython()

# COMMAND ----------

import tweepy
import pandas as pd

consumer_key = "nZ6EA0FxZ293SxGNg8g8aP0HM"
consumer_secret = "fJGEodwe3KiKUnsYJC3VRndj7jevVvXbK2D5EiJ2nehafRgA6i"
access_token = "1092294848-aHN7DcRP9B4VMTQIhwqOYiB14YkW92fFO8k8EPy"
access_token_secret = "X4dHmhPfaksHcQ7SCbmZa2oYBBVSD2g8uIHXsp5CTaksx"

#Pass in our twitter API authentication key
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret,
    access_token, access_token_secret
)

#Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

search_query = "'ref''world cup'-filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100

try:
    #The number of tweets we want to retrieved from the search
    tweets = api.search_tweets(q=search_query, lang="en", count=no_of_tweets, tweet_mode ='extended')
    
    #Pulling Some attributes from the tweet
    attributes_container = [[tweet.user.name, tweet.created_at, tweet.favorite_count, tweet.source, tweet.full_text] for tweet in tweets]

    #Creation of column list to rename the columns in the dataframe
    columns = ["User", "Date Created", "Number of Likes", "Source of Tweet", "Tweet"]
    
    #Creation of Dataframe
    tweets_df = pd.DataFrame(attributes_container, columns=columns)
except BaseException as e:
    print('Status Failed On,',str(e))

# COMMAND ----------


