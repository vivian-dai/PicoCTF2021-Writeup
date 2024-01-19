# MacroHard WeakEdge

## Overview

Points: 60
Category: Forensics

## Desscription

I've hidden a flag in this file. Can you find it? [Forensics is fun.pptm](./Forensics%20is%20fun.pptm)

## Approach

The best approach to finding files hidden inside other files is [`binwalk`](https://tools.kali.org/forensics/binwalk)

If we perform `binwalk "Forensics is fun.pptm"` we'll see there's a bunch of [`.zip`](https://en.wikipedia.org/wiki/ZIP_(file_format)) files. We can extract it using `binwalk -e "Forensics is fun.pptm"` (`-e` or `--extract` for extract)

Now there's `_Forensics is fun.pptm.extracted` folder which I will navigate using [7zip](https://www.7-zip.org/).

Since there's too many things in `0.zip` I decided I might as well automate the search process. I extracted `0.zip` then navigated to it in the terminal.

The rest was very guessy, I tried `grep -r pico` (find recursively) for things like "pico" or "{" except none of it was useful. I tried `find -D tree|grep flag` in hopes of finding a flag file which also didn't work. Eventually after some guessing I tried `find -D tree|grep hidden` which returned:

```console
./ppt/slideMasters/hidden
```

Navigate to `cat ./ppt/slideMasters/hidden`:

```text
Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q
```

This doesn't look like any kind of substitution cipher, might be base 64 so that's worth a try.

First we should write a script to get rid of the spaces:

```python
s = "Z m x h Z z o g c G l j b 0 N U R n t E M W R f d V 9 r b j B 3 X 3 B w d H N f c l 9 6 M X A 1 f Q"
s = s.split(" ")
print("".join(s))
```

This gave "ZmxhZzogcGljb0NURntEMWRfdV9rbjB3X3BwdHNfcl96MXA1fQ" which we can then decode using [this website](https://www.base64decode.org/)

## Flag

picoCTF{D1d_u_kn0w_ppts_r_z1p5}

## After Thoughts

P.S. I didn't know ppts are zips but hey, that's a cool fact
