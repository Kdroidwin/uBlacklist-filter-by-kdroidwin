# uBlacklist-filter-by-kdroidwin


uBlacklist,uBlock Origin用のフィルター　
- 主に、詐欺サイトや偽サイト、悪質なアフィリエイトサイトを除外することが目的です。
- 誤検知があれば教えてください。Githubアカウントを持っていない方はTwitterもしくは[こちら](https://tally.so/r/wA5brD)からお願いします。

# Changelog(変更履歴)
重要
5/6 除外用のURL変更に伴い、再度uBlacklistに登録が必要

[完全な変更履歴](https://github.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/commits/main/)


# フィルター購読 やり方

 1. [uBlacklist](https://iorate.github.io/ublacklist/ja/docs)をインストールしてください。
 2. chromeユーザーは下の購読を押してください。Firefox、SafariユーザーはURLをコピーボタンを押してコピーしてください。

※uBlock Origin用のフィルターはuBlacklistには使えません。
ABP形式のコンテンツブロッカーの機能があるブラウザ(cromiteなど)にも対応しています。フィルターリストのインポートから指定されたURLを入力してください。

# uBlacklist用 フィルターの種類
- １つ目のは基本的にインストール推奨です。
- 2つ目の購読の方は多少の誤ブロックが許せる方向けです。本来ブロックするべきではないサイトもブロックされる恐れがあります。実験的です。1つ目のフィルターに加えて使ってください。(必ず１つ目のフィルターも購読する必要があります。)
- 3つ目の除外用は購読必須です。1つめと2つめのフィルターの誤爆を減らすためのものです。


> [!IMPORTANT]
>Firefox,Safariユーザーは購読が押せないです。uBlacklistのオプション＞購読＞購読を追加する からコピーボタンを押してコピーしたURLと適当な名前を入力してください。

chrome(chromiumの派生)ユーザー向け

[購読](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin&url=https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist.txt)

[購読2](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin2&url=https%3A%2F%2Fraw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist2.txt)

[除外用の購読](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin_exclusion&url=https%3A%2F%2Fraw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlacklist-Exclusion.txt)


Firefox,Safariユーザー向け

下記はURL 
- uBlacklistフィルター1 by Kdroidwin URL
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist.txt
```

- uBlacklistフィルター2 by Kdroidwin URL(実験的)
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist2.txt
```

- uBlacklist exclusionフィルター(除外用) by Kdroidwin URL
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlacklist-Exclusion.txt
```

# uBlock Origin Cromite用 フィルターの種類


- フィルターリストのインポートから追加できます。検索結果には表示されますがアクセスを防ぐことができます。ただし、強力であるため、関係のないサイトまでブロックされることがあります。
- 2つめはCromiteなどを使用していてuBlacklistが使えない人向け、もしくはuBlock origin以外の拡張機能をインストールしたくない人向け SearXNGの検索結果から非表示にします。SearXNG以外は対応していません。
- Androidアプリ版AdGuardにも対応していますが、誤検知したときにアプリを開く必要があります。

- uBlock Origin 用フィルター URL
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlockorigin.txt
```
uBlock Origin用はメールアプリやSNSなどのアプリからリンクしたときなどに使えるがまだ実験的です。
⚠検索結果には表示されますがリンククリックするとuBlock originのポップアップが出ます。

- uBlock Origin 用フィルター URL 検索結果非表示
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlacklist_converted-foruBo.txt
```
SearXNGの一部のインスタンスにしか対応していません。
更新頻度は低いです。

# 対象サイト

- いかがでしたかサイト(芸能ゴシップ記事など)
- UNEXTアフィリエイトやNordアフィリエイトなどお金をもらってランキング上げている悪質なアフィリエイトサイト
- avast LINE opera Gmail とかをおすすめソフト 紹介しているアフィリエイト記事(自社の有料ソフトを紹介、もしくはステマ込み)※見たい人もいるのでかなりひどい記事のみ 条件厳しめにしている。
- LINE タウンWifi Lemon08 Tiktok とかを神アプリと紹介している明らかにアフィリエイト系の記事
- DMMの紹介文と画像コピペしてアフィリンク挿入しただけの記事
- 詐欺サイト(ショッピング系など)
- 一部ランキングサイト(mybestなど)
- 偽サイト(偽revanced、偽Githubリポジトリ、偽Z-Libなど)
- 一部SNS(Tiktok Instagram はてなブックマーク pinterest等)
- 技術系スパムサイト(間違った情報) ※条件厳しめ
- 危険なソフトウェアダウンロードサイト
- まとめサイト（多すぎるので悪質なサイトのみ）
- 誤った情報を多く含むサイト(AIのハルシネーション等)


# 貢献

URLの追加やミスの削除に協力していだける方は、レポジトリをForkして編集していただき、pull requestを送ってください。
issueでも構いません。

Githubアカウントを持っていない方はTwitterもしくは[こちら](https://tally.so/r/wA5brD)からお願いします。

# 補足
Kiwi browserでDuckDuckGo、SearXNGが使えない問題を修正
[uBlacklist for Kiwi (mod)](https://github.com/Kdroidwin/ublacklist)
