import os
import binascii
import ecdsa
import hmac
import hashlib


seed = os.urandom(32)
root_key = b"Bitcoin Seed"


def hmac_sha512(data, keymessage):
    hash = hmac.new(data, keymessage, hashlib.sha512).digest()
    return hash


def create_pubkey(priv_key):
    pub_key = ecdsa.SigningKey.from_string(
        priv_key, curve=ecdsa.SECP256k1
    ).verifying_key.to_string()
    return pub_key


master = hmac_sha512(seed, root_key)
master_secretkey = master[:32]
master_chaincode = master[32:]
master_pubkey = create_pubkey(master_secretkey)

master_pubkey_integer = int.from_bytes(master_pubkey[32:], byteorder="big")

# 圧縮公開鍵作成
if master_pubkey_integer % 2 == 0:
    master_pubkey_x = b"\x02" + master_pubkey[:32]
else:
    master_pubkey_x = b"\x03" + master_pubkey[:32]

# マスター秘密鍵
print("マスター秘密鍵")
print(binascii.hexlify(master_secretkey))
# マスターチェーンコード
print("\n")
print("マスターチェーンコード")
print(binascii.hexlify(master_chaincode))
# マスター圧縮公開鍵
print("\n")
print("マスター公開鍵")
print(binascii.hexlify(master_pubkey_x))

# 以下子秘密鍵の作成

index = 0
index_bytes = index.to_bytes(8, "big")
data = master_pubkey_x + index_bytes
result_hmac512 = hmac_sha512(data, master_chaincode)

# 親秘密鍵とHMACSHA512の結果の前半部分を足し合わせる
sum_integer = int.from_bytes(master_secretkey, "big") + int.from_bytes(
    result_hmac512[:32], "big"
)

p = 2 ** 256 - 2 ** 32 - 2 ** 9 - 2 ** 8 - 2 ** 7 - 2 ** 6 - 2 ** 4 - 1
child_secretkey = (sum_integer % p).to_bytes(32, "big")

# 子秘密鍵（マスターから見て１つ下の秘密鍵）
print("\n")
print("子秘密鍵")
print(binascii.hexlify(child_secretkey))
