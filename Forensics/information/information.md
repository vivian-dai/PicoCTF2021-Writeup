# information

## Overview

Points: 10
Category: Forensics

## Description

Files can always be changed in a secret way. Can you find the flag? [cat.jpg](./cat.jpg)

## Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

## Approach

I downloaded the file and tried to see if there were any plaintext strings in it. There weren't.
The first hint was to look at the details of the file. I used [this](https://29a.ch/photo-forensics/#strings) site to find the strings inside the file. It gave the contents of [`information.xml`](./information.xml)

The resouce line looks promising. `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9` could be a base64 text. Decoded it using [this](https://www.base64decode.org/) site.

## Flag

picoCTF{the_m3tadata_1s_modified}
