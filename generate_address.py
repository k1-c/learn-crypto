import os
import ecdsa
import hashlib
import base58

priv_key = os.urandom(32)
pub_key = ecdsa.SigningKey.from_string(
    priv_key, curve=ecdsa.SECP256k1
).verifying_key.to_string()

# 非圧縮公開鍵のプレフィックスを付与
prefix_and_pubkey = b"\x04" + pub_key

intermediate = hashlib.sha256(prefix_and_pubkey).digest()

ripemd160 = hashlib.new("ripemd160")
ripemd160.update(intermediate)

# RIPEMD160でハッシュ160を生成
# SHA256 -> PIPEMDと２回ハッシュすることをまとめてHASH160と呼ばれる。
hash160 = ripemd160.digest()

# 公開鍵ハッシュのバージョンプレフィックスを付与
prefix_and_hash160 = b"\x00" + hash160

# hashlib.sha256が入れ子になってることを確認
double_hash = hashlib.sha256(hashlib.sha256(prefix_and_hash160).digest()).digest()

# 先頭４バイトを取り出す
checksum = double_hash[:4]

# チェックサムを末尾に付与し、base58でエンコード
pre_address = prefix_and_hash160 + checksum
address = base58.b58encode(pre_address)

print(address.decode())
