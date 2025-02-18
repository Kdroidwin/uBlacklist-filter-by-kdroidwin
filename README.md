# uBlacklist-filter-by-kdroidwin


uBlacklist 用のフィルター　
- 主に、詐欺サイトや偽サイト、悪質なアフィリエイトサイトを除外することが目的です。

Filters for uBlacklist　
- The main purpose is to exclude fraudulent or fake sites.

# フィルター購読 やり方

- [uBlacklist](https://iorate.github.io/ublacklist/ja/docs)をインストールしてください。
- その後、chromeユーザーは下の購読を押してください。FirefoxユーザーはURLをコピーボタンを押してコピーしてください。
- 2つ目の購読の方は多少の誤爆が許せる方向けです。1つ目のフィルターに加えて使ってください。(必ず１つ目のフィルターも購読する必要があります。)
- 3つ目の除外用は購読必須です。
- 4つ目のはuBlock Origin用です。実験的です。フィルターリストのインポートから追加できます。

> [!IMPORTANT]
>Firefoxユーザーは購読が押せないです。uBlacklistのオプション＞購読＞購読を追加する からコピーボタンを押してコピーしたURLと適当な名前を入力してください。

chromeユーザー向け

[購読](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin&url=https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist.txt)

[購読2](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin2&url=https%3A%2F%2Fraw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist2.txt)

[除外用の購読](https://iorate.github.io/ublacklist/subscribe?name=uBlacklist-filter-by-kdroidwin_exclusion&url=https%3A%2F%2Fraw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/Exclusion.txt)

Firefoxユーザー向け

下記はURL 
- uBlacklistフィルター1 by Kdroidwin URL
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist.txt
```

- uBlacklistフィルター2 by Kdroidwin URL
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/main/uBlacklist2.txt
```

- uBlacklist exclusionフィルター(除外用) by Kdroidwin URL
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/Exclusion.txt
```



- uBlock origin 用フィルター URL（実験的）
```
https://raw.githubusercontent.com/Kdroidwin/uBlacklist-filter-by-kdroidwin/refs/heads/main/uBlockorigin.txt
```
uBlock Origin用はメールアプリやSNSなどのアプリからリンクしたときなどに使えるがまだ実験的です。

# 対象サイト

- いかがでしたかサイト(芸能ゴシップ記事など)
- UNEXTアフィリエイトやNordアフィリエイトなどお金をもらってランキング上げているサイト
- avast LINE opera Gmail とかをおすすめソフト 紹介している見る価値のない記事(自社の有料ソフトを紹介、もしくはステマ込み)※条件厳しめに
- LINE タウンWifi Lemon08 Tiktok とかを神アプリと紹介している明らかにアフィリエイト系の記事
- DMMの紹介文と画像コピペしてアフィリンク挿入しただけの記事
- 詐欺サイト(詐欺ショッピングサイトなど)
- 一部ランキングサイト(mybestなど)
- 偽サイト(偽revanced、偽Githubリポジトリ、偽Z-Libなど)
- 一部SNS(Tiktok Instagram はてなブックマーク pinterest等)
- 技術系スパムサイト(間違った情報) ※条件厳しめ
- 危険なソフトウェアダウンロードサイト(igggamesなどマルウェア配布サイト)

> [!NOTE]
>まとめサイトは評価が人によって分かれるのと、数が多いので含めていません。しかし、◯的ゲーム速報、は◯ま寄稿、や◯おん、稲妻◯報などのサイトはwikiに迷惑サイトとあることやtwitterでの評判が悪い上に、捏造や誹謗中傷が多く、誰の目から見ても不要なので特例でリストインしています。


# 効果をテスト

[検索](https://www.google.com/search?q=%E5%85%AC%E5%BC%8F+site%3Aonline+OR+site%3Acn+OR+site%3Ashop+OR+site%3Atop+OR+site%3Asite+OR+site%3Aapp+OR+site%3Acfd+OR+site%3Axyz+OR+site%3Ame+OR+site%3Ame+OR+site%3Aru+OR+site%3Auk+OR+site%3Apl+OR+site%3Aonline+OR+site%3Ashop&sca_upv=1#ip=1)


# 貢献

URLの追加やミスの削除に協力していだける方は、レポジトリをForkして編集していただき、pull requestを送ってください。
issueでも構いませんが、可能ならpull requestのほうが嬉しいです。
このフィルターと別のフィルターをコードエディターなどにコピーし
ファイル名をuBlacklist.txtにし、pyファイルを使うと、アルファベット順に並べられ重複を削除できますが、Pull Requestするときは必ずしも必要ではありません。（勿論しても良いです。）

# 補足
Kiwi browserでDuckDuckGo、SearXNGが使えない問題を修正
[uBlacklist for Kiwi (mod)](https://github.com/Kdroidwin/ublacklist)
