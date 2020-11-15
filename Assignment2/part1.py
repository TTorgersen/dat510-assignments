import sdes
# Key exchange  DH 
#Public factors P, G
P = 353 #Prime number
G = 3   # shared value
print("Global parameters: ", "mod", P, "generator", G)
#Private key a and b
a = 97
b = 233
print("private key A", a, " and B ", b)
#public key generated x and y
x = (G**a%P)    
print('pubkey A', x)
y = (G**b%P)
print("pubkey B", y)
#Create shared key Ka and Kb
ka = y**a % P
print("sharedkey A", ka)
kb = x**b % P
print("sharedkey B", kb)

#Cryptographically strong pseudorandom number generator BBS
def prng(inKab):  #Shared key as input
    p = 11 # 11 mod 4 = 3
    q = 23 # 23 mod 4 = 3
    n = p * q
    kab = inKab
    bitlist = [None]*20
    for i in range(len(bitlist)):
        kab = kab**2
        nr = kab % n
        bit = nr & 1 #bitwise operation to get last bit
        bitlist[i] = bit
    rk1 = bitlist[0:10] #key 1
    rk2 = bitlist[10:20] #key 2 
    return(rk1, rk2)
rk1, rk2  = prng(ka)

#Alice message without spaces
message = "HiHowAreYou"

#From ascii to binary,  my sdes methods takes in binary as input https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa user jfs
def sendmes(rk1, rk2, message):
    print("Sent message: ", message)
    bits = bin(int.from_bytes(message.encode(), 'big'))[2:]
    bits2 = list(map(int, bits.zfill(8*((len(bits)+7) // 8))))
    encrypt = sdes.tripledes_generate(rk1, rk2, bits2)
    print(encrypt)
    return encrypt
encrypt = sendmes(rk1, rk2, message)

#Bob recieve and decrypt
def readmes(rk1, rk2, encrypt):
    plain = sdes.tripledes(rk1, rk2, encrypt)
    #From binary to ascii values, my sdes methods return binary as output https://stackoverflow.com/questions/10237926/convert-string-to-list-of-bits-and-viceversa user jfs
    n = int(''.join(map(str, plain)),2)
    plaintext = n.to_bytes((n.bit_length()+7) // 8, 'big').decode()

    print("Received message", plaintext)
    return plaintext
readmes(rk1, rk2, encrypt)