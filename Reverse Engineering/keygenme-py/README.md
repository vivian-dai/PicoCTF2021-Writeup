# keygenme-py

## Problem Description

[keygenme-trial.py](./keygenme-trial.py)

### Points

30

### Question Type

Reverse Engineering

### Hints

(None)

## Approach

What stood out to me first was the following python code:

```python
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```

After looking for the code that contained the word "key", you find

```python
def enter_license():
    user_key = input("\nEnter your license key: ")
    user_key = user_key.strip()

    global bUsername_trial
    
    if check_key(user_key, bUsername_trial):
        decrypt_full_version(user_key)
    else:
        print("\nKey is NOT VALID. Check your data entry.\n\n")
```

It is likely that if check_key(user_key, bUsername_trial) returns true, it will lead to the flag so I looked at the function check_key.

```python
if len(key) != len(key_full_template_trial):
    return False
```

This code tells us that the key is the same length as "picoCTF{1n_7h3_|<3y_of_xxxxxxxx}".

```python
for c in key_part_static1_trial:
    if key[i] != c:
        return False
    i += 1
```

This code shows that the first part of the flag is "picoCTF{1n_7h3_|<3y_of_"

```python
if key[i] != hashlib.sha256(username_trial).hexdigest()[x]:
    return False
else:
    i += 1
```

The remaining code in the function is 8 if statements in the format above where x is in the order 45362718.

As the amount of if statements is equal to the remaining characters needed to find, I found the values that key[i] needs to be equal to using the code.

```python
import hashlib
username_trial = "PRITCHARD"
bUsername_trial = b"PRITCHARD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

#I used bUsername_trial because enter_liscence used it as well but after testing afterwards, they output the same answer
print(hashlib.sha256(bUsername_trial).hexdigest()[4]) 
print(hashlib.sha256(bUsername_trial).hexdigest()[5])
print(hashlib.sha256(bUsername_trial).hexdigest()[3])
print(hashlib.sha256(bUsername_trial).hexdigest()[6])
print(hashlib.sha256(bUsername_trial).hexdigest()[2])
print(hashlib.sha256(bUsername_trial).hexdigest()[7])
print(hashlib.sha256(bUsername_trial).hexdigest()[1])
print(hashlib.sha256(bUsername_trial).hexdigest()[8])
```

The output is 54ef6292 and adding it to "picoCTF{1n_7h3_|<3y_of_", we get the flag of picoCTF{1n_7h3_|<3y_of_54ef6292}.

## Flag

picoCTF{1n_7h3_|<3y_of_54ef6292}
