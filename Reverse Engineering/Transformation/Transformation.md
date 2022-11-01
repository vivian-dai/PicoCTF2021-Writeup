# Transformation

## Problem Description

I wonder what this really is... [enc](./enc)

''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

### Points

20

### Question Type

Reverse Engineering

### Hints

1. You may find some decoders online

## Approach

Because the code given in the description used ord() and chr() which are used in Python when changing from decimal to ascii values, I tried placing the characters in the file into an online convertor and got the numbers:

> 28777,25455,17236,18043,12598,24418,26996,29535,26990,29556,13108,25695,28518,24376,24368,13411,12343,13872,25725

Upon further analyzing the code given in the description, we can deduce that the value is equal to the characters in the file and the flag is the value of the array "flag".

```python
''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
```

Testing this out with "pi" which are the first two most likely characters for the flag, we prove that this hypothesis is correct.

```text
28777 = ord(flag[0]) << 8 + ord(flag[1])
ord('p') <<8 + ord('i')
= 112 << 8 + 105
= 28672 + 105 = 28777
```

After realizing this, I decided to write code to find the characters corresponding to each of the numbers:

```java
public class Transformation {
    public static void main (String[] args){
        int sum[] = {28777, 25455, 17236, 18043, 12598, 24418, 26996, 29535, 26990, 29556, 13108, 25695, 28518, 24376, 24368, 13411, 12343, 13872, 25725};
        for(int j = 0; j < sum.length; j++){
            for(int i= 0; i <= 126; i++){
                if((sum[j] - (i << 8)) <= 126 && (sum[j] - (i << 8)) >= 0){
                    System.out.print(Character.toString((char) i) + Character.toString((char) (sum[j] - (i << 8))));
                }
            }
        }
    }
}
```

I looped through all of the values in the ASCII table just in case and each number outputed two characters which formed picoCTF{16_bits_inst34d_of_8_04c0760d}.

## Flag

picoCTF{16_bits_inst34d_of_8_04c0760d}
