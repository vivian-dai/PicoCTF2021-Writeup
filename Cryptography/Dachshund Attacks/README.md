# Dachshund Attacks

## Challenge Description

What if d is too small? Connect with nc mercury.picoctf.net 36463.

## Challenge Information

Points: 80

## Hints

1) What do you think about my pet? [dachshund.jpg](./dachshund.jpg)

## Solution

Connecting to nc mercury.picoctf.net 36463 in the webshell, it gives us the values of e, n and c. Give it like 10 seconds for it to return these values. As you could probably tell, it's encrypted using RSA.

Now, the picture in the hint refers to Dachshund dogs. Searching up "dachshund" on Google, it returns a lot of results, but we're mostly looking for different names for dachshund dogs. Thus, searching up "different names for dachshund dogs" it gives some relevant pages one of them being this wonderful Wikipedia page. [Dachshund Dogs](https://en.wikipedia.org/wiki/Dachshund#:~:text=Although%20%22dachshund%22%20is%20a%20German,wiener%20dog%20or%20sausage%20dog.)

By searching up "Wiener RSA", we see that it's an attack method used on RSA, especially when "d" is too small (it says it in the challenge description!). [Wiener's Attack](https://en.wikipedia.org/wiki/Wiener%27s_attack)

There's an already designed and availible Python3 implementation of Wiener attack which can be found here: [Weiner Attack Python3 Implementation](https://pypi.org/project/owiener/) Run the command in shell, and it should install the implementation.

From here, we need to find "d" using the Wiener attack method. Thus, I decided to write a small program to solve for "d" basing it off of the example given in the website.

````python
import owiener

c = 51729254814612320597643328450085959536599727372680938760771949307679773005615308695648114596258975136775968889388756216401496118257971113771919925769604554578645725822883285841825381936016630539284003180253228150727414300152034618534378132051795168049160397854013369582290350212981743918731826059625571659195
e = 26708677238429428374170262208931535733743911260604248499407092969454401069520229604707421630650361943655516583033522359546446670546154254638564481680864845797555129549483370241281955795119447253220108830835178572671949509316867647933241089013588496517578768012481040939437738400995777121296915356470885241301
n = 102050270322368919270668432655276557677924971440195120212230040263372875358539516722287129116966588442412373177849929844163493405962383401732877189240511737479294203917101072408029656805628085793609392233931279848866908950627490592662932946058562223278970874388262808195065269805169207346022676107536878090839
d = owiener.attack(e, n)

if d is None:
    print("Failed")

else :
    print("Hacked d = {}".format(d))
````

As you can see, the values for c, e and n are included already, and it uses the command owiener.attack(e,n) to solve for "d". If there is a d value, it will print the value.

By adding the following line:

````python
M = pow(c, d, n)

print("Decrypted message: ", M)
````

By using the built-in python command pow, it allows it to decrypt the message giving the following:

> 198614235373674103788888306985643587194108045477674049828366797219789354877

Converting this number to to hex, we get the following (feel free to find an online converter to speed up the process):

> 7069636F4354467B70726F76696E675F7769656E65725F323633353435377D

Now converting the hexadecimal to plaintext we get the flag.

## Flag

picoCTF{proving_wiener_2635457}
