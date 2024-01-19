# Ancient History

## Overview

Points: 10
Category: Web Exploitation

## Description

I must have been sleep hacking or something, I don't remember visiting all of these sites... [http://mercury.picoctf.net:52731/](http://mercury.picoctf.net:52731/) (try a couple different browsers if it's not working right)

## Hints

1. What kind of information can JavaScript modify?
2. If you want to do this the un-fun way, the obfuscation is pretty lazy. (got removed)
3. Don't rely on viewing the list all at once in your browser, sometimes the browser doesn't show all the flag characters. So instead, go through them one at a time. If that doesn't work, then you can try a totally different approach by digging around until you find the windows to the past.

## Approach

Haha I probably did this the "un-fun" way. First upon inspecting the page, I realized there's a lot of JavaScript [*stuff*](./stuff.js).

...as you can see... that's a lot of *stuff*.
I noticed some commands that look like:

```js
window.history.pushState({urlpath:'/index.html?p'}, "", '/index.html?p');
```

The `?p` is the first character in "picoCTF". By manually searching for "url" and assembling the characters together one by one, the flag can be obtained.

## Flag

picoCTF{th4ts_k1nd4_n34t_bb660d55}
