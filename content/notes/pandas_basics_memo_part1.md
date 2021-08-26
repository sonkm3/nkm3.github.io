Title: pands basics memo part1
Date: 2021-09-01 00:00
Modified: 2021-09-01 00:00
Category: note
Tags: note
Slug: pands-basics-memo-pt1
Authors: sonkmr
Summary: 東京都が出してるコロナのデータを扱ってみて覚えたpandasの基本的な使い方たちを忘れたくないのでメモしてみた part1

## pandasの基本的な使い方たちを忘れないようにメモしてみる part1
csvデータの読み込み方法など

### csvデータを読み込む  

#### ローカルファイル

pandasのread_csvメソッドで読み込める  
今のところ日付として取り扱うカラムを指定するparse_datesの指定のみでうまく読み込めている  

``` python
>>> import pandas as pd
>>> data = pd.read_csv('data/130001_tokyo_covid19_patients.csv', parse_dates = ['公表_年月日', '発症_年月日', '確定_年月日'], low_memory=False)
>>> data
            No  全国地方公共団体コード 都道府県名  市区町村名     公表_年月日     発症_年月日     確定_年月日  ... 患者_職業 患者_状態 患者_症状 患者_渡航歴の有無フラグ  患者_接触歴の有無フラグ  備考  退院済フラグ
0            1       130001   東京都    NaN 2020-01-24        NaT        NaT  ...   NaN   NaN   NaN          NaN           NaN NaN     1.0
1            2       130001   東京都    NaN 2020-01-25        NaT        NaT  ...   NaN   NaN   NaN          NaN           NaN NaN     1.0
2            3       130001   東京都    NaN 2020-01-30        NaT        NaT  ...   NaN   NaN   NaN          NaN           NaN NaN     1.0
3            4       130001   東京都    NaN 2020-02-13        NaT        NaT  ...   NaN   NaN   NaN          NaN           NaN NaN     1.0
4            5       130001   東京都    NaN 2020-02-14        NaT        NaT  ...   NaN   NaN   NaN          NaN           NaN NaN     1.0
...        ...          ...   ...    ...        ...        ...        ...  ...   ...   ...   ...          ...           ...  ..     ...
202302  201419       130001   東京都    NaN 2021-07-27 2021-07-24 2021-07-26  ...   会社員   NaN   NaN          NaN           1.0 NaN     1.0
202303  201420       130001   東京都    NaN 2021-07-27 2021-07-23 2021-07-26  ...     －   NaN   NaN          NaN           NaN NaN     1.0
202304  201421       130001   東京都    NaN 2021-07-27 2021-07-22 2021-07-26  ...     －   NaN   NaN          NaN           1.0 NaN     1.0
202305  201422       130001   東京都    NaN 2021-07-27 2021-07-17 2021-07-26  ...     －   NaN   NaN          NaN           NaN NaN     NaN
202306  201423       130001   東京都    NaN 2021-07-27 2021-07-24 2021-07-26  ...   会社員   NaN   NaN          NaN           NaN NaN     NaN

[202307 rows x 17 columns]
```

#### httpで取得する

requestsでファイルを取得してStringIO経由でread_csvに渡している  
CacheControlを使うとリクエストデータをキャッシュすることができる(この例では.webcacheディレクトリにキャッシュが保存される)  

``` python
>>> import io
>>>
>>> import pandas as pd
>>> import requests
>>> from cachecontrol import CacheControl
>>> from cachecontrol.caches import FileCache
>>>
>>> cached_session = CacheControl(requests.Session(), cache=FileCache('.webcache'))
>>> response = cached_session.get('https://stopcovid19.metro.tokyo.lg.jp/data/130001_tokyo_covid19_patients.csv')
>>> data = pd.read_csv(io.StringIO(response.text), parse_dates = ['公表_年月日', '発症_年月日', '確定_年月日'], low_memory=False)
>>> data
            No  全国地方公共団体コード 都道府県名  市区町村名     公表_年月日 発症_年月日 確定_年月日  患者_居住地  ... 患者_性別 患者_職業 患者_状態  患者_症状  患者_渡航歴の有無フラグ  患者_接触歴の有無フラグ  備考  退院済フラグ
0            1       130001   東京都    NaN 2020-01-24    NaT    NaT  湖北省武漢市  ...    男性   NaN   NaN    NaN           NaN           NaN NaN     1.0
1            2       130001   東京都    NaN 2020-01-25    NaT    NaT  湖北省武漢市  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     1.0
2            3       130001   東京都    NaN 2020-01-30    NaT    NaT  湖南省長沙市  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     1.0
3            4       130001   東京都    NaN 2020-02-13    NaT    NaT      都内  ...    男性   NaN   NaN    NaN           NaN           NaN NaN     1.0
4            5       130001   東京都    NaN 2020-02-14    NaT    NaT      都内  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     1.0
...        ...          ...   ...    ...        ...    ...    ...     ...  ...   ...   ...   ...    ...           ...           ...  ..     ...
323152  322269       130001   東京都    NaN 2021-08-25    NaT    NaT     NaN  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     NaN
323153  322270       130001   東京都    NaN 2021-08-25    NaT    NaT     NaN  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     NaN
323154  322271       130001   東京都    NaN 2021-08-25    NaT    NaT     NaN  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     NaN
323155  322272       130001   東京都    NaN 2021-08-25    NaT    NaT     NaN  ...    男性   NaN   NaN    NaN           NaN           NaN NaN     NaN
323156  322273       130001   東京都    NaN 2021-08-25    NaT    NaT     NaN  ...    女性   NaN   NaN    NaN           NaN           NaN NaN     NaN

[323157 rows x 17 columns]
```

#### 文字列を渡す

例として使うぐらいであまり使うことはなさそうだけれどできる  

```
>>> import io
>>> import pandas as pd
>>> csv = '''date,id,data,count,xyz
... 2021-04-01, 1, data1, 1, 2
... 2021-04-02, 2, data2, 2, 3
... 2021-04-03, 3, data3, 3, 4
... 2021-04-04, 4, data4, 4, 5
... 2021-04-05, 5, data5, 5, 6
... 2021-04-06, 6, data6, 6, 7
... 2021-04-07, 7, data7, 7, 8
... 2021-04-08, 8, data8, 8, 9
... 2021-04-09, 9, data9, 9, 10
... 2021-04-10, 10, data10, 10, 11
... '''
>>>
>>> data = pd.read_csv(io.StringIO(csv), parse_dates = ['date', ], low_memory=False)
>>> data
        date  id     data  count  xyz
0 2021-04-01   1    data1      1    2
1 2021-04-02   2    data2      2    3
2 2021-04-03   3    data3      3    4
3 2021-04-04   4    data4      4    5
4 2021-04-05   5    data5      5    6
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```


