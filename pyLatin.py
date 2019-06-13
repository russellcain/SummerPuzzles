#**Pig Latin** - Pig Latin is a game of alterations played on the English language game. To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.

vowels = "a e i o u".split(" ")

def pigLatin(words):
	answer = ""
	for word in words.split(" "):
		if (word[0] in vowels or word[:2] == "ho"): #"ho"pefully there aren't other silent consonant-vowel patterns
			answer += (word + "way ") 
			break
		for i in range(len(word)):
			if word[0] not in vowels:
				word = word[1:]+word[0]
			else:
				answer += (word+"ay ")
				break
	return answer.strip()
# assume the user only enters letters (and we are using conventional grouping):
print(pigLatin(input("enter a word \n> ")))