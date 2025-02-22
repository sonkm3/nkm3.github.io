Title: calculate effective reproduction number
Date: 2021-08-15 00:00:00
Category: note
Tags: note, software
Slug: calculate-effective-reproduction-number
Authors: sonkmr
Summary: 東京都の実行再生算数を簡易計算してみた

## 東京都の実行再生算数を簡易計算してみた
今回もふと思い立って書いてみたプログラムです  

国立感染症研究所のサイトに簡易的な実行再生算数の計算方法が載っていたので公開されている東京都のデータと合わせて[Jupyter Notebook](https://jupyter.org)と[pandas](https://pandas.pydata.org)の練習がてら手元で計算してみました  

###　迷ったところ
```
daily['ern'] = daily['count'].rolling(window='19D').apply(calc_ern)
```  

19日単位のウインドウで実行再生算数を計算している  
「できるはずだけどこの世界の言葉でどう呼ばれているのかがわからない」で手間取った  

### リンク
- 簡易的な実行再生算数の計算方法[COVID-19感染報告者数に基づく簡易実効再生産数推定方法](https://www.niid.go.jp/niid/ja/diseases/ka/corona-virus/2019-ncov/2502-idsc/iasr-in/10465-496d04.html)  
- 東京都福祉保健局のオープンデータ[東京都 新型コロナウイルス陽性患者発表詳細](https://catalog.data.metro.tokyo.lg.jp/dataset/t000010d0000000068)

### notebook
- github [tokyo_covid19_effective_reproduction_number.ipynb](https://github.com/sonkm3/sonkm3.github.io/blob/main/content/ipynb/tokyo_covid19_effective_reproduction_number.ipynb)


{% notebook ipynb/tokyo_covid19/tokyo_covid19_effective_reproduction_number.ipynb %}
