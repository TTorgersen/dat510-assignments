import time

def sdes_key_generation(rkey):
    perm_key = []
    LS_1 = []
    LS_2 = []
    LS_2_2 = []
    LS_1_2 = []
    subk_1 = []
    subk_2 = []

    P10 = [3,5,2,7,4,10,1,9,8,6]
    for i in P10:
        perm_key.append(rkey[i-1])
    
                                    
    for i in  range(len(perm_key)): 
        if i < 5: 
            LS_1.append(perm_key[i])
        else: 
            LS_2.append(perm_key[i])    
    
    LS_1.append(LS_1.pop(0))
    LS_2.append(LS_2.pop(0))

    LS_1_2 = LS_1.copy()
    LS_2_2 = LS_2.copy()
    

    LS_1.extend(LS_2)
    P8 = [6,3,7,4,8,5,10,9]

    for i in P8: 
        subk_1.append(LS_1[i-1])

    #Subkey 2
    LS_1_2.append(LS_1_2.pop(0))
    LS_1_2.append(LS_1_2.pop(0))
    LS_2_2.append(LS_2_2.pop(0))
    LS_2_2.append(LS_2_2.pop(0))
    LS_1_2.extend(LS_2_2)

    for i in P8: 
        subk_2.append(LS_1_2[i-1])
    return(subk_1, subk_2)


def sdes_fk1(fbitsl,fbitsr, key):
    EP = [4,1,2,3,2,3,4,1]
    mapped =[]

    for k in EP: 
        mapped.append(fbitsr[k-1])
    xored = [] 


    for h in range(len(mapped)):
        xored.append(int(mapped[h])^int(key[h]))


    # split the xored
    sL = xored[0:4]
    sR = xored[4:8]

    #S0 S-box
    lb1 = ''
    lb1 += str(sL[0])
    lb1 += str(sL[3])
    lb1 = int(lb1,2)

    lb2 = ''
    lb2 += str(sL[1])
    lb2 += str(sL[2])
    lb2 = int(lb2,2)

    rb1 = ''
    rb1 += str(sR[0])
    rb1 += str(sR[3])
    rb1 = int(rb1,2)
    rb2 = ''
    rb2 += str(sR[1])
    rb2 += str(sR[2])
    rb2 = int(rb2,2)

    S0 = [[1,0,3,2],
    [3,2,1,0],
    [0,2,1,3], 
    [3,1,3,2]]

    p4_1 = S0[lb1][lb2]

    S1 = [[0,1,2,3],
    [2,0,1,3],
    [3,0,1,0], 
    [2,1,0,3]]

    p4_2 = S1[rb1][rb2]

    bin1 = f'{p4_1:02b}'
    bin2 = f'{p4_2:02b}'
    fourbit2 = []
    fourbit2 +=[bin1[0],bin1[1], bin2[0], bin2[1]]


    P4 = [2,4,3,1]
    bit4 = []
    for l in P4:
        bit4.append(int(fourbit2[l-1]))

    bitReturn = []
    for o in range(len(bit4)):
        bitReturn.append(bit4[o]^int(fbitsl[o]))
    return bitReturn

def sdes_fk2(fbitsl,fbitsr, key):
    EP = [4,1,2,3,2,3,4,1]
    mapped =[]
    for k in EP: 
        mapped.append(fbitsr[k-1])
    xored = [] 

    for h in range(len(mapped)):
        xored.append(mapped[h]^int(key[h]))


    # split the xored
    sL = xored[0:4]
    sR = xored[4:8]

    #S0 S-box
    lb1 = ''
    lb1 += str(sL[0])
    lb1 += str(sL[3])
    lb1 = int(lb1,2)

    lb2 = ''
    lb2 += str(sL[1])
    lb2 += str(sL[2])
    lb2 = int(lb2,2)

    rb1 = ''
    rb1 += str(sR[0])
    rb1 += str(sR[3])
    rb1 = int(rb1,2)
    rb2 = ''
    rb2 += str(sR[1])
    rb2 += str(sR[2])
    rb2 = int(rb2,2)

    S0 = [[1,0,3,2],
    [3,2,1,0],
    [0,2,1,3], 
    [3,1,3,2]]

    p4_1 = S0[lb1][lb2]

    S1 = [[0,1,2,3],
    [2,0,1,3],
    [3,0,1,0], 
    [2,1,0,3]]

    p4_2 = S1[rb1][rb2]

    bin1 = f'{p4_1:02b}'
    bin2 = f'{p4_2:02b}'
    fourbit2 = []
    fourbit2 +=[bin1[0],bin1[1], bin2[0], bin2[1]]

    P4 = [2,4,3,1]
    bit4 = []
    for l in P4:
        bit4.append(int(fourbit2[l-1]))

    bitReturn = []
    for o in range(len(bit4)):
        bitReturn.append(bit4[o]^int(fbitsl[o]))
    return bitReturn

def sdes_encryption(rawkey, plaintext):
    subk1, subk2 = sdes_key_generation(rawkey)
    LS4 = []
    RS4 = []
    IP = [2,6,3,1,4,8,5,7]
    perm_key2 = []
    for i in IP: 
        perm_key2.append(plaintext[i-1])
    LS4 = perm_key2[0:4]
    RS4 = perm_key2[4:8]      

    #function fk
    #F - mapping
    fk1 = sdes_fk1(LS4, RS4,subk1)

    fk2 = sdes_fk2(RS4, fk1, subk2)
    permfk = []
    permfk += fk2
    permfk += fk1
    result = []

    iIP = [4,1,3,5,7,2,8,6]
    for l in iIP:
        result.append(permfk[l-1])
    #print('Ciphertext result', result)
    return result

def sdes_decryption(rawkey,ciphertext):
    subk1, subk2 = sdes_key_generation(rawkey)
    LS4 = []
    RS4 = []
    IP = [2,6,3,1,4,8,5,7]
    perm_key2 = []
    for i in IP: 
        perm_key2.append(ciphertext[i-1])
    LS4 = perm_key2[0:4]
    RS4 = perm_key2[4:8]      

    #function fk
    #F - mapping

    #RS4, subk1
    fk1 = sdes_fk1(LS4, RS4,subk2)

    fk2 = sdes_fk2(RS4, fk1, subk1)
    permfk = []
    permfk += fk2
    permfk += fk1
    result = []

    iIP = [4,1,3,5,7,2,8,6]
    for l in iIP:
        result.append(permfk[l-1])
    #print('Plaintext result', result)
    return result



def triple_des(plaintext):
    enc1 = sdes_encryption(raw_key_1,plaintext)
    dec1 = sdes_decryption(raw_key_2,enc1)
    enc3 = sdes_encryption(raw_key_1,dec1)
    
    #print('Tripledes ciphertext: ', enc3)
    return(enc3)

def triple_des_decrypt(raw_key_1, raw_key_2, ciphertext):
    dec1 = sdes_decryption(raw_key_1,ciphertext)
    enc1 = sdes_encryption(raw_key_2,dec1)
    dec2 = sdes_decryption(raw_key_1, enc1)
    #print('Tripledes plaintext: ',dec2)
    return(dec2)

#Task 3 Cracking SDES
def crack_sdes(text1):
    start_time = time.time()

    with open(text1, 'r') as c: 
        s = c.read()
        letters = []
        for i in range(len(s)):
            if i%8 == 0:
                letters.append(s[i:i+8])

        keyList = []

        for k in range(1024):
            k2 = "{0:010b}".format(k)
            keyList.append(k2)  

        for k3 in keyList:  
            decrypted = []  
            for l in range(len(letters)):
                decrypt = sdes_decryption(k3,str(letters[l]))
                decletter = ''.join(str(x) for x in decrypt)
                n = int(decletter,2)
                if(n >= 65 and n <= 90): 
                    decrypted.append(chr(n))
                elif(n >= 97 and n <= 122):
                    decrypted.append(chr(n))
                else: 
                    break

                if(len(decrypted) == len(letters)):
                    returntxt = ''.join(str(x) for x in decrypted)
                    print('Key: ', k3)
                    print('Plaintext: ', returntxt)
                    end_time = time.time()
                    s = end_time - start_time
                    print('time',s)
                    return k3, decrypted


def crack_3des(text2):
    start_time = time.time()
    with open(text2, 'r') as c: 
        s = c.read()
        letters = []
        for i in range(len(s)):
            if i%8 == 0:
                letters.append(s[i:i+8])

        keyList = []

        for k in range(1024):
            k2 = "{0:010b}".format(k)
            keyList.append(k2)  

        for k3 in keyList:  
            print(k3)
            for k4 in keyList: 
                decrypted = []  
                for l in range(len(letters)):
                    decrypt = triple_des_decrypt(k3, k4, str(letters[l]))
                    decletter = ''.join(str(x) for x in decrypt)
                    n = int(decletter,2)
                    if(n >= 65 and n <= 90): 
                        decrypted.append(chr(n))
                    elif(n >= 97 and n <= 122):
                        decrypted.append(chr(n))
                    else: 
                        break

                    if(len(decrypted) == len(letters)):
                        returntxt = ''.join(str(x) for x in decrypted)
                        print('Keys: ', k3, k4)
                        print('Plaintext: ', returntxt)
                        end_time = time.time()
                        totTime = end_time - start_time
                        print('Time used: ', totTime)
                        return k3,k4, decrypted


#task 4 generate ciphertext
def tripledes_generate(k1,k2,plain): 
    returntext = []
    for i in range(len(plain)):
        if i%8 == 0: 
            enc1 = sdes_encryption(k1,plain[i:i+8])
            dec1 = sdes_decryption(k2,enc1)
            enc3 = sdes_encryption(k1,dec1)
            returntext.append(enc3)
    print(returntext)
    return returntext
#task 4 method call
def tripledes(k1,k2,cipher): 
    returntext = []
    for i in range(len(cipher)):
        if i%8 == 0: 
            dec1 = sdes_decryption(k1,cipher[i:i+8])
            enc1 = sdes_encryption(k2,dec1)
            dec2 = sdes_decryption(k1, enc1)
            returntext.append(dec2)
    print(returntext)
    return returntext

if __name__ == "__main__":    
    raw_key_1 = [1,0,0,0,1,0,1,1,1,0]
    raw_key_2 = [0,1,1,0,1,0,1,1,1,0]
    plaintext = [0,1,0,1,0,1,0,1]
    ciphertext = [0,1,0,1,0,0,0,0]    

    sdes_key_generation(raw_key_1) #Key Generation

    #encrypted = sdes_encryption(raw_key_1,plaintext) #SDES encryption
    #print('encrypted: ',encrypted)

   # decrypted = sdes_decryption(raw_key_1,ciphertext) #SDES decryption
   # print('decrypted: ', decrypted)

 

    #trides = triple_des(plaintext) #Triple DES encryption
    #print('Triple des encryption: ', trides)

   # trides_dec = triple_des_decrypt(raw_key_1, raw_key_2, ciphertext) #Triple des decryption
   # print('Triple des decryption: ', trides_dec)

  

    crackKey, crackText = crack_sdes('cxt1.txt') #Crack with SDES
    print('Cracked key and text: ', crackKey, crackText) 

    #crackKey1, crackKey2, crackText2 = crack_3des('cxt2.txt') #Crack with triple des
    #print('Cracked keys and text: ', crackKey1, crackKey2, crackText2)

    # TASK 4

    rawkey1 = [1,0,0,0,1,0,1,1,1,0]
    rawkey2 = [0,1,1,0,1,0,1,1,1,0]   
    cipher = '0110000110100110111010111000111110010011000011111000110110111010'
    plain = '01010100011010000110100101110011011010010111001101110011011000010110011001100101' 
    #tripledes(rawkey1,rawkey2, cipher)
    #newciph = tripledes_generate(rawkey1, rawkey2, plain)








