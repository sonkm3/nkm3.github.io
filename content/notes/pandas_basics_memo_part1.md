Title: pands basics memo part1
Date: 2021-09-01 00:00
Modified: 2021-09-01 00:00
Category: note
Tags: note
Slug: pands-basics-memo-pt1
Authors: sonkmr
Summary: 東京都が出してるコロナのデータを扱ってみて覚えたpandasの基本的な使い方たちを忘れたくないのでメモしてみた part1
Status: draft

## pandasの基本的な使い方たちを忘れないようにメモしてみる part1
csvデータの読み込み方法など

### csvデータを読み込む  

#### ローカルファイル

pandasのread_csvメソッドで読み込める  
今のところ日付として取り扱うカラムを指定するparse_datesの指定のみでうまく読み込めている  

``` python
import pandas as pd
data = pd.read_csv('data/130001_tokyo_covid19_patients.csv', parse_dates = ['公表_年月日', '発症_年月日', '確定_年月日'], low_memory=False)
```

#### httpで取得する

requestsでファイルを取得してStringIO経由でread_csvに渡している  
CacheControlを使うとリクエストデータをキャッシュすることができる(この例では.webcacheディレクトリにキャッシュが保存される)  

``` python
import io

import requests
from cachecontrol import CacheControl 
from cachecontrol.caches import FileCache

cached_session = CacheControl(requests.Session(), cache=FileCache('.webcache'))
response = cached_session.get('https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv', low_memory=False) 
data = pd.read_csv(io.StringIO(response.text), parse_dates = ['公表_年月日', '発症_年月日', '確定_年月日'])
```

#### 文字列を渡す

例として使うぐらいであまり使うことはなさそうだけれど一応できることはできる  

```
import io
import pandas as pd
csv = '''date,id,data,count,xyz
2021-04-01, 1, data1, 1, 2
2021-04-02, 2, data2, 2, 3
2021-04-03, 3, data3, 3, 4
2021-04-04, 4, data4, 4, 5
2021-04-05, 5, data5, 5, 6
2021-04-06, 6, data6, 6, 7
2021-04-07, 7, data7, 7, 8
2021-04-08, 8, data8, 8, 9
2021-04-09, 9, data9, 9, 10
2021-04-10, 10, data10, 10, 11
'''

data = pd.read_csv(io.StringIO(csv), parse_dates = ['date', ], low_memory=False)
```


