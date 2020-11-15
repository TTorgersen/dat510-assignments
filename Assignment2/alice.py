from flask import Flask
import requests
from prng import prng 
import sdes
P = 353
G = 3
a = 97
x = (G**a%P)

app = Flask(__name__)           

@app.route("/getpub")
def setup():
    print("Global parameters: ", P, G)
    print("Alice private key: ", a)
    print("Alice public key: ", x) #only this value is returned
    return str(x) #public key

@app.route("/getmsg", methods=['GET', 'POST'])     
def getmsg():
    r = requests.get('http://127.0.0.1:5000/getpub') #request bob pubkey
    y = int(r.text) #bob key
    ka = y**a % P
    print(" shared key", ka)
    rk1, rk2 = prng(ka)
    v = requests.get("http://127.0.0.1:5000/sendmsg")
    encrypt = v.text
    plain = sdes.tripledes(rk1, rk2, encrypt)

    #Convert to readable format
    n = int(''.join(map(str, plain)),2)
    plaintext = n.to_bytes((n.bit_length()+7) // 8, 'big').decode()  #Big refers to the msb being at the beginning of the string/array.
    print("receieved message from bob: ", plaintext)
    return(plaintext)

@app.route("/sendmsg", methods=['GET', 'POST'])     
def sendmsg():
    message = "HiHowAreYou"
    print("Sending message to bob: ", message)
    r = requests.get('http://127.0.0.1:5000/getpub') #request bob pub key
    y = int(r.text) #bob key
    ka = y**a % P
    print(" shared key", ka)
    rk1, rk2 = prng(ka)

    #Converts the message to correct format
    bits = bin(int.from_bytes(message.encode(), 'big'))[2:] #Big refers to the msb being at the beginning of the string/array.
    bits2 = list(map(int, bits.zfill(8*((len(bits)+7) // 8))))
    #Encrypt with key1,key2
    encrypt = sdes.tripledes_generate(rk1, rk2, bits2)
    encrypted = ''.join([str(el) for el in encrypt])
    print("alice encrypted", encrypted)
    return(encrypted)   

if __name__ == "__main__":        
    app.run(debug=True, port=8000)                         