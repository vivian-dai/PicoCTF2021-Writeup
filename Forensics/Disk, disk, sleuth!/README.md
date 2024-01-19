# Disk, disk, sleuth

## Overview

Points: 110
Category: Forensics

## Description

Use `srch_strings` from the sleuthkit and some terminal-fu to find a flag in this disk image: [dds1-alpine.flag.img.gz](https://store7.gofile.io/download/7gZCkt/b5391e51dbaf80145bdff5839260a725/dds1-alpine.flag.img.gz)

## Hints

1. Have you ever used `file` to determine what a file was?
2. Relevant terminal-fu in picoGym: [https://play.picoctf.org/practice/challenge/85](https://play.picoctf.org/practice/challenge/85)
3. Mastering this terminal-fu would enable you to find the flag in a single command: [https://play.picoctf.org/practice/challenge/48](https://play.picoctf.org/practice/challenge/48)
4. Using your own computer, you could use qemu to boot from this disk!

## Approach

Ok for an 100+ pointer question, this was way too easy. The first hint asks if you've ever used `file` to determine what a file was. I thought this might mean the file extension had been changed to be misleading.

`file dds1-alpine.flag.img.gz` gave:
`dds1-alpine.flag.img.gz: gzip compressed data, was "dds1-alpine.flag.img", last modified: Tue Mar 16 00:19:51 2021, from Unix, original size modulo 2^32 134217728`

Ok very interesting, it's actually a gzip file meaning the extension is correct. We can unzip it with `gzip -d dds1-alpine.flag.img.gz` (`-d` means decompress aka unzip)

A [file](https://store7.gofile.io/download/7gZCkt/8d07bc9a337759e1b988fb050d6d14a1/dds1-alpine.flag.img) was extracted from the gzip file. I attempted to open it but that didn't work so I read the next hints.

The next hints were pointing to `grep` and outputing to a file. I thought I might as well try that but wasn't expecting any results.
`cat dds1-alpine.flag.img|strings|grep pico` this gave results.

```text
ffffffff81399ccf t pirq_pico_get
ffffffff81399cee t pirq_pico_set
ffffffff820adb46 t pico_router_probe
  SAY picoCTF{f0r3ns1c4t0r_n30phyt3_ad5c96c0}
```

## Flag

picoCTF{f0r3ns1c4t0r_n30phyt3_ad5c96c0}
