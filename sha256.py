import sys
import hashlib

print(sys.argv)

if len(sys.argv) == 2:
    # 引数をバイト文字列に変換
    hash_origin = sys.argv[1].encode()
    # SHA256でハッシュ化 / 16進数に変換
    hash = hashlib.sha256(hash_origin).hexdigest()
    print(hash)
else:
    print("error: invalid arguments")
