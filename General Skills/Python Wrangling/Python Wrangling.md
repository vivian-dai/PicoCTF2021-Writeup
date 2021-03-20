# Python Wrangling

## Overview

Points: 10
Category: General Skills

## Description

Python scripts are invoked kind of like programs in the Terminal... Can you run [this Python script](https://github.com/v341196137/PicoCTF2021-Writeup/blob/main/General%20Skills/Python%20Wrangling/ende.py) using [this password](https://github.com/v341196137/PicoCTF2021-Writeup/blob/main/General%20Skills/Python%20Wrangling/pw.txt) to get [the flag](https://github.com/v341196137/PicoCTF2021-Writeup/blob/main/General%20Skills/Python%20Wrangling/flag.txt.en)?

## Hints

1. Get the Python script accessible in your shell by entering the following command in the Terminal prompt: $ wget [https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py](https://mercury.picoctf.net/static/8e33ede04d02f3765b8c6a6e24d72733/ende.py)
2. $ man python

## Approach

I tried running the code in the IDE but that didn't work. I navigated to the directory where the Python file was (make sure the flag file is in the same directory) and used `python -d flag.txt.en` (-d for decode I'm guessing, -e is probably encode). This asked for the password which I pasted from pw.txt and then it outputted the flag.

## Flag

picoCTF{4p0110_1n_7h3_h0us3_aa821c16}
