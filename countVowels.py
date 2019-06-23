#**Count Vowels** - Enter a string and the program counts the number of vowels in the text. For added complexity have it report a sum of each vowel found.

passed_string = input("Enter a string, any string:\n> ").strip()

vowel_count = {
	"a" : 0,
	"e" : 0,
	"i" : 0,
	"o" : 0,
	"u" : 0
}

for i in passed_string:
	if i in list(vowel_count):
		vowel_count[i] += 1

print("There were %i vowels in your string. Want to see a breakdown? (y for yes)" %(sum(vowel_count.values())))
see_more = input("> ")
if see_more.strip() == 'y':
	print('"'+passed_string+'":')
	for i in vowel_count:
		print(i+":\t",vowel_count[i])
	# print(vowel_count.values.sorted())