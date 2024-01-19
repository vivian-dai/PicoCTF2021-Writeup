# New Caesar

## Problem Description

We found a brand new type of encryption, can you break the secret code? (Wrap with picoCTF{}) mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj [new_caesar.py](./new_caesar.py)

### Points

60

### Question Type

Cryptography

### Hints

1. How does the cipher work if the alphabet isn't 26 letters?
2. Even though the letters are split up, the same paradigms still apply

## Approach

### Understanding the Code

```python
ALPHABET = string.ascii_lowercase[:16] #a,b,c,d,... p
flag = "redacted"
key = "redacted"
assert all([k in ALPHABET for k in key])
assert len(key) == 1
```

The assert statements show that the key needs to be one character and be a letter between a to p. It is necessary to change the values of flag and key in order to get an output of "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj".

Next, I needed to understand what the function b16_encode did as the next line of code was "b16 = b16_encode(flag)"

```python
def b16_encode(plain):
    enc = ""
    for c in plain:
        binary = "{0:08b}".format(ord(c))
        enc += ALPHABET[int(binary[:4], 2)]
        enc += ALPHABET[int(binary[4:], 2)]
    return enc
```

Testing the code "binary = "{0:08b}".format(ord(c))", it outputs the ascii value of c (values in the flag) in binary form. The following two lines split the binary number in half (e.g. 01101110 becomes 0110 for the first and 1110 for the second), in which the integer value is the index of a letter in the list ALPHABET (e.g. 0110_2 = 6_10, ALPHABET[6] is added to the encryption) that will be added to the variable encryption.

```python
for i, c in enumerate(b16):
    enc += shift(c, key[i % len(key)])
```

The final process of encrypting the flag is above. Usine enumerate loops through the values of b16, assigning i to the index at a particular point and c the value. The values for the function include the values of b16 and the key (len(key) = 1, i%1 = 0).

```python
def shift(c, k):
    t1 = ord(c) - LOWERCASE_OFFSET
    t2 = ord(k) - LOWERCASE_OFFSET
    return ALPHABET[(t1 + t2) % len(ALPHABET)]
```

The function shift returns a value in ALPHABET at the index ascii value of the c minus 97 plus the ascii value of the key minus 97 mod 16.

### Solving

I decided to write code to make the program run in reverse [new_caesar_reverse_code](./new_caesar_reverse_code.py)

I stored the value in the question in the variable enc and as the key could have been any character from a to p, I decided to create a list named b16 so that I can convert the encryption for all possible keys. I first needed to revers the function shift.

```python
for i in enc:
    for k in range(len(ALPHABET)):
        index = ALPHABET.index(i)
        if(k <= index):
            b16[k]+=chr(index -k+97)
        else:
            b16[k]+=chr(index +16-k+97)
```

I looped through each value of enc and converted it for each possible key. We know that the index of i in ALPHABET needs to equal the character we are looking - 97 and the key -97 modulus 16. The variable k is equal to ord(key) - 97 so we can determine the ascii value of the characters in b16 with either (index - k - 97) or (index + 16 - 7 + 97) if the sum exceeds the index. At the end of this code, we have all possible values of b16.

The following next code outputs all possible flags given b16:

```python
for k in range(len(ALPHABET)):
    flag=""
    b = b16[k]
    for i in range(0, len(b), 2):
        if(b[i+1] in ALPHABET and b[i] in ALPHABET):
            index1 = ALPHABET.index(b[i])
            index2 = ALPHABET.index(b[i+1])
            flag+= chr((index1 <<4) +index2)
    print(flag)
```

Each value in the flag is equal to the index of b[i] in ALPHABET bitwise shifted 4 bits blus the index of b[i+1] in ALPHABET. When we run the code, all outputs include invalid characters except et_tu?_a2da1e18af49f649806988786deb2a6c.

## Flag

picoCTF{et_tu?_a2da1e18af49f649806988786deb2a6c}
