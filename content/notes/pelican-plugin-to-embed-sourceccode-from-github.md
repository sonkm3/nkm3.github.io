Title: pelican plugin to embed sourcecode from github
Date: 2021-08-21 00:00
Modified: 2021-08-21 00:00
Category: note
Tags: note, software
Slug: pelican-plugin-to-embed-sourceccode-from-github
Authors: sonkmr
Summary: pelicanのページにgithubのソースコードを埋め込めるようにしてみた

## pelicanのページにgithubのソースコードを埋め込めるようにしてみた  

ソースコードの埋め込み表示にはEmbed Like Gistを使って、jsへ値を渡すためのMarkdownエクステンションをmdx_embedlyを元にして書いた感じ  

### さっそく埋め込んでみる
埋め込みたいところで[https://github.com/{user}/{repo}/blob/main/{path-to-file}:embed-github]と書くと以下のようにソースコードが埋め込まれる  
実際のエクステンションのソースも動作もこれだけ、というかそれだけ、という感じ

[https://github.com/sonkm3/sonkm3.github.io/blob/main/plugins/embed_github.py:embed-github]

### 行番号で範囲指定もできる  
例えばこんな感じに書くと [\https://github.com/sonkm3/sonkm3.github.io/blob/main/plugins/embed_github.py#L8-L11:embed-github] 下のように表示される(`\`は消してねおねがい)

[https://github.com/sonkm3/sonkm3.github.io/blob/main/plugins/embed_github.py#L8-L11:embed-github]


### おまけ:MarkdownモジュールはEmbedGithubExtensionを自動で使えるようにしてくれない
`pelican.conf`の`MARKDOWN`に`'plugins.embed_github:EmbedGithubExtension': {},`のように追加すると使えるようになる  
例えばこんな感じ  
以前の`Pelican`と書き方が変わったのかな？使っているのは`Pelican 4.6`です  

```
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'plugins.embed_github:EmbedGithubExtension': {},
    },
    'output_format': 'html5',
}
```


### おまけ:Markdownエクステンションの動作確認
Markdownのエクステンションを書く時はPelicanからではなくmarkdownモジュールを直接使うと動作の確認がしやすかった  
以下が確認で使ったReplのログ  
ここのURLの箇所も展開されてしまうのでembed-githubのところはembed-github-dummyに置き換えている  

``` python
$ python
Python 3.8.11 (default, Jul  3 2021, 08:42:01) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import markdown
>>> source = '[https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/app/serializers.py#L6-L16:embed-github-dummy]'
>>> html = markdown.markdown(source, extensions=['plugins.embed_github'])
>>> html
'<p>\n<script src="https://emgithub.com/embed.js?target=%5Bhttps%3A//github.com/sonkm3/wordbook/blob/main/wordbook-backend/app/serializers.py%23L6-L16%3Aembed-github%5D&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>\n</p>'
>>> ^D
```

### リンク

- Embed Like Gist [https://emgithub.com](https://emgithub.com)
- Embedly Extension for Python-Markdown(mdx_embedly) [https://github.com/yymm/mdx_embedly](https://github.com/yymm/mdx_embedly)
