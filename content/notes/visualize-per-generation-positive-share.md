Title: visualize per generation positive share
Date: 2021-08-17 00:00:00
Category: note
Tags: note, software
Slug: visualize-per-generation-positive-share
Authors: sonkmr
Summary: 陽性者の年代別シェアを可視化してみた

## 陽性者の年代別シェアを可視化してみた
今回はやろうと思っていたけどやり方がわからず詰まっていたプログラムです

年代ごとの陽性者数のデータはあるけど日毎の偏りはわかりにくいので計算して画像かしてみたのがこちら  
「若者の感染が増えてます」みたいな煽りを見た気がするけど2月から4月が比較的少なく、シェアで見ると全体的に20代、30代が占めている割合は多いように見える  
毎回のように不安になるけど、、、計算あってるのか！？  

### 迷ったところ
全ての行の指定した列に対して割合を計算する方法
```
cross_df.update(cross_df.loc[:, '10歳未満': '-'].div(cross_df["All"], axis=0))
```
`10歳未満`から`-`の各セルを行のAll列の値(小計)で割っている  
一行ずつループで回したりしなくてよくて楽ちん(ましてExcelで同じことをすると思うと)  

あとDataFrameのカラムの並び順の変え方がわからなかったけど  
```
cross_df = cross_df.reindex(columns=['10歳未満', '10代', '20代', '30代', '40代', '50代', '60代', '70代','80代', '90代', '100歳以上', '-', 'All'])
```
のDataframe.reindex()でできた  

### リンク

- 東京都福祉保健局のオープンデータ[東京都 新型コロナウイルス陽性患者発表詳細](https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068)

### notebook

- github [tokyo_covid19_effective_reproduction_number.ipynb](https://github.com/sonkm3/sonkm3.github.io/blob/main/content/ipynb/tokyo_covid19_per_generation_daily_graph.ipynb)

{% notebook ipynb/tokyo_covid19_per_generation_daily_graph.ipynb %}
