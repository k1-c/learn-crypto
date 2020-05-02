import os
import ecdsa
import binascii

priv_key = os.urandom(32)
pub_key = ecdsa.SigningKey.from_string(
    priv_key, curve=ecdsa.SECP256k1).verifying_key.to_string()

# y座標を取り出す
pub_key_y = int.from_bytes(pub_key[32:], "big")

# 圧縮公開鍵を生成
if pub_key_y % 2 == 0:
    pub_key_compressed = b"\02" + pub_key[:32]
else:
    pub_key_compressed = b"\03" + pub_key[:32]

print(binascii.hexlify(pub_key))
print(binascii.hexlify(pub_key_compressed))