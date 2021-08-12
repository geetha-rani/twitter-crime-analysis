
import sys,tweepy,csv,re
from textblob import TextBlob
import matplotlib.pyplot as plt
class Analysis:
 def __init__(self):
 self.tweets = []
 self.tweetText = []
 def DownloadData(self):
 # authenticating
 consumerKey = 'XXXXXXXXXXXXXXXXXXXXXX'
 consumerSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
 accessToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
 accessTokenSecret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
 auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
 auth.set_access_token(accessToken, accessTokenSecret)
 api = tweepy.API(auth)
 searchTerm = input("Enter Keyword/Tag to search about: ")
 NoOfTerms = int(input("Enter how many tweets to search: "))
 self.tweets = tweepy.Cursor(api.search, q=searchTerm, lang = "en").items(NoOfTerms)
 csvFile = open('result.csv', 'a')
 csvWriter = csv.writer(csvFile)
 polarity = 0
 positive = 0
 wpositive = 0
 spositive = 0
 negative = 0
 wnegative = 0
 snegative = 0
 neutral = 0
 for tweet in self.tweets:
    
 self.tweetText.append(self.cleanTweet(tweet.text).encode('utf-8'))  # print (tweet.text.translate(non_bmp_map)) #print tweet's text
 
analysis = TextBlob(tweet.text) # print(analysis.sentiment) # print tweet's polarity
 
 polarity += analysis.sentiment.polarity   # adding up polarities to find the average later
 
if (analysis.sentiment.polarity == 0):   # adding reaction of how people are reacting to find

  average later
 neutral += 1
 elif (analysis.sentiment.polarity > 0 and analysis.sentiment.polarity <= 0.3):
 wpositive += 1
 elif (analysis.sentiment.polarity > 0.3 and analysis.sentiment.polarity <= 0.6):
 positive += 1
 elif (analysis.sentiment.polarity > 0.6 and analysis.sentiment.polarity <= 1):
 spositive += 1
 elif (analysis.sentiment.polarity > -0.3 and analysis.sentiment.polarity <= 0):
 wnegative += 1
 elif (analysis.sentiment.polarity > -0.6 and analysis.sentiment.polarity <= -0.3):
 negative += 1
 elif (analysis.sentiment.polarity > -1 and analysis.sentiment.polarity <= -0.6):
 snegative += 1
 csvWriter.writerow(self.tweetText)
 csvFile.close()
 positive = self.percentage(positive, NoOfTerms)
 wpositive = self.percentage(wpositive, NoOfTerms)
 spositive = self.percentage(spositive, NoOfTerms)
 negative = self.percentage(negative, NoOfTerms)
 wnegative = self.percentage(wnegative, NoOfTerms)
 snegative = self.percentage(snegative, NoOfTerms)
 neutral = self.percentage(neutral, NoOfTerms)
 polarity = polarity / NoOfTerms
 print("How people are reacting on " + searchTerm + " by analyzing " + str(NoOfTerms) + "
tweets.")
 print()
 print("General Report: ")
 if (polarity == 0):
 print("neutral")
 elif (polarity > 0 and polarity <= 0.3):
 print("Weakly Positive")
 elif (polarity > 0.3 and polarity <= 0.6):
 print("Normal")
 elif (polarity > 0.6 and polarity <= 1):
 print("Strongly Positive")
 elif (polarity > -0.3 and polarity <= 0):
 print("suspicious")
 elif (polarity > -0.6 and polarity <= -0.3):
 print("Negative")
 elif (polarity > -1):
 print("crime(need emergency)")
 print()
 print("Detailed Report: ")
 print(str(positive) + "% Normal")
 print(str(negative) + "% crime")
 print(str(wnegative) + "% suspicious")
 print(str(snegative) + "% crime(need emergency)")
 self.plotPieChart(positive, negative, wnegative, snegative, searchTerm, noOfSearchTerms)
 def cleanTweet(self, tweet):
 return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w +:\ / \ / \S +)", " ", tweet).split())
 def percentage(self, part, whole):
 temp = 100 * float(part) / float(whole)
 return format(temp, '.2f')
 def plotPieChart( positive, negative, wnegative, snegative, searchTerm, noOfSearchTerms):
 labels = ['Normal [' + str(positive) + '%]','crime [' + str(negative) + '%]','suspicious [' +
str(wnegative) + '%]','crime(need emergency) [' + str(snegative) + '%]']
 sizes = [positive,negative, wnegative, snegative]
 colors = ['yellowgreen','red','lightsalmon','darkred']
 patches, texts = plt.pie(sizes, colors=colors, startangle=90)
 plt.legend(patches, labels, loc="best")
 plt.title('How people are reacting on ' + searchTerm + ' by analyzing ' + str(noOfSearchTerms) + '
Tweets.')
 plt.axis('equal')
 plt.tight_layout()
 plt.show()

if __name__== "__main__":
 sa = SentimentAnalysis()
 sa.DownloadData()
