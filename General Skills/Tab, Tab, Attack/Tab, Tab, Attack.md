# Tab, Tab, Attack

## Overview

Points: 20
Category: General Skills

## Description

Using tabcomplete in the Terminal will add years to your life, esp. when dealing with long rambling directory structures and filenames: [Addadshashanammu.zip](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/General%20Skills/Tab,%20Tab,%20Attack/Addadshashanammu.zip)

## Hints

After `unzip`ing, this problem can be solved with 11 button-presses...(mostly Tab)...

## Approach

Um. There really isn't that many files. Unzip everything then have fun navigating using `ls` to list the folders/files and `cd <foldername>` to navigate there. Eventually there will be an [ELF file](https://github.com/vivian-dai/PicoCTF2021-Writeup/blob/main/General%20Skills/Tab,%20Tab,%20Attack/fang-of-haynekhtnamet) which named `fang-of-haynekhtnamet`
`./fang-of-haynekhtnamet` to run it.
It outputs:
`*ZAP!* picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}`

## Flag

picoCTF{l3v3l_up!_t4k3_4_r35t!_524e3dc4}
