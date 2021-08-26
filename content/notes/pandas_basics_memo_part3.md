Title: pands basics memo part3
Date: 2021-09-01 00:00
Modified: 2021-09-01 00:00
Category: note
Tags: note
Slug: pands-basics-memo-pt3
Authors: sonkmr
Summary: 東京都が出してるコロナのデータを扱って覚えたpandasの基本的な使い方たちを忘れたくないのでメモしてみた part3
Status: draft

## pandasの基本的な使い方たちを忘れないようにメモしてみる part3
データのフィルタ、検索について

### まずデータを読み込む  
実際はファイルを読み込んでいるけれどここでは文字列から読み込んでいる  
ファイルから読み込む場合は`pd.read_csv(filepath, 他の引数)`でいける  
``` python
$ python
Python 3.8.11 (default, Jul  3 2021, 08:42:01)
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import io
>>> import pandas as pd
>>>
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
...
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


### 条件ひとつ

`data[data['count'] > 5]`でcount列が5より大きい行が得られる

``` python
>>> data[data['count'] > 5]
        date  id     data  count  xyz
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```

### 日付のカラムに対して  
`data[data['date'] > '2021-04-05']`とするとdate列が`2021/4/5`よりあとの日付の行が得られる

``` python
>>> # date列でフィルタする
>>> data[data['date'] > '2021-04-05']
        date  id     data  count  xyz
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```

###　複数の条件

``` python
>>> data[(data['count'] > 5) & (data['xyz'] > 5)]
        date  id     data  count  xyz
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```


### 代わりにquery()を使ってみる

``` python
>>> data.query('count > 5 | xyz > 5')
        date  id     data  count  xyz
4 2021-04-05   5    data5      5    6
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```


### query()の第一引数は文字列なのでフィルタ条件を生成することができる

``` python
>>> condition = '> 5'
>>> column_name_list = ['count', 'xyz']
>>> query = '|'.join([f'{key} {condition}' for key in column_name_list])
>>> data.query(query)
        date  id     data  count  xyz
4 2021-04-05   5    data5      5    6
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```


