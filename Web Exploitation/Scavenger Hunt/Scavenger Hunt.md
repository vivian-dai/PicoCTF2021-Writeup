# Scavenger Hunt

## Overview

Points: 50
Category: Web Exploitation

## Desctipion

There is some interesting information hidden around this site [http://mercury.picoctf.net:44070/](http://mercury.picoctf.net:44070/). Can you find it?

## Hints

1. You should have enough hints to find the files, don't run a brute forcer.

## Approach

Clicking on the link brings us to some boring HTML. Ctrl + Shift + I will show the source code of the page:

```html
<html><head>
    <title>Scavenger Hunt</title>
    <link href="https://fonts.googleapis.com/css?family=Open+Sans|Roboto" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="mycss.css">
    <script type="application/javascript" src="myjs.js"></script>
  </head>

  <body>
    <div class="container">
      <header>
        <h1>Just some boring HTML</h1>
      </header>

      <button class="tablink" onclick="openTab('tabintro', this, '#222')" id="defaultOpen" style="background-color: rgb(34, 34, 34);">How</button>
      <button class="tablink" onclick="openTab('tababout', this, '#222')" style="">What</button>

      <div id="tabintro" class="tabcontent" style="display: block;">
        <h3>How</h3>
        <p>How do you like my website?</p>
      </div>

      <div id="tababout" class="tabcontent" style="display: none;">
        <h3>What</h3>
        <p>I used these to make this site: <br>
            HTML <br>
            CSS <br>
            JS (JavaScript)
        </p>
    <!-- Here's the first part of the flag: picoCTF{t -->
      </div>

    </div>

  

</body></html>
```

This comment `<!-- Here's the first part of the flag: picoCTF{t -->` gives us the first part of the flag.

Next, there are some files linked to it like the CSS and JS.

```html
<link rel="stylesheet" type="text/css" href="mycss.css">
<script type="application/javascript" src="myjs.js"></script>
```

Adding `/mycss.css` to the URL gives access to the CSS file

```css
div.container {
    width: 100%;
}

header {
    background-color: black;
    padding: 1em;
    color: white;
    clear: left;
    text-align: center;
}

body {
    font-family: Roboto;
}

h1 {
    color: white;
}

p {
    font-family: "Open Sans";
}

.tablink {
    background-color: #555;
    color: white;
    float: left;
    border: none;
    outline: none;
    cursor: pointer;
    padding: 14px 16px;
    font-size: 17px;
    width: 50%;
}

.tablink:hover {
    background-color: #777;
}

.tabcontent {
    color: #111;
    display: none;
    padding: 50px;
    text-align: center;
}

#tabintro { background-color: #ccc; }
#tababout { background-color: #ccc; }

/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */
```

Nice, here's the next part of the flag `/* CSS makes the page look nice, and yes, it also has part of the flag. Here's part 2: h4ts_4_l0 */`

Next, we can check out the JS by replacing `mycss.css` with `myjs.js`. The JS file reveals:

```js
function openTab(tabName,elmnt,color) {
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].style.backgroundColor = "";
    }
    document.getElementById(tabName).style.display = "block";
    if(elmnt.style != null) {
        elmnt.style.backgroundColor = color;
    }
}

window.onload = function() {
    openTab('tabintro', this, '#222');
}

/* How can I keep Google from indexing my website? */
```

`/* How can I keep Google from indexing my website? */` hmmm. I searched up "index website on google" and it brought up things about web crawlers. [This](https://www.google.com/search/howsearchworks/crawling-indexing/) made me think it's possible a robots exclusion file (robots.txt) might have something. I changed `myjs.js` to `robots.txt`

```text
User-agent: *
Disallow: /index.html
# Part 3: t_0f_pl4c
# I think this is an apache server... can you Access the next flag?
```

Alright! The comments give part 3 of the flag as well as a hint for the next part.

The [.htacess](https://phoenixnap.com/kbhow-to-set-up-enable-htaccess-apache) file manages Apache server permissions. Replacing `robots.txt` with `.htaccess` got this:

```text
# Part 4: 3s_2_lO0k
# I love making websites on my Mac, I can Store a lot of information there.
```

What stands out the most about that hint is the capitalized "Store". In Macs, a [`.DS_Store` file](https://en.wikipedia.org/wiki/.DS_Store) stores the configurations for how the desktop looks (eg. icon location, etc.) Changing `.htacess` with `.DS_Store` got

```text
Congrats! You completed the scavenger hunt. Part 5: _7a46d25d}
```

## Flag

picoCTF{th4ts_4_l0t_0f_pl4c3s_2_lO0k_7a46d25d}
