def prng(inKab): 
    p = 11
    q = 23
    n = p * q
    kab = inKab
    bitlist = [None]*20
    for i in range(len(bitlist)):
        kab = kab**2
        nr = kab % n
        bit = nr & 1 #bitwise operation to get last bit
        bitlist[i] = bit
    rk1 = bitlist[0:10]
    rk2 = bitlist[10:20]
    return(rk1, rk2)