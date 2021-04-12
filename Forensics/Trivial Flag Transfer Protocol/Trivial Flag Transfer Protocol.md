# Trivial Flag Transfer Protocol

## Overview

Points: 90
Category: Forensics

## Description

Figure out how they moved the [flag](./tftp.pcapng).

## Hints

1. What are some other ways to hide data?

## Approach

When looking at the [packet capture](./tftp.pcapng) using [Wireshark](https://www.wireshark.org/), I noticed there were a lot of files. ~~For some reason I thought [TFTP](https://en.wikipedia.org/wiki/Trivial_File_Transfer_Protocol) wasn't a legit protocol and was instead, something Pico made up but uhhhh I looked into it after solving this question lol.~~

To extract the files ~~watch [this video](https://www.youtube.com/watch?v=AMGerIJPUYU)~~, on Wireshark:

File > Export Objects > TFTP

which shows all the files recorded in the packet capture

![files](./files.png)

Click "Save All" to save them.

The files included [instructions.txt](./instructions.txt), [plan](./plan), [program.deb](./program.deb), [picture1.bmp](./picture1.bmp), [picture2.bmp](./picture2.bmp), and [picture3.bmp](.picture3.bmp). Let's analyze each of them individually.

### instructions.txt

Here are the contents of [instructions.txt](./instructions.txt):

```text
GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA
```

Wow! Encrypted data! My first thought was a [substitution](https://en.wikipedia.org/wiki/Substitution_cipher) of some sort. It turned out to be [ROT13](https://en.wikipedia.org/wiki/ROT13)

```text
TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN
```

I actually thought this was nonsense at first so I'll add in the spaces for you XD

> TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DISGUISE OUR FLAG TRANSFER. FIGURE OUT A WAY TO HIDE THE FLAG AND I WILL CHECK BACK FOR THE PLAN

Check back for the [plan](./plan)? Ok onto the the [plan](./plan)!

### plan

Here are the raw contents of [plan](./plan):

```text
VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF
```

Once again, it is encrypted using [ROT13](https://en.wikipedia.org/wiki/ROT13). Here's the decrypted message

```text
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

Here's some spaces:

> I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE. CHECK OUT THE PHOTOS

Hmmm "used the [program](./program.deb)"

### program.deb

I opened [program](./program.deb) using [7-zip](https://www.7-zip.org/) and found many files that seemed to all point to [steghide](http://steghide.sourceforge.net/).

### pictures

![picture1](./picture1.bmp)

![picture2](./picture2.bmp)

![picture3](./picture3.bmp)

In all honesty the actual content of the pictures themselves have absolutely nothing to do with anything. I just want to say the huge size of [picture2.bmp](./picture2.bmp) really threw me off.

### steghide and finally solving

There's a part on steghide's README titled "Quick-Start" that explains how to use it. I used the command `steghide info picture3.bmp` (no particular reason to start with 3, in this case it's just that picture3 is the one that had all the juicy info like the flag) and it prompted me for a passcode. ~~I was going to bruteforce the passcode~~ I remembered the contents of [plan](./plan):

```text
IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS
```

> ANDHIDITWITH-DUEDILIGENCE

What if "DUEDILIGENCE" was the password the flag is hidden with? With "DUEDILIGENCE" as the password, steghide revealed there's a flag.txt hidden inside picture3. Using `steghide extract -sf picture3.bmp` and "DUEDILIGENCE" as the password, [flag.txt](./flag.txt) was extracted.

## Flag

picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919}
