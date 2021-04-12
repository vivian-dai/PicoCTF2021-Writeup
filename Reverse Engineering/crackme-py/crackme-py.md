# crackme-py

## Description

[crackme.py](./crackme.py)

## Hints

(None)

## Approach

When looking at the contents of the Python file, there are a few things to note:

```python
# Hiding this really important number in an obscure piece of code is brilliant!
# AND it's encrypted!
# We want our biggest client to know his information is safe with us.
bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"
```

This can be decrypted using the `decode_secret` method BUT the method is never called.
I replaced the call for `choose_greatest()` on line 34 for `decode_secret(bezos_cc_secret)` and ran it.

## Flag

picoCTF{1|\/|_4_p34|\|ut_dd2c4616}
