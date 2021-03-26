#!/usr/bin/python3 -u
import signal

SQUARE_SIZE = 6

def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
        for row in range(SQUARE_SIZE):
                for col in range(SQUARE_SIZE):
                        if matrix[row][col] == letter:
                            return (row, col)
        print("letter not found in matrix.")
        exit()

alphabet = "0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q"
matrix = generate_square(alphabet)
msg = ""
enc_msg = "herfayo7oqxrz7jwxx15ie20p40u1i"
for i in range(0, len(enc_msg), 2):
        a = get_index(enc_msg[i], matrix)
        b = get_index(enc_msg[i+1],matrix)
        if(a[0] == b[0]):
                msg += matrix[a[0]][(a[1]-1) % SQUARE_SIZE] + matrix[b[0]][(b[1]-1)% SQUARE_SIZE]
        elif(a[1] == b[1]):
                msg += matrix[(a[0]-1)% SQUARE_SIZE][a[1]] + matrix[(b[0]-1)% SQUARE_SIZE][b[1]]
        else:
                msg += matrix[a[0]][b[1]] + matrix[b[0]][a[1]]
        
print(msg)
#herfayo7oqxrz7jwxx15ie20p40u1i
#007d0a696aaad7fb5ec21c7698e4f754
# https://en.wikipedia.org/wiki/Playfair_cipher
