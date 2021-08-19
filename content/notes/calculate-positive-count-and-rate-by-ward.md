Title: calculate positive count and rate by ward
Date: 2021-08-15 01:00:00
Category: note
Tags: note, software
Slug: calculate-positive-count-and-rate-by-ward
Authors: sonkmr
Summary: 23区ごとの陽性者数と人口割合を可視化してみた

## 23区ごとの陽性者数と人口割合を可視化してみた
前回のプログラム合わせて書いてみたプログラムです  

区ごとの陽性者数のデータはあるけど人口多い区は人数多くなるので割り合いを計算してみたのがこちら  
割合で見てもやっぱり人が多い区の方が割り合いが高い雰囲気だけどそもそも計算があってるのかな  

### 迷ったところ
pandasのpivot_tableとdf.applyの使い方  
前回と同じく「できるはずだけどこの世界の言葉でどう呼ばれているのかがわからない」で手間取った  

### リンク
- 東京都福祉保健局のオープンデータ[陽性者数（区市町村別）](https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000085)
- 東京都の統計[住民基本台帳による東京都の世帯と人口（町丁別・年齢別）] https://www.toukei.metro.tokyo.lg.jp/juukiy/2021/jy21000001.htm

### notebook
github [tokyo_covid19_daily_positive_count_and_rate_graph_by_ward.ipynb](https://github.com/sonkm3/sonkm3.github.io/blob/main/content/ipynb/tokyo_covid19_daily_positive_count_and_rate_graph_by_ward.ipynb)

{% notebook ipynb/tokyo_covid19_daily_positive_count_and_rate_graph_by_ward.ipynb %}
