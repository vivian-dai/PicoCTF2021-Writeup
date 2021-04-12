# New Vignere

## Problem Description

Another slight twist on a classic, see if you can recover the flag. (Wrap with picoCTF{}) bkglibgkhghkijphhhejggikgjkbhefgpienefjdioghhchffhmmhhbjgclpjfkp [new_vignere.py](./new_vignere.py)

### Points

300

### Question Type

Cryptography

### Hints

1. [https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher#Cryptanalysis)

## Approach

### Understanding the Code

*Suggested to read the writeup for New Caesar first.* The code given is the same as New Caesar except for the restrictions on flag and key.

```python
flag = "redacted"
assert all([c in "abcdef0123456789" for c in flag])

key = "redacted"
assert all([k in ALPHABET for k in key]) and len(key) < 15
```

The flag can only contain the characters in "abcdef0123456789" and the key needs to be in ALPHABET (letters from 'a' to 'p') and has a maximum length of 15.

### Solving

Because the flag is limited to a few characters, I ran "abcdef0123456789" in my code for New Caesar to get the value of b16. There I found that each character corresponded to two characters.

```text
gb - a      gc - b      gd - c      ge - d      gf - e      gg - f
da - 0      db - 1      dc - 2      dd - 3      de - 4      df - 5
dg - 6      dh - 7      di - 8      dj - 9
```

This means that in g16, every other character is either a 'g' or a 'd'.

In the original code, enc += shift(c, key[i % len(key)]), which means that the values of key are looped through to get the values of enc. This means that there will be a pattern in the key every len(key) values in enc.

I decided to try manually getting the flag so I printed out the values of b16 for the letters 'a' to 'p'.

![b16 Possible Values 1](./B16%20Possible%20Values%201.png)

I first attempted to find a pattern in the letters at index 0, 2, etc. I highlighted all pairs that start with g or b to try to find a pattern in the key. Column 10 is the first repetition of either a key of 'l' or 'o' which are the values found in column 1 so I tried seeing if there was a pattern every 9 pairs. The circles correspons to how I figured out the value for the 9 pairs. I was unable to find the 6th pair but I guessed that I would be able to find it after taking into account the second letter. The values for the key we currently have are "odfde(b/e)cjb".

![b16 possible values 2](./b16%20possible%20values%202.jpeg)

Next I tried to find a pattern including the second letters in the pair. As the pattern above is 9 characters, if we take into account the second letter, that would mean that the flag is 18 (9 * 2) characters long, which exceeds the maximum length for the key. This means thatat there is a repeated value in between pair 1 and pair 9. It is likely that the pattern repeates every 9 letters so I tried it out. If the first value is a 'd', the character needs to be an integer so the second value is a character from a to j. If the first value is a 'g', the character is a letter and the second letter is a letter between 'b' and 'g'.

![b16 possible values 3](./b16%20possible%20values%203.png)

In the image above, it only shows the first three loops because it is possible to find the pattern with just the first three loops. There is a pattern every 9 letters and the letters we get from that are "oedcfjdbe", which is the key.

I slightly modified the code from New Caesar to use the key found, [new_vignere_solve](./new_vignere_solve.py). The code to convert from b16 to the flag is the same while the code to convert from enc to b16 now loops through the key.

```python
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
```

Running the code, we get that the flag "698987ddce418c11e9aa564229c50fda" and testing picoCTF{698987ddce418c11e9aa564229c50fda}, we find the flag.

## Flag

picoCTF{698987ddce418c11e9aa564229c50fda}
