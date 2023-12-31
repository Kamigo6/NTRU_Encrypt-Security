# Illustration of NTRU Encrypt for only 1 block of message
from ntru import Ntru
import poly


# ----------Parameter selection--------------
print("=============NTRU Public Key Cryptosystem===============")
N = int(input("Enter value for N: "))
p = int(input("Enter value for p: "))
q = int(input("Enter value for q: "))

# -------------Key generation----------------
# Set f and g
print("Enter the coefficient for f:")
# -1 1 1 0 -1 0 1 0 0 1 -1
f = [int(x) for x in input().split()]
print("Enter the coefficient for g:")
# -1 0 1 1 0 1 0 0 -1 0 -1 
g = [int(x) for x in input().split()]

Bob = Ntru(N, p, q)
Bob.genPublicKey(f, g)
pub_key = Bob.getPublicKey()
print("Public Key Generated by Bob: ", poly.cenPoly(pub_key, q))

# ---------------Encryption------------------
print("\n-----------------------Encryption--------------------------\n")
Alice = Ntru(N, p, q)
Alice.setPublicKey(pub_key)

print("Enter the coefficient for message:")
# -1 0 0 1 -1 0 0 0 -1 1 1
msg = [int(x) for x in input().split()]

print("Enter the coefficient for random polynomial:")
# -1 0 1 1 1 -1 0 -1 0 0 0
r = [int(x) for x in input().split()]
print("Random Polynomial: ", r)

encrypt_msg = Alice.encrypt(msg, r)
print("Encrypted Message: ", poly.cenPoly(encrypt_msg, q))


# ---------------Decryption------------------
print("\n-----------------------Decryption--------------------------\n")
print("Bob decrypts message sent to him")
[a, b, c] = Bob.decrypt(encrypt_msg)
a = poly.cenPoly(a, q)
b = poly.cenPoly(b, p)
c = poly.cenPoly(c, p)
print("a = f*e (mod q) = ", a)
print("b = a (mod p) = ", b)
print("c = f_p.b (mod p) = ", c)
print("\nDecrypted Message:", c)
