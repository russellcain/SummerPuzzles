import feedparser 

feed = feedparser.parse("https://www.sportsnet.ca/feed/")
entries = feed['entries']

print(list(entries[0]))
for i in entries:
	# if ("NHL" in i.title or "trade" in i.title):
		# print("\n"+i.title+":\n\t", i['summary'][3:i['summary'].index('</p>')].replace("&#8217;","'"))#,i.content[0].value)
	try:
		if i['sport']['id'] == '1247':
			print("\n"+i.title+":\n\t", i['summary'][3:i['summary'].index('</p>')].replace("&#8217;","'"))
	except:
		pass
