# uBlacklist-filter-by-kdroidwin (Block malicious websites by Kdroidwin)


uBlacklist,uBlock Origin用のフィルター　
- 主に、詐欺サイトや偽サイト、悪質なアフィリエイトサイトを除外することが目的です。
- 誤検知があれば教えてください。Githubアカウントを持っていない人でも[Twitter](https://x.com/Kdroidwin1)もしくは[こちら](https://tally.so/r/wA5brD)からお願いします。

# Changelog(変更履歴)
重要
5/6 除外用のURL変更に伴い、再度uBlacklistに登録が必要

[完全な変更履歴](https://github.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/commits/main/)
<br>
<br>

# uBlacklist用フィルター購読方法

 1. [uBlacklist](https://iorate.github.io/ublacklist/ja/docs)をインストールしてください。
 2. 下の購読を押してください。

※uBlock Origin用のフィルターはuBlacklistには使えません。


# uBlacklist用 フィルターの種類
- １つ目のは基本的なフィルターです。
- 2つ目の購読の方は多少の誤ブロックが許せる方向けです。本来ブロックするべきではないサイトもブロックされる恐れがあります。実験的です。1つ目のフィルターに加えて使ってください。
- 3つ目の除外用は購読必須です。1つめと2つめのフィルターの誤爆を減らすためのものです。



<br>
<br>
chrome(chromiumの派生)ユーザー向け

[購読](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin&url=https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist.txt)

[購読2](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin2&url=https%3A%2F%2Fraw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist2.txt)

[除外用の購読](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin_exclusion&url=https%3A%2F%2Fraw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlacklist-Exclusion.txt)

<br>

Firefox及びそのフォークユーザー向け

[購読](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FKdroidwin%2FuBlacklist-filter-by-kdroidwin%2Fmain%2FuBlacklist.txt)

[購読2](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FKdroidwin%2FuBlacklist-filter-by-kdroidwin%2Fmain%2FuBlacklist2.txt)

[除外用の購読](https://ublacklist.github.io/rulesets/subscribe?url=https%3A%2F%2Fraw.githubusercontent.com%2FKdroidwin%2FuBlacklist-filter-by-kdroidwin%2Fmain%2FuBlacklist-Exclusion.txt)

下記はURL 
- uBlacklistのオプション＞購読＞購読を追加する からコピーボタンを押してコピーしたURLと適当な名前を入力してください。SafariユーザーはURLをコピーボタンを押してコピーしてください。
<br>
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

<br>
<br>

# uBlock Origin用フィルターの購読方法

フィルターリストのインポートから指定されたURLを入力してください。
ABP形式のコンテンツブロッカーの機能があるブラウザ(1DMブラウザなどにも対応しています。

# uBlock Origin 用フィルターの種類


- 検索結果には表示されますがアクセスを防ぐことができます。ただし、強力であるため、関係のないサイトまでブロックされることがあります。
- 2つめはuBlacklistが使えない人向け、もしくはuBlock origin以外の拡張機能をインストールしたくない人向け SearXNGの検索結果から非表示にします。SearXNG以外は対応していません。
- Androidアプリ版AdGuardにも対応していますが、誤検知したときにアプリを開く必要があるのであまり推奨はしていないです。

<br>
<br>

- Block malicious websites by Kdroidwin
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlockorigin.txt
```
購読推奨
メールアプリやSNSなどのアプリからリンクしたときなどに使えます。
⚠検索結果には表示されますがリンククリックするとuBlock Originのポップアップが出ます。

- uBlock Origin 用フィルター URL 検索結果非表示
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/sites/uBO-note.txt
```
SearXNGの一部のインスタンスにしか対応していません。 更新頻度は低いです。（実験的）

- Block specific note by Kdroidwin
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlacklist_converted-foruBo.txt
```
一部の中身のないnote記事をnote内のおすすめやnote内の検索結果から非表示にします。（実験的）

<br>
<br>

# 対象サイト

- いかがでしたかサイト(芸能ゴシップ記事など)
- 悪質なアフィリエイトサイト( UNEXTアフィリエイトやNordアフィリエイトなど。報酬が高い順にランキングを上げている)
- avast LINE opera Gmail などをおすすめソフトとして 紹介しているアフィリエイト記事(自社のソフトを紹介、もしくはステマ込み)※見たい人もいるのでかなりひどい記事のみ 条件厳しめにしている。
- LINE タウンWifi Lemon08 Tiktok とかを神アプリと紹介しているアフィリエイト系の記事
- DMMの紹介文と画像コピペしてアフィリエイトリンク挿入しただけの記事(レビューになっていない。)
- 詐欺サイト(ショッピング系など)
- 一部の役に立たないランキングサイト(mybestなど)
- 偽サイト(偽revanced、偽Githubリポジトリ、偽Z-Libなど)
- 一部SNS(pinterest等)
- 技術系スパムサイト(間違った情報) ※リストするサイトは条件厳しめに設定
- 危険なソフトウェアダウンロードサイト(マルウェア配布等)
- 悪質なまとめサイト（多すぎるので一部の悪質なサイトのみ）
- 誤った情報を多く含むサイト(AIのハルシネーション等)

<br>
<br>

# 貢献

URLの追加やミスの削除に協力していだける方は、レポジトリをForkして編集していただき、pull requestを送ってください。
issueでも構いません。並び替えはbotがやるので不要です。

Githubアカウントを持っていない方はTwitterもしくは[こちら](https://tally.so/r/wA5brD)からお願いします。

# Credits

Contains parts from Dandelion Sprout's Anti-Malware List  
by Dandelion Sprout  
https://github.com/DandelionSprout/adfilt  

License: Dandelicence v1.4  
https://github.com/DandelionSprout/Dandelicence
