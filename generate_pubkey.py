import os
import ecdsa
import binascii

priv_key = os.urandom(32)
pub_key = ecdsa.SigningKey.from_string(
    priv_key, curve=ecdsa.SECP256k1
).verifying_key.to_string()

print("private key:")
print(binascii.hexlify(priv_key))
print("public key:")
print(binascii.hexlify(pub_key))
