## MODULES IDENTIFIED IN THIS PROJECT ARE:
### MODULE 1 : ***Getting data using Flume***
                      
After creating an application in the Twitter developer site we want to use the consumer key and secret along with the access token
and secret values. By which we can access the Twitter and we can get the information that what we want exactly here we will get everything
in JSON format and this is stored in the HDFS that we have given the location where to save all the data that comes from the Twitter. The
following is the configuration file that we want to use to get the Twitter data from the Twitter. 

### MODULE 2 : ***Querying using Hive Query Language***

After running the Flume by setting the above configuration
then the Twitter data will automatically will save into HDFS where we
have the set the path storage to save the Twitter data that was taken
by using Flume. From these data first we get to know how we are
going to read the data that is in the form of JSON format for that we
are using the custom serve for JSON so that our hive can read the JSON
data and can create a table in our prescribed format. Also we are using
another User Defined Functions (UDF) for performing the sentiment
analysis on the tales that are created by using Hive

### MODULE 3 : ***Prediction Analysis***

The Natural Language Toolkit, or more commonly NLTK,
is a suite of libraries and programs for symbolic and statistical natural
language processing (NLP) for English written in the Python 
programming language. NLTK has been used successfully as a teaching
tool, as an individual study tool, and as a platform for prototyping and
building research systems. Using NLTK and Python we will predict the
analysis of the tweets which we got in the JSON file which are stored
using hive in hdfs
