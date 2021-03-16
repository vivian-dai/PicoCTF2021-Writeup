# Weird File

## Overview

Points: 20
Category: Forensics

## Description

What could go wrong if we let Word documents run programs? (aka "in-the-clear"). [Download file](https://github.com/v341196137/PicoCTF2021-Writeup/blob/main/Forensics/Weird%20File/weird.docm).

## Hints

[https://www.youtube.com/watch?v=Y7IJjnLGqTQ](https://www.youtube.com/watch?v=Y7IJjnLGqTQ)

## Approach

I watched about 3 minutes of the video. The description and the video are both pointing towards macros which are potentially malicious programs which is a wonderful feature for hackers!
After opening the file in Microsoft word, I navigated to view, and macros.
![view](https://github.com/v341196137/PicoCTF2021-Writeup/blob/main/Forensics/Weird%20File/view.png)
[Here](https://support.microsoft.com/en-us/office/macros-or-vba-code-found-5e836a6e-cce5-494a-b0b8-2ce739d35f2f) is a better explanation on how to view macros.

Inside the macros, this code is found:

```vb
 Sub runpython()

Dim Ret_Val
Args = """" '"""
Ret_Val = Shell("python -c 'print(\"cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9\")'" & " " & Args, vbNormalFocus)
If Ret_Val = 0 Then
   MsgBox "Couldn't run python script!", vbOKOnly
End If
```

`cGljb0NURnttNGNyMHNfcl9kNG5nM3IwdXN9` this string looks promising.
It looks like [base 64](https://www.base64decode.org/)

## Flag

picoCTF{m4cr0s_r_d4ng3r0us}
