# Waving Flag

## Challenge Description

Can you invoke help flags for a tool or binary? [This program](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm) has extraordinarily helpful information...

## Challenge Information

Points: 10

## Hints

1. This program will only work in the webshell or another Linux computer.

2. To get the file accessible in your shell, enter the following in the Terminal prompt:
$ wget [https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm](https://mercury.picoctf.net/static/a14be2648c73e3cda5fc8490a2f476af/warm)

3. Run this program by entering the following in the Terminal prompt: $ ./warm, but you'll first have to make it executable with $ chmod +x warm

4. -h and --help are the most common arguments to give to programs to get more information from them!

5. Not every program implements help features like -h and --help.

## Solution

Download "this program", open it and search for "pico" in the search tab.
From there, you should be able to find the flag somewhere in the middle.

## Flag

>picoCTF{b1scu1ts_4nd_gr4vy_755f3544}
