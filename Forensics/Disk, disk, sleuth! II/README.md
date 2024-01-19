# Disk, disk, sleuth! II

## Overview

Points: 130
Category: Forensics

## Description

All we know is the file with the flag is named `down-at-the-bottom.txt`... Disk image: [dds2-alpine.flag.img.gz](https://srv-store6.gofile.io/download/OqFIZV/88e49ad83469300f94781a0fca88e9c5/dds2-alpine.flag.img.gz)

## Hints

1. The sleuthkit has some great tools for this challenge as well.
2. Sleuthkit docs here are so helpful: [TSK Tool Overview](http://wiki.sleuthkit.org/index.php?title=TSK_Tool_Overview)
3. This disk can also be booted with qemu!

## Approach

First the file is zipped. Unzip it with `gzip -d dds2-alpine.flag.img`

After the file is unzipped, the [image file](https://srv-store1.gofile.io/download/OqFIZV/cdbb01f6ece33855c5e24d3ca48581ed/dds2-alpine.flag.img) should be visible.

`mmls dds2-alpine.flag.img` returned details about the disc image:

```text
DOS Partition Table
Offset Sector: 0
Units are in 512-byte sectors

      Slot      Start        End          Length       Description
000:  Meta      0000000000   0000000000   0000000001   Primary Table (#0)
001:  -------   0000000000   0000002047   0000002048   Unallocated
002:  000:000   0000002048   0000262143   0000260096   Linux (0x83)
```

By the way, [this video](https://www.youtube.com/watch?v=ld9RW3pxAKg) gives a really good overview on how to use The Sleuth Kit.

It seems that the first two partitions probably don't have anything interesting in it. Partition at index 002 begins at 2048. I used `fls -o 2048 dds2-alpine.flag.img` to check the contents of that partition.

```text
d/d 11: lost+found
r/r 12: .dockerenv
d/d 20321:      bin
d/d 4065:       boot
d/d 6097:       dev
d/d 2033:       etc
d/d 26417:      home
d/d 8129:       lib
d/d 14225:      media
d/d 16257:      mnt
d/d 18289:      opt
d/d 16258:      proc
d/d 18290:      root
d/d 16259:      run
d/d 18292:      sbin
d/d 12222:      srv
d/d 16260:      sys
d/d 18369:      tmp
d/d 12223:      usr
d/d 14229:      var
V/V 32513:      $OrphanFiles
```

I figured the `root` directory would be a good starting point. `root` has control to everything and CTFs store important things in places with admin permissions. `fls -o 2048 dds2-alpine.flag.img 18290`:

```text
r/r 18291:      down-at-the-bottom.txt
```

It took me a while to figure out how to use the `icat` command but eventually, `icat -o 2048 dds2-alpine.flag.img 18291` worked:

```text
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( p ) ( i ) ( c ) ( o ) ( C ) ( T ) ( F ) ( { ) ( f ) ( 0 ) ( r ) ( 3 ) ( n )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( s ) ( 1 ) ( c ) ( 4 ) ( t ) ( 0 ) ( r ) ( _ ) ( n ) ( 0 ) ( v ) ( 1 ) ( c )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
   _     _     _     _     _     _     _     _     _     _     _
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \
 ( 3 ) ( _ ) ( 6 ) ( 9 ) ( a ) ( b ) ( 1 ) ( d ) ( c ) ( 8 ) ( } )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/
  ```

## Flag

picoCTF{f0r3ns1c4t0r_n0v1c3_69ab1dc8}
