# Matryoshka doll

## Overview

Points: 30
Category: Forensics

## Description

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: [this](./dolls.jpg)

## Hints

1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

## Approach

Hiding files inside of files really stumped me until I found [a video](https://youtu.be/KUZVIBXfoeA?t=221). I opened the file in [HxD](https://mh-nexus.de/en/hxd/) and it turns out that was exactly what it is. I searched for "IEND" and selected the part from "PK" to the end of the file, copied the hex portion and pasted it onto a new file to create a new file. After that I navigated into the zip folder and repeated this process about 5 times before being given a `flag.txt` file which contains:

> p i c o C T F { e 3 f 3 7 8 f e 6 c 1 e a 7 f 6 b c 5 a c 2 c 3 d 6 8 0 1 c 1 f }

I mean it's perfectly possible to jam it all together manually but here's a [Python script](./script.py) to do it

## Alternative Approach

You can also use Binwalk. it's a tool that allows you to search binary images for embedded files and executable code. I found a zip file inside and extracted it using this command:
```bash
binwalk -e dolls.png
```
keep doing that and you'll get to flag.txt

visit this [link](https://infosecwriteups.com/beginners-ctf-guide-finding-hidden-data-in-images-e3be9e34ae0d) to learn more.

## Flag

picoCTF{e3f378fe6c1ea7f6bc5ac2c3d6801c1f}
