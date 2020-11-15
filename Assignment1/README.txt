Assignment 1

decrypt_1.py contains the methods used to solve part I in the assignment 
It can simply be run while opened and will return the decrypted plaintext, and the plaintext with the use of another keyword
To check the other ciphertext, edit the method call from ciph2 to ciph3 in 
decipher(ciph2, key) at line 175.

sdes.py contains the SDES and Triple-DES tasks. 
I created a main at line 355 which contains the method calls for all functions. 
Key generation method is uncommented, to test one of the functions uncomment a function such as: 
encrypted = sdes_encryption and its preceding print-line. 

web.py contains the local web server. 
This method can simply be run, and click the url for the localhost. 
Insert the following to get a working example: 
http://127.0.0.1:5000/decipher=10110110000101011000100001000110100010000100011001000110001000011011010101010111