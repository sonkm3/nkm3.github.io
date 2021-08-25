Title: calculate positive count and rate by ward
Date: 2021-08-15 01:00:00
Modified: 2021-08-25 01:00:00
Category: note
Tags: note, software
Slug: calculate-positive-count-and-rate-by-ward
Authors: sonkmr
Summary: 23区ごとの陽性者数と人口割合を可視化してみた
Status: published

## 23区ごとの陽性者数と人口割合を可視化してみた
前回のプログラム合わせて書いてみたプログラムです  

区ごとの陽性者数のデータはあるけど人口多い区は人数多くなるので割り合いを計算してみたのがこちら  
割合で見てもやっぱり人が多い区の方が割り合いが高い雰囲気だけどそもそも計算があってるのかな  

### 迷ったところ

- ピボットをcrosstabで書き換えた箇所
    - pivot_tableよりcrosstabの方が引数が明確でわかりやすい
    - ピボットさせるだけで再集計は発生しないのでaggfuncが`lambda x: x`でいける
```
daily_count = pd.crosstab(data['公表_年月日'], data['市区町村名'], data['陽性者数'], aggfunc=lambda x: x, dropna=False, margins=False)
```

- このcsvの陽性者数は積み上がった総数なのでピボットしてから差分を取る必要があった
```
daily_diff = daily_count.diff()
```

- divを使って各行政区ごとの人口で割る処理
    - divの第一引数はリストも渡せる
```
daily_diff_rate = daily_diff.div(population_dict.values(), axis='columns').mul(100)
```

- 区の数の多さや、規模の差が大きいなど、わかりにくいグラフになったので箱ひげ図でイメージを掴めるようにした
    - 人口の少ない町村で突出した値が出てしまう
    - 突出した値は箱ひげ図でも見分けがつくので傾向は分かりそう

- boxplotは値を返すので余計な出力が出てしまう
    - 一時変数に代入して解消
```
_ = ax1.boxplot(plot_df, vert=True, labels=plot_df.columns)
```

### リンク
- 東京都福祉保健局のオープンデータ[陽性者数（区市町村別）](https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0cro000000085)
- 東京都の統計[住民基本台帳による東京都の世帯と人口（町丁別・年齢別）](https://www.toukei.metro.tokyo.lg.jp/juukiy/2021/jy21000001.htm)

### notebook
github [tokyo_covid19_daily_positive_count_and_rate_graph_by_ward.ipynb](https://github.com/sonkm3/sonkm3.github.io/blob/main/content/ipynb/tokyo_covid19/tokyo_covid19_daily_positive_rate_graph_by_ward.ipynb)

{% notebook ipynb/tokyo_covid19/tokyo_covid19_daily_positive_rate_graph_by_ward.ipynb %}
