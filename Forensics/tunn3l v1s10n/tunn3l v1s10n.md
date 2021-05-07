# tunn3l v1s10n

Disclaimer: overall approach was taught to me by a friend, not solved during pico.

## Overview

Points: 40
Category: Forensics

## Description

We found this [file](./tunn3l_v1s10n). Recover the flag.

## Hints

1. Weird that it won't display right...

## Approach

There's no [file extension](https://en.wikipedia.org/wiki/Filename_extension) so we don't actually know what type of file it is.

Let's open this with a [hex editor](https://en.wikipedia.org/wiki/Hex_editor) like [HxD](https://mh-nexus.de/en/hxd/) to check the intended file type. The first two characters are `BM` which indicates a [BMP file](https://fileinfo.com/extension/bmp).

Let's change the file extension to `.bmp` and since it still doesn't open, I decided to use [ImageMagick](https://imagemagick.org/index.php) to open it. I'm sure there's probably some way of changing the file header to open it properly but that's alright. It displays:

![notaflag](./notaflag.png)

No flag hmmm. Something interesting to note is the size of the BMP file. It's about 2MB in size for such a tiny image? That doesn't seem right. [This site](http://www.ece.ualberta.ca/~elliott/ee552/studentAppNotes/2003_w/misc/bmp_file_format/bmp_file_format.htm) explains what everything in the BMP header is.

Height for a BMP file is at [offset](http://www.novell.com/documentation/ndsv8/usnds/c1help/novell_common/hexeditor.html) 0016h. I changed offset 0017h from 0x01 to 0x03.

Open in [ImageMagick](https://imagemagick.org/index.php):

![flag](./flag.png)

## Flag

picoCTF{qu1t3_a_v13w_2020}
