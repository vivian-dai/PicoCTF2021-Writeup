# Python Wrangling

## Overview

Points: 10
Category: General Skills

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](./ende.py) using [this password](./pw.txt) to get [the flag](./flag.txt.en)?

## Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget [https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py)
2. $ man python

## Approach

I tried running the code in the IDE but that didn't work. I navigated to the directory where the Python file was (make sure the flag file is in the same directory) and used `python -d flag.txt.en` (-d for decode I'm guessing, -e is probably encode). This asked for the password which I pasted from pw.txt and then it outputted the flag.

Note ([issue here](https://github.com/vivian-dai/PicoCTF2021-Writeup/issues/1)): if you are running this on Python 2, `buffer` doesn't work the same way as it does in Python 3. Line 49 of [the Python script](./ende.py):

```python
sys.stdout.buffer.write(data_c)
```

needs to be replaced with

```python
sys.stdout.write(data_c)
```

## Flag

picoCTF{4p0110_1n_7h3_h0us3_aa821c16}
