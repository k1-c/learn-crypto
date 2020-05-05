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
- アドレスの作成
  - Base58→人が見て読み間違えやすい文字列を排除したエンコード方式
  - Base58Check→チェックサムの導入
- 非決定性ウォレットと決定性ウォレット
- BIP32とBIP44
- 階層的決定性ウォレット
- 拡張鍵


## 秘密鍵からアドレス生成までの流れ
![btc encryption](https://github.com/shunk-py/images/blob/master/btc-encryption.png)

## 圧縮公開鍵と非圧縮公開鍵
|プレフィックス|意味|
|:---:|:---:|
|x02|正の座標|
|x03|負の座標|
|x04|非圧縮公開鍵|

## Base58Checkエンコードのプロセス
![base58check encode](https://github.com/shunk-py/images/blob/master/base58check-encode.png)

## 代表的なバージョンバイト
|バージョンバイト|意味|エンコード後|
|:---:|:---:|:---:|
|0x00|公開鍵ハッシュ|1|
|0x05|スクリプトハッシュ|3|
|0x08|秘密鍵WIF方式|5|
|0x0488B21E|BIP32拡張公開鍵|xpub|

## アドレス作成の流れ
- 公開鍵をSHA-256でハッシュ化（①）
- ①をRIPEMD-160でハッシュ化（②）
- ②をBase58Checkエンコード

## BIP44に定めるHDウォレットのパスの仕様
`m / purpose' / coin_type' / account' / change / address_index`

## HD Walletにおけるマスター鍵の導出プロセス
![generate hd master key](https://github.com/shunk-py/images/blob/master/generate-hd-master-key.png)

## HD Walletにおける子鍵の導出プロセス
![generate hd child key](https://github.com/shunk-py/images/blob/master/generate-hd-child-key.png)