#**Check if Palindrome** - Checks if the string entered by the user is a palindrome. That is that it reads the same forwards as backwards like “racecar”

passed_string = input("enter a word (maybe a palindrome?)\n> ").lower().strip()
if passed_string == passed_string[::-1]:
	print("Congrats! You've got yourself a palindrome")
else:
	print("Sorry, this doesnt seem to be a palindrome")