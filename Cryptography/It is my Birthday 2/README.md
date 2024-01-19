# It is my Birthday 2

## Overview

Points: 170
Category: Cryptography

## Description

My birthday is coming up again, but I want to have a very exclusive party for only the best cryptologists. See if you can solve my challenge, upload 2 valid PDFs that are different but have the same SHA1 hash. They should both have the same 1000 bytes at the end as the original invite. [http://mercury.picoctf.net:59127/](http://mercury.picoctf.net:59127/) [invite.pdf](./invite.pdf)

## Hints

1. This isn't REALLY a birthday attack problem
2. [https://shattered.io/](https://shattered.io/)
3. The PDFs cannot be the same
4. The PDFs must be valid
5. The last 1000 bytes of each PDF must match the last 1000 bytes of the original

## Approach

They sent a [website](https://shattered.io/) about the first SHA-1 collision files ever made under the second hint. In the website there are two PDFs with the same SHA-1 hash. The question also asks for the last 1000 bytes of the PDFs to be the same as the [original](./invite.pdf). Hashes work dependent on the portion that came before.

If files A and B have the same hash, then C is added to the end of both, then A appended with C will still have the same hash as B appended with C because hashes are only dependent on the part that comes before.

I didn't really want to figure out what the last 1000 bytes of the original file was so I opened the original file with [HxD](https://mh-nexus.de/en/hxd/), copied the entire hex content of it, then pasted it at the bottom of both SHA-1 breaking files. PDFs don't read anything after "EOF" (end of file) so this is still a valid file.

These file creations ended up creating [this](./shattered-1.pdf) and [this](./shattered-2.pdf) which are two very valid PDF files with the last 1000 bytes that are the same as the original and have the same SHA-1 hash.

## Flag

picoCTF{h4ppy_b1rthd4y_2_m3_96ee9031}
