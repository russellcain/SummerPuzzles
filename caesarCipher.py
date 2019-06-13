#**Caesar cipher** - Implement a Caesar cipher, both encoding and decoding. The key is an integer from 1 to 25. This cipher rotates the letters of the alphabet (A to Z). The encoding replaces each letter with the 1st to 25th next letter in the alphabet (wrapping Z to A). So key 2 encrypts "HI" to "JK", but key 20 encrypts "HI" to "BC". This simple "monoalphabetic substitution cipher" provides almost no security, because an attacker who has the encoded message can either use frequency analysis to guess the key, or just try all 25 keys.

def encode(message, n):
	alphabet = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
	result = ""
	for i in message:
		if i in alphabet:
			result += alphabet[(alphabet.index(i)+n)%26]
		else:
			if i.lower() in alphabet:
				result += alphabet[(alphabet.index(i.lower())+n)%26].upper()
			else:
				result += i
	return result

class CaesarCipher(object):
	def __init__(self, n, message):
		self.n = int(n)
		self.message = message

	def solution(self):
		print("pssst:", encode(self.message, self.n))

if __name__ == "__main__":
	message = input("What is your secret message? \n> ")
	n = input("and how many spins on the old dial should we give it? \n> ")
	CaesarCipher(n, message).solution()