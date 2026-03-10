# YAHIAOUI Hadj Habib | chaos.hh@gmail.com 
# PGS SSI 2018/2019
# Cryptanalyse et factorisation du RSA pour décrypter un message électronique
# Plateforme RSA & Attaques
# Module ModInv : calcule l'exposant de déchiffrement en utilisant l'inverse modulaire


# put the values of p, q and e here :
p=10417037966006109733   
q=15260333411323805533
e = 666766235
#------------------------------------
n = p*q
phi = (p-1)*(q-1)

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    g, y, x = egcd(b%a,a)
    return (g, x - (b//a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('No modular inverse')
    return x%m


d = modinv(e, phi)
print(" ")
print('P =', p)
print('Q =', q)
print('N =', n)
print('Phi =', phi)
print('e =', e)
print(" ")
print("The exponent d is found:")
print("----------------------------------------------------------------------")
print('d =', d)
print("----------------------------------------------------------------------")
print("")
print('(e*d)%Phi =', (e*d)%phi)