#class Key. It defines a key object used for vigenere encoding
class Key:

	def __init__(self, keyString):
		self.keyString = keyString
		self.keyLength = len(self.keyString)
		self.keyIndex = 0

	#Method to increment keyIndex
	def incrementKeyIndex(self):
		self.keyIndex = self.keyIndex + 1

	#Method to get keyIndex
	def getKeyIndex(self):
		return self.keyIndex

	#Method to get key character depending on index
	def getKeyChar(self):
		return self.keyString[self.keyIndex%self.keyLength]