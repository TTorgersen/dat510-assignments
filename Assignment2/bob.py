from flask import Flask
import requests
from prng import prng
import sdes
P = 353
G = 3
b = 233 
y = (G**b%P) 
app = Flask(__name__)           

@app.route("/getpub")
def setup():
    print("Global parameters: ", P, G)
    print("Bob private key: ", b)
    print("Bob public key: ", y) #only this value is returned
    return str(y) #public key


#Call the method 8000/getmsg
#Decoder message with shared key
# Return plaintext  
@app.route("/getmsg", methods=['GET', 'POST'])     
def getmsg():
    r = requests.get("http://127.0.0.1:8000/getpub")#get alice pubkey
    x = int(r.text) #alice key
    kb = x**b % P
    print("shared key", kb)
    rk1, rk2 = prng(kb)
    v = requests.get("http://127.0.0.1:8000/sendmsg")
    encrypt = v.text
    
    plain = sdes.tripledes(rk1, rk2, encrypt)  

    #convert plaintext to readable format
    n = int(''.join(map(str, plain)),2)
    plaintext = n.to_bytes((n.bit_length()+7) // 8, 'big').decode() #Big refers to the msb being at the beginning of the string/array.
    print("received message from alice: ", plaintext)
    return(plaintext)


#Sendmsg function
#Encode message with shared key
#Return koded message

@app.route("/sendmsg", methods=['GET', 'POST'])     
def sendmsg():
    message = "IAmFineAndYou"
    print("sending message to alice: ", message)
    r = requests.get("http://127.0.0.1:8000/getpub") #get alice pubkey
    x = int(r.text) #alice key
    kb = x**b % P
    print(" shared key", kb)
    rk1, rk2 = prng(kb)

    # Convert message to correct format
    bits = bin(int.from_bytes(message.encode(), 'big'))[2:] #Big refers to the msb being at the beginning of the string/array.
    bits2 = list(map(int, bits.zfill(8*((len(bits)+7) // 8))))
    #Encrypt with key1 and key2
    encrypt = sdes.tripledes_generate(rk1, rk2, bits2)
    encrypted = ''.join([str(el) for el in encrypt])
    print("bob encrypted", encrypted)
    return(encrypted)


if __name__ == "__main__":        
    app.run(debug=True, port=5000)                         