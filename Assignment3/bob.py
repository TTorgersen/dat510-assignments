from flask import Flask
import requests
import hashlib
import random
import math
from main import  getE, inversemod, encryptblock, decryptblock
import time

app = Flask(__name__)         

p = 3442143121370103686316674040079725703
q = 18764264852184498752189732920671430769

start = time.time()
n = p*q
print("Modulo N: ",n)
print("Bit lenght of N: ", n.bit_length())

phi = (p-1)*(q-1)
print("Phi (n) : ", phi)
e = getE(phi) #public key
print("Public key: ", e)

d = inversemod(e, phi) #private key
print("Private key: ", d)

end = time.time()
print("Time key generation: " , end-start)
@app.route("/getpub")
def setup():

    print("Bob public key: ", e) #only this value is returned
    return str(e) #public key

@app.route("/getmsg", methods=['GET', 'POST'])     
def getmsg():
    r = requests.get('http://127.0.0.1:8000/getpub') #request bob pubkey
    e1 = int(r.text) #bob key
    print("Alice public key", e1)

    v = requests.get("http://127.0.0.1:8000/sendmsg")
    #Receive M and encrypted hash M2
    returns = v.text.split(',')
    start3 = time.time()

    #hash the Original word
    h = returns[0]
    ha = hashlib.sha512(h.encode())
    has = str(ha.hexdigest()) #one way hash 1
    print("Received message to hash", has)
    #DSS received encrtypted hash

    ms = []
    M1 = returns[1]
    M1 = M1[1:]
    ms.append(int(M1))
    Mm1 = returns[-1]
    Mm1 = Mm1[:-1]

    M = returns[2:-1]
    for m in M:
        m = m.strip()
        m = int(m)
        ms.append(m)
    
    ms.append(int(Mm1))

    #decrypt list of numbers
    deced = decryptblock(ms, e1, n)
    hexed = '{:06x}'.format(deced) #one way hash 2
    end3 = time.time()
    print("Decryption time: ", end3-start3)
    print("Decrypted alice hash : ", hexed)

    if(hexed == has):
        answer = True
    else: 
        answer = False
    return(str(answer) + "  " +str(has) +"   "+str(hexed))



@app.route("/sendmsg", methods=['GET', 'POST'])     
def sendmsg():
    message = input("Enter a message:")

    start2 = time.time()
    hashM = hashlib.sha512(message.encode()) #send this to alice
    print("Original:", message)
    hash = str(hashM.hexdigest()) 
    hash2 = int(hash, 16) 

    #Encrypt method
    det = encryptblock(hash2, d, n)

    end2 = time.time()
    print("Hash and Sign time: ", end2-start2)
    return(str(message) +","+str(det))   

if __name__ == "__main__":        
    app.run(debug=True, port=5000)                          