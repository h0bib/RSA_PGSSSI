# YAHIAOUI Hadj Habib | chaos.hh@gmail.com 
# PGS SSI 2018/2019
# Cryptanalyse et factorisation du RSA pour décrypter un message électronique
# Plateforme RSA & Attaques
# Module makeRSAKeys : Génération des clés publiques et privées 

import random, sys, os, primeNum, cryptomath


def main(nn):
    # Create a public/private keypair with 128 bit keys:
    print("")
    print('Making RSA-%s key files...' % (nn))
    PrimeLenth = int(nn/2)
    makeKeyFiles('ENIGMA', PrimeLenth)
    print("")
    print("Done, key files made.")

def generateKey(keySize):
    # Creates a public/private keys keySize bits in size.
    p = 0
    q = 0
    # Step 1: Create two prime numbers, p and q. Calculate n = p * q.
    print('Generating p & q primes...')
    print("")
    while p == q:
        p = primeNum.generateLargePrime(keySize)
        q = primeNum.generateLargePrime(keySize)
    n = p * q
    print('  p =', p)
    print('  q =', q)
    # Step 2: Create a number e that is relatively prime to (p-1)*(q-1):
    print("")
    print('Generating e that is relatively prime to (p-1)*(q-1)...')
    while True:
        # Keep trying random numbers for e until one is valid:
        #e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
        e = random.randrange(2 ** (30 - 1), 2 ** (30)) # change 30 to biger value to have biger exponent e
        if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
            break

    # Step 3: Calculate d, the mod inverse of e:
    print('Calculating d that is mod inverse of e...')
    d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

    publicKey = (n, e)
    privateKey = (n, d)
    print("")
    print("-----------------------------------------------------------------------------------------------------------------")
    print('Public key:', publicKey)
    print('Private key:', privateKey)
    print("-----------------------------------------------------------------------------------------------------------------")
    print("")

    return (publicKey, privateKey)


def makeKeyFiles(name, keySize):
    # Creates two files 'x_pubkey.txt' and 'x_privkey.txt' (where x
    # is the value in name) with the n,e and d,e integers written in
    # them, delimited by a comma.

    # Our safety check will prevent us from overwriting our old key files:
    if os.path.exists('%s_pubkey.txt' % (name)) or os.path.exists('%s_privkey.txt' % (name)):
        sys.exit('WARNING: The file %s_pubkey.txt or %s_privkey.txt already exists! Use a different name or delete these files and re-run this program.' % (name, name))

    publicKey, privateKey = generateKey(keySize)

    print('The public key is a %s and a %s digit number.' % (len(str(publicKey[0])), len(str(publicKey[1]))))
    print('Writing public key to file %s_pubkey.txt...' % (name))
    fo = open('%s_pubkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (int(keySize*2), publicKey[0], publicKey[1]))
    fo.close()
    print("")
    print('The private key is a %s and a %s digit number.' % (len(str(privateKey[0])), len(str(privateKey[1]))))
    print('Writing private key to file %s_privkey.txt...' % (name))
    fo = open('%s_privkey.txt' % (name), 'w')
    fo.write('%s,%s,%s' % (int(keySize*2), privateKey[0], privateKey[1]))
    fo.close()



if __name__ == '__main__':
    if len(sys.argv) > 1:
        try:   # Check if entered value is enteger, float or string
            N = int(sys.argv[1])  # N is integer - good
            main(N)
        except ValueError:
            try:
                N = float(sys.argv[1])  # N is float - error
                print(" ")
                print(" Error: input is not integer. It's a float")
            except ValueError: 
                print(" ")
                print(" Error: input is not integer. It's a string")   # else, N is string - error

    else:
        print("Usage: makeRSAKeys.py <N>", file=sys.stderr)