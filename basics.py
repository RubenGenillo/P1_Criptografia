import math

def to_numbers(text):
    return [ord(letter) - 65 for letter in list(text.upper())]



def to_letters(nums):
    characters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] 
    return"".join([ characters[integer] for integer in nums])


def egcd(a,b):
    return (a, b, math.gcd (a,b))



def modinv_rec(p,q,y,r):
    if r == 1:
        return r,-q
    x,z = modinv_rec(y,y//r,r, y%r)
    return z , (x-z*q)

def modinv(a, m):
    if egcd(a,m)[2] != 1:
        raise ValueError("offending value")
    if a == 1:
        return m + 1
    x, y = modinv_rec(m,m//a, a, m%a)
    if y < 0:
        y = y + 26
    return y

def xor_bytes(a,b):
    retorno = []
    for i in range(len(a)):
        retorno.append( a[i] ^ b[i] )
    return   bytes(retorno)


