import os
import binascii

# 32バイトの乱数を生成
priv_key = os.urandom(32)
print(priv_key)

# バイナリデータを16進数に変換
priv_key_hex = binascii.hexlify(priv_key)
print(priv_key_hex)
print(priv_key_hex.decode())
