# It is my Birthday

## Description

I sent out 2 invitations to all of my friends for my birthday! I'll know if they get stolen because the two invites look similar, and they even have the same md5 hash, but they are slightly different! You wouldn't believe how long it took me to find a collision. Anyway, see if you're invited by submitting 2 PDFs to my website. [http://mercury.picoctf.net:11590/](http://mercury.picoctf.net:11590/)

## Hints

1. Look at the category of this problem.
2. How may a PHP site check the rules in the description?

## Approach

I searched up "MD5 collision" and eventually found [this](https://www.mscs.dal.ca/~selinger/md5collision/) website. It provided 2 executable files ([hello](./hello.pdf) and [erase](./erase.pdf)) which have the same MD5 hash. I downloaded those files and changed the extension to a .pdf file.

I uploaded those two files and the website redirected to the [PHP](./source.php):

The flag can be found in a comment at the end of the PHP (before the HTML portion, line [37](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/53bed8a7177440cca590ed45ed4a6ed142ca8515/Web%20Exploitation/It%20is%20my%20Birthday/source.php#L37))

## Flag

picoCTF{c0ngr4ts_u_r_1nv1t3d_3d3e4c57}
