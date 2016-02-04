from Key import Key

#class Vigenere. It defines vigenere crypting and cracking methods.
class Vigenere:

	def __init__(self, stringToCrypt):
		self.clearString = stringToCrypt

	#Method to do a vigenere encoding on a string using a key passed as a parameter
	def crypt(self, key):
		key = Key(key)
		stringCrypted = list(self.clearString)
		#Loop on all upper characters in the string to crypt
		for c in str.upper(self.clearString):
			stringCrypted[key.getKeyIndex()] = self.encodeCharacter(c, key)
			key.incrementKeyIndex()
		return stringCrypted

	#Method to do a vigenere encoding on a single character
	def encodeCharacter(self, characterToCrypt, key):
		#Crypt character
		characterToCrypt = chr( ord(characterToCrypt) + (ord(key.getKeyChar())-ord('A')) )
		#If crypted character is higher than Z, add the rest of the % by coming back to A
		if (characterToCrypt > 'Z'):
			characterToCrypt = chr (ord('A')-1 + (ord(characterToCrypt)%ord('Z')))
		return characterToCrypt