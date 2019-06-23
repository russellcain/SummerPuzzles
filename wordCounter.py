#**Count Words in a String** - Counts the number of individual words in a string. For added complexity read these strings in from a text file and generate a summary.
import feedparser 

feed = feedparser.parse("https://www.sportsnet.ca/feed/")
entries = feed['entries']

passed_file = input("let me guess how many words you just entered\n> ").strip()
print("I think that's about %i words?" %len(passed_file.split(" ")))
latest_article = entries[0]['summary'][3:entries[0]['summary'].index('</p>')].replace("&#8217;","'")
print("\nAnd the most recent article from the NHL RSS feed (%s) has %i words!" %(latest_article, len(latest_article.split(" "))))