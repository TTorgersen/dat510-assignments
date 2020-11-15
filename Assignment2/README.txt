Part1.py

In this part you need to have import the local script "sdes", but this is included already. 
The sdes script is the same as my previous assignment and is used to encrypt and decrypt with 3sdes. 
The first lines of part1.py is declaring variables for Alice and Bob
Blum-Blum-Shub is implemented as the cryptographically strong PRNG, where shared key is the input. 
Afterwards Alice sends a message with 3DES encryption, which Bob recieves and decrypts. 

#Part 2
Alice/Bob.py are identical scripts for each of the users. 
in these scripts there are multiple imports: 
flask, requests, prng (from part 1), sdes (local script)
requests may be required to be installed with pip
"python -m pip install requets" in the command terminal.

The route '/' is not in use. 
'/getpub' is used to give the other user my own key. 
'/getmsg' is used to retrieve a message from the other user
'/sendmsg' is a method used to send the already decided message. 