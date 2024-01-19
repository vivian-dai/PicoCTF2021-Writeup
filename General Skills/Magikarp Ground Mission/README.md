# Magikarp Ground Mission

## Overview

Points: 30
Category: General Skills

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6d448c9c`

## Hints

1. Finding a cheatsheet for bash would be really helpful!

## Approach

Hmm start by connecting to the server with `ssh ctf-player@venus.picoctf.net -p 50713` and `6d448c9c` as the password like the question says.

Using `ls` lists `1of3.flag.txt  instructions-to-2of3.txt`

With `cat 1of3.flag.txt`, we get

```text
picoCTF{xxsh_
```

`cat instructions-to-2of3.txt` says

```text
Next, go to the root of all things, more succinctly `/`
```

I typed in `cd ..` (go back a directory) then `ls -a` (list all because I have trust issues with hidden files) and came across `3of3.flag.txt`

`cat 3of3.flag.txt` gave

```text
5190b070}
```

I kept going back (with `cd ..`) and listing the files and directories (`ls -a`) until `2of3.flag.txt` appeared.

`cat 2of3.flag.txt` gave

```text
0ut_0f_\/\/4t3r_
```

## Flag

picoCTF{xxsh_0ut_0f_\/\/4t3r_5190b070}
