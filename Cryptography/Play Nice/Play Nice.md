# Play Nice

## Problem Description

Not all ancient ciphers were so bad... The flag is not in standard format. nc mercury.picoctf.net 30568 [playfair.py](./playfair.py)

### Points

110

### Question Type

Cryptography

### Hints

(None)

## Approach

### Understanding the Code

```python
alphabet = open("key").read().rstrip()
m = generate_square(alphabet)
msg = open("msg").read().rstrip()
enc_msg = encrypt_string(msg, m)
print("Here is the alphabet: {}\nHere is the encrypted message: {}".format(alphabet, enc_msg))
```

This initializes important variables in the program. Running it in Terminal, we get that that the alphabet is "0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q" and enc_msg is "herfayo7oqxrz7jwxx15ie20p40u1i".

```python
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
```

The cuntion generate_square creates a 2D list of letters and numbers, which is stored in the variable m. Printing it out, we get:

```text
[['0', 'f', 'k', 'd', 'w', 'u'],
['6', 'r', 'p', '8', 'z', 'v'],
['s', 'n', 'l', 'j', '3', 'i'],
['y', 't', 'x', 'm', 'e', 'h'],
['7', '2', 'c', 'a', '9', 'b'],
['g', '5', 'o', '4', '1', 'q']]
```

```python
def encrypt_string(s, matrix):
    result = ""
    if len(s) % 2 == 0:
            plain = s
    else:
            plain = s + "0fkdwu6rp8zvsnlj3iytxmeh72ca9bg5o41q"[0]
    for i in range(0, len(plain), 2):
            result += encrypt_pair(plain[i:i + 2], matrix)
    return result
```

The function encrypt_string simply adds a '0' to the end of the message if the length is odd and then runs encrypt_pair two characters in msg at a time. When solving, we can simply ignore this function and if the outputted message ends with a 0, test it with and without a '0' in the terminal.

```python
def get_index(letter, matrix):
    for row in range(SQUARE_SIZE):
            for col in range(SQUARE_SIZE):
                    if matrix[row][col] == letter:
                        return (row, col)
    print("letter not found in matrix.")
    exit()
```

This function, get_index, gets the index of letter in matrix.

```python
def encrypt_pair(pair, matrix):
    p1 = get_index(pair[0], matrix)
    p2 = get_index(pair[1], matrix)

    if p1[0] == p2[0]:
        return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE]
    elif p1[1] == p2[1]:
        return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]]
    else:
        return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]
```

The function encrypt_pair is where characters in the message are changed. If the two letters are in the same row, both a shifted left, if they are in the same column, they are shifted down and if they are not in the same column or row, the column is switched.

### Solving

I created a program [playfair_solve](./playfair_solve.py) to find the message

```python
for i in range(0, len(enc_msg), 2):
    a = get_index(enc_msg[i], matrix)
    b = get_index(enc_msg[i+1],matrix)
    if(a[0] == b[0]):
        msg += matrix[a[0]][(a[1]-1) % SQUARE_SIZE] + matrix[b[0]][(b[1]-1)% SQUARE_SIZE]
    elif(a[1] == b[1]):
        msg += matrix[(a[0]-1)% SQUARE_SIZE][a[1]] + matrix[(b[0]-1)% SQUARE_SIZE][b[1]]
    else:
        msg += matrix[a[0]][b[1]] + matrix[b[0]][a[1]]
```

I looped through the letters in enc_msg two at a time and got their index in matrix, stored in a and b. If a[0] == b[0], then I would shift both of them left, if a[1] == b[1], I would shift them up and otherwise, I would switch b[1] and a[1]. The message that was outputted was "emf57mgc51tp693dtt4g3h7f8ouwq3". Running the program in terminal and inputting that value as plain text, it outputs "Congratulations! Here's the flag: 007d0a696aaad7fb5ec21c7698e4f754".

I tried picoCTF{007d0a696aaad7fb5ec21c7698e4f754} which didn't work and then tried 007d0a696aaad7fb5ec21c7698e4f754, which is the flag.

## Flag

007d0a696aaad7fb5ec21c7698e4f754
