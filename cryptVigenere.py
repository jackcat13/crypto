 #!/usr/bin/python

import sys
from Vigenere import Vigenere

key = ""

#Input verifications
if len(sys.argv) == 2:
    key = sys.argv[1]
else:
    print "Usage : python vigenere.py key(string)"
    sys.exit(0)

#User input which is the string to crypt
stringToCrypt = raw_input();

vigenere = Vigenere(stringToCrypt)
stringCrypted = vigenere.crypt(key)

#Print crypted string
print "".join(stringCrypted);