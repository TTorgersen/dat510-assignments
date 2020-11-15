import hashlib
import random
import math

#Compute gcd 
def computeGCD(a,b): #Source: https://www.geeksforgeeks.org/gcd-in-python/
    while(b):
        a,b = b, a%b
    return a

#encryption key e : 1<e < phi, gcd(e, phi) = 1
def getE(phi):
    key = []
    for i in range(round(phi/2), phi): #compute many gcds
        gcd = computeGCD(phi, i) 
        
        if gcd == 1:  #only store the gcd that are gcd(e,phi) =1
            key.append(i)
            if len(key) == 1000: 
                break
    e = random.choice(key) #chooses a random number in the list of approved keys.
    return e

#decryption key d : 0 < d < n , e*d = 1 mod phi
#need to be multiplicate inverse modulo

def inversemod(e, phi): 
    e = e %phi
    d = pow(e, -1, mod=phi)
    print("Confirm mod inverse: ", d*e%phi)
    return d
"""     for d in range(1,phi): #Source: https://www.geeksforgeeks.org/multiplicative-inverse-under-modulo-m/
        if pow(e,d,phi) == 1:
           return d """


#Encryption method for block 
#hString is the hex values for the hash pub key received from sender
def encryptblock(hString, pub, n): #Other users public key
    hashList = []
    while hString: 
        tall = hString&0x7fff #15 bits from the hString   15 < bit size of n    
        encTall = pow(tall,pub,n) #encrypt 
        hashList.append(encTall) #store encrypt value
        hString = hString >> 15 #bitshift to the next 15 bits
    hashList.reverse() #Reverse the list to be in the correct order
    return hashList

#Decryption
#Takes a list of encrypted numbers as input, private key as key.
def decryptblock(cryptList, priv, n):
    start = 0
    for i in cryptList:
        start  = start << 15 #bit shift by 15
        start |= pow(i, priv,n) #decrypt the number i and store it to the variable start(int)
    return start
        


