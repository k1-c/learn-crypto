# Learn Crypto

## Topics
- SHA256を使ったハッシュ化
- 秘密鍵の生成
- 楕円曲線暗号（ecdsa）を使った公開鍵の生成
- 圧縮公開鍵の生成（公開鍵圧縮のアルゴリズム）
  - 公開鍵は楕円曲線上の座標x, yで表される
  - 楕円曲線上のyがわかっている時、xは自明なので省略可能
  - よって正負のプレフィックスをつけて圧縮できる
  - yの値が正であれば02, 負であれば03

## 秘密鍵からアドレス生成までの流れ
![btc encryption](https://github.com/shunk-py/images/blob/master/btc-encryption.png)