from flask import Flask  
from sdes import tripledes

app = Flask(__name__)            

@app.route("/")


@app.route("/decipher=<string:cipher>/", methods=['GET', 'POST'])      


def decipher(cipher):     
    rawkey1 = [1,0,0,0,1,0,1,1,1,0]
    rawkey2 = [0,1,1,0,1,0,1,1,1,0]   
    #cipher2 = '10110110000101011000100001000110100010000100011001000110001000011011010101010111'

    print(cipher)

    plain = tripledes(rawkey1, rawkey2, cipher)   

    word = ''    
    for i in range(len(plain)):
        letter = ''.join(str(x) for x in plain[i])
        n = int(letter, 2)
        lett = chr(n)
        word += lett
    return word

    
if __name__ == "__main__":        
    app.run(debug=True)                             