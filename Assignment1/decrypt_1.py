from collections import Counter
import time
ciphertext = ("BQZRMQ  KLBOXE  WCCEFL  DKRYYL  BVEHIZ  NYJQEE  BDYFJO  PTLOEM  EHOMIC  UYHHTS  GKNJFG EHIMK NIHCTI HVRIHA RSMGQT RQCSXX CSWTNK PTMNSW AMXVCY WEOGSR FFUEEB DKQLQZ WRKUCO  FTPLOT  GOJZRI  XEPZSE  ISXTCT  WZRMXI  RIHALE  SPRFAE  FVYORI  HNITRG  PUHITM CFCDLA  HIBKLH  RCDIMT  WQWTOR  DJCNDY  YWMJCN  HDUWOF  DPUPNG  BANULZ  NGYPQU LEUXOV  FFDCEE  YHQUXO   YOXQUO  DDCVIR  RPJCAT  RAQVFS  AWMJCN  HTSOXQ   UODDAG BANURR REZJGD VJSXOO MSDNIT RGPUHN HRSSSF VFSINH MSGPCM ZJCSLY GEWGQT DREASV FPXEAR IMLPZW EHQGMG WSEIXE GQKPRM XIBFWL IPCHYM OTNXYV FFDCEE YHASBA  TEXCJZ VTSGBA NUDYAP IUGTLD WLKVRIHWACZG PTRYCE VNQCUP AOSPEU KPCSNG RIHLRI KUMGFC YTDQES DAHCKP BDUJPX KPYMBD IWDQEF WSEVKT CDDWLI NEPZSE OPYIW ")
ciph2 = "".join(ciphertext.split())

ciphertext2 = ("BQZRMQKLAYAVAYITETEOFGWTEALRRDHNIFMLBIHHQYXXEXYVLPHFLWUOJILE GSDLKH BZGCTALHKAIZBIOIGKSZXLZSUTCPZWJHNPUSMSDITNOSKSJI EOKVILBKMSZB XZOEHAKTAWXPWLUEJMAIWGLRTZLVHZSATVQIHZWAXXZXDCIVTMLBIQRWZMLB VNGVQKAIZBXZ HVVMMAMJLRIWGKITZLVHZRRVYCBTVM FVOIYEFSKGKJAVWHUVBUHZSA EFLHMQHHVSGZXIKYTSYZXUUC KBTOGUVABLDPBGJCGFNLIIYA HJFWGG PSCPVAZEASMEMLGOYRCGFXVGEJTTTWTSAAILQFKEEPCPULXW WZRLVIVVYUMSMSILRI IBLWJITKWUXZGUZEJG DUCQEEQEOBTPSIHTGWUALVMAILTAEZTFLDPE IVEGYHPLZRTCYJVYGXABFNPQXLCEYARGIFCCWHBGIF WSYLBZMDWFPXKZSYCYAPJTFRCKTYYUYICYLR ZALETSDWHMGRPTTGUWCGFNTBJTRNWRAADNPQXLTBGPRZMJTFKGTSPVDTVAPEZPRIP")
ciph3 = "".join(ciphertext2.split())
#print(Counter(ciph2).most_common(5)) #returns E 35


def combo(iterable, size):
    length = len(iterable) - 1
    result = []
    for i in range(length):
        result.append(iterable[i:i+size])
    return result

size = 3
word_pairs = combo(ciph2, size)
#word_pairs = [''.join(i) for i in word_pairs if len(i) == size]


#print(Counter(word_pairs).most_common(4)) #returns RIH 5

most_freq = Counter(word_pairs).most_common(1)[0][0]
#print(most_freq) # RIH

word_list = []

def combopos(string):
    for x in range(len(string)):
        if string[x-2] == 'R': 
            if string[x-1] == 'I':
                if string[x] == 'H':
                    word_list.append(x-2)
                    word_list.append(x-1)
                    word_list.append(x)
    return word_list
combopos(ciph2)
    
#print(word_list)
plholder = []
factor_diff = []
def factor_difference(list_of_words):
    for p in range(len(list_of_words)):
        if p%3 == 0:
            plholder.append(list_of_words[p])
    
    for q in range(len(plholder)-1):
        factor_diff.append(plholder[q+1] - plholder[q])
    return factor_diff

factor_difference(word_list)
print(factor_diff)
numbers = []

def factorial(lista):
    for f in lista: 
        for i in range(1,f+1):
            if f%i == 0:
                numbers.append(i)
factorial(factor_diff)

keylengths = Counter(numbers).most_common(5)

keylength = keylengths[3][0]
 #1,2,4,8 keylength 1 and 2 are very unlikely, keylength 4 is unlikely. only 3 of the four has 16 as factor

alphabet = {}
freq_letter = {}
perc_letter = {}
for w in range(keylength):
    alphabet[w] = {}
    freq_letter[w] = {}
    perc_letter[w] = {}

def div_letter(text, k_length):
    i = 0
    for r in range(len(text)):
        if r%k_length == i:

            if str(text[r]) in alphabet[i]:
                alphabet[i][text[r]]+=1
            else:
                 alphabet[i].update({str(text[r]): 1})
            i += 1  
            if i > (k_length-1): i = 0

div_letter(ciph2, keylength)

#use english alphabet to compare with each alphabet
eng_alp = {'A':0.08167, 'B':0.01492, 'C':0.02782, 'D':0.04253, 'E':0.12702, 'F':0.0228, 'G':0.02015, 'H':0.06094, 'I':0.06996, 'J':0.00153, 'K':0.00772, 'L':0.04025, 'M':0.02406, 'N':0.06759, 'O':0.07507, 'P':0.01929, 'Q':0.00095, 'R':0.05987, 'S':0.06327, 'T':0.09056, 'U':0.02758, 'V':0.00978, 'W':0.0236, 'X':0.0015, 'Y':0.01974, 'Z':0.00074}
eng_len = 0.0
ciph_len = len(ciph2)

""" for k,v in eng_alp.items():
    eng_alp.update({k:v*ciph_len}) """

sum_list = []
chi_list = []
chi_hold = []
letter_list = []
solution_key = []
def chi_mode(alpha_list):
    
    for a in alpha_list:
        sum_list.append([])
        letter_list.append([])
        for i in alpha_list[a].values():
            sum_list[a].append(i)

    
    for i in alpha_list:
        for j,y in alpha_list[i].items():
            alpha_list[i][j] = y/(len(sum_list[i]))
    print(alpha_list[0])

    index = 26
    for a in alpha_list: # alpha_ list a 0-7
        current_alph = alpha_list[a]
        sum_dict = {}
        sum_list2 = []
        for i in range(index): #for shift 0-25 av bokstav K i liste a
            sum1 = 0.0
            for letter, e in eng_alp.items():
                letter = ord(letter)+i

                if(letter > 90):
                    letter=chr(letter-26)
                else: 
                    letter=chr(letter)

                if letter in current_alph: 
                    o = current_alph[letter] # o = 3

                    sum1 += ((o-e)**2)/e
                else: 
                    sum1 += ((-e)**2)/e

           # print(sum1)
            sum_list2.append(sum1)
            sum_dict[sum1] = chr(i+65)
       # print(min(sum_list2))
        kmy = sum_dict[min(sum_list2)]
        solution_key.append(kmy)

chi_mode(alphabet)

key = ''.join(str(x) for x in solution_key)




def decipher(ciphertext,key):
    key_length = len(key)
    key_index = []
    ciphertext_index = []

    for i in key: 
        key_index.append(ord(i))
    for i in ciphertext: 
        ciphertext_index.append(ord(i))
    plaintext = ''

    for i in range(len(ciphertext_index)):
        diff = (ciphertext_index[i] - key_index[i % key_length])
        val =  diff%26
        plaintext += chr(val+65) 

    print(plaintext)
    return plaintext

print('OG KEY:', key)
decipher(ciph2, key) 

def encrypt(plaintext, key):
    key_length = len(key)
    key_index = []
    plaintext_index = []

    for i in key: 
        key_index.append(ord(i))
    for i in plaintext: 
        plaintext_index.append(ord(i))
    ciphertext = ''

    for i in range(len(plaintext_index)):
        diff = (plaintext_index[i] + key_index[i % key_length])
        val =  diff%26
        ciphertext += chr(val+65) 

    return ciphertext 

### KEY lengths
# BDLAEKCY (8) = 0.02
# ABCDE = 0.0
# ABCDEFGHIJK
OGkey = key
testKey3 = 'ABC'
testKey5 = 'ABCDE'
testKey11 = 'ABJSDAKLDSPSASDFG'

def keyLength_test(OGkey, NEWkey, ciphertext):
    plain = decipher(ciphertext, OGkey)
    encryptTest = encrypt(plain, NEWkey)

    start_time = time.time()
    testDec = decipher(encryptTest, NEWkey)
    end_time = time.time()
    totTime = end_time - start_time
    totTime = "{:.5f}".format(totTime)
    print(end_time, start_time)
    print('test new key',testDec, NEWkey, totTime)

keyLength_test(OGkey, testKey11, ciph2)

""" ANORIGIN ANORIGIN          s = 0
    ZVPVWOGV ALMESSAG          s = -1
    DQTOBWUV EISKNOWN           s = -1
    DXARNTFP ASTHEPLA           s = +3
    HCBLXYFJ INTEXTWH           s = -1
    PVMXANWX ILETHECO           s = 7
    KMWFHMSQ DEDMESS            s = 7
    IFAECIBN
    JEQ
"""
"""
    #print(letter_list)
    #print(letter_list[0]) #letterlist[x] contains 26 alphabets starting from x = 0 to 25
    sum_bokst = []
    sum_listeshift = []
                if (ord(k)+i > 90):
                    k = chr(ord(k)+i-26)
                else: 
                    k = chr(ord(k)+i) """   
"""     for k in range(0,index):
        sum_listeshift.append([])
        sum_bokst.append([])
        for j in range(len(letter_list[0][k])):
            print(letter_list)
            sum_bokst[k].append([letter_list[0][k]])
           # print(k,letter_list[0][k][j][0])
        sum_bokstav_tall = 0.0
        for u in range(len(sum_bokst[k])):
            sum_bokstav_tall += sum_bokst[k][u][0]
            #print(sum_bokstav_tall,k)
        sum_listeshift[k].append([sum_bokstav_tall,k])
    print(sum_listeshift)
    print(min(sum_listeshift))
    mini = min(sum_listeshift)
    print(mini[0][1]) """

    #print(chr(65+mini[0][1]))



""" for h in range(8):
    print(min(perc_letter[h].values())) """

"""                     perc_letter[a][i] = ({k:v/(sum(sum_list[a]))*100})  #v prosent acutal for bokstav
                    print(perc_letter[a][i]) """
"""                 perc_letter[a].append({k:v/(sum(sum_list[a]))*100}) #v = prosent for bokstav
                for n,w in eng_alp.items():
                    if k == n: 
                        perc_letter[a].append({k:((v-w)**2/(w))}) #v = chi value for letter k=n
                #at this moment sum(perc_letter[x].values) gives correct chi for list X with shift 0 """
""" guessletters = ['E', 'T', 'A']
ciphword = []
guessword = []
keyword = []
def create_keyword(ciphletters, guess):
    for l in ciphletters[0]: 
        ciphword.append(ord(l)-65)
    for i in guess:
        guessword.append(ord(i)-65)

    for i in range(len(ciphword)):
        print(abs(ciphword[i]-guessword[i]))
        s = abs(ciphword[i]-guessword[i])
        keyword.append(chr(s+65))
    print(keyword)

create_keyword(freq_letter, guessletters) """

""" Chi squared (o-e)^2 / e
O = B-Z
E = A 
"""
""" 
1.Lag en funksjon som sjekker antall bokstaver mellom hver gang RIH oppstår
2.Finne ut hvilke faktorer som finnes i disse tallene (nøkkellengde)
3.For nøkkellengde, lag en liste som inneholder hver i-te bokstav fra nøkkelordet
4.For hver nye liste med bokstaver, sjekk hyppigheten av bokstavene
5.Test ut hvilken kombinasjon av bokstavene som gir rett plaintekst
6. Lag en metode som trenger en nøkkel og en tekst og deciphrer

"""




""" Function that takes in a KEY and Ciphertext that returns Plaintext"""
"""   for k in range(len(KEY)):
    index_list.append(ord(KEY[k])-65)
print(index_list) """
