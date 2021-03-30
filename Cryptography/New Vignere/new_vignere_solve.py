import string
import binascii
enc ="bkglibgkhghkijphhhejggikgjkbhefgpienefjdioghhchffhmmhhbjgclpjfkp"
ALPHABET = string.ascii_lowercase[:16] 
key = "oedcfjdbe"
b16 = ""

loop =0
for i in enc:
	k = ALPHABET.index(key[loop % len(key)])
	loop = loop + 1
	index = ALPHABET.index(i)
	if(k <= index):
		b16+=chr(index -k+97)
	elif (k <= index + 16):
		b16+=chr(index +16-k+97)

flag = ""
print(b16)
for i in range(0, len(b16), 2):
	if(b16[i+1] in ALPHABET and b16[i] in ALPHABET):
		index1 = ALPHABET.index(b16[i])
		index2 = ALPHABET.index(b16[i+1])
		flag+= chr((index1<<4)+index2)
print(flag)
