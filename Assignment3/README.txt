This assigment has three files: 
Main.py (which performs the calculations)
Alice.py 
Bob.py 

Alice and Bob are almost identical scripts. 
They have the same p and q, which then creates the same n and phi. 
In these files the libraries such as flask, requests, hashlib, random, math are improted. 
These files are also similar as the previous assignments with the methods:
/getpub, /getmsg, /sendmsg

To run the code: 
    simply start the localhost servers. When Bob asks for a message from Alice, the console outputs "Enter message:"
    Then you can enter any length of sentence, that will be hashed and encrypted. 

Main.py
- create key E 
    - uses computeGCD method
- create modular inverse E
- encrypt block from a hash string
- decrypt block from list of numbers

