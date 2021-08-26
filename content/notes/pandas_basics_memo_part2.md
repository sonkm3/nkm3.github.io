Title: pands basics memo part2
Date: 2021-09-01 00:00
Modified: 2021-09-01 00:00
Category: note
Tags: note
Slug: pands-basics-memo-pt2
Authors: sonkmr
Summary: 東京都が出してるコロナのデータを扱って覚えたpandasの基本的な使い方たちを忘れたくないのでメモしてみた part2
Status: draft

## pandasの基本的な使い方たちを忘れないようにメモしてみる part2
データへの計算の方法について

### まずデータを読み込む  
 
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

### フィルタしてみる  
`data[data['date'] > '2021-04-05']`とするとdate列が`2021/4/5`より大きい、あとの列のみのDataFrameが返ってくる
```
>>> # date列でフィルタする
>>> data[data['date'] > '2021-04-05']
        date  id     data  count  xyz
5 2021-04-06   6    data6      6    7
6 2021-04-07   7    data7      7    8
7 2021-04-08   8    data8      8    9
8 2021-04-09   9    data9      9   10
9 2021-04-10  10   data10     10   11
```

### DataFrameに対しての計算
`data['count'] + 3`とするとcount列のすべての値に3を足した結果がSeriesで返ってくる

``` python
>>> # count列の値すべてを+3した結果を受け取る
>>> data['count'] + 3
0     4
1     5
2     6
3     7
4     8
5     9
6    10
7    11
8    12
9    13
Name: count, dtype: int64
```

### 計算結果をDataFrameに保存する
`data['count_minus_1'] = data['count'] - 1`とするとcount列全体を−1したSeriesを作ってその結果をdata['count_minus_1']列に代入する  
その結果、data DataFrameには新しいcount_minus_1列ができ、count列から1を引いた値が保存されている
``` python
>>> # count列の値すべてを-1した結果を新しい列にする
>>> data['count_minus_1'] = data['count'] - 1
>>> data
        date  id     data  count  xyz  count_minus_1
0 2021-04-01   1    data1      1    2              0
1 2021-04-02   2    data2      2    3              1
2 2021-04-03   3    data3      3    4              2
3 2021-04-04   4    data4      4    5              3
4 2021-04-05   5    data5      5    6              4
5 2021-04-06   6    data6      6    7              5
6 2021-04-07   7    data7      7    8              6
7 2021-04-08   8    data8      8    9              7
8 2021-04-09   9    data9      9   10              8
9 2021-04-10  10   data10     10   11              9
```

### DataFrameから列(など)を削除する
count_minus_1列はもういらないので`data = data.drop('count_minus_1', axis='columns')`として列を削除する  
axis引数は多くのDataFrameのメソッドに有る引数で、indexもしくはcolumnsが指定できる(メソッドごとによく使われる方向がデフォルト指定されているので指定しないでもなんとなく動くほか、0/1でも指定できる)  
指定した処理をそれぞれ行方向(横)、列方向(縦)のどちらに対して実行するかを指定できる  
``` python
>>> # count_minus_1列を削除する
>>> data = data.drop('count_minus_1', axis='columns')
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

### 既存の列を新たな値で更新する場合はDataFrame.update()が使える  
ここまでの通り`data['count'] * 3`はSeriesを返すので`data.update(data['count'] * 3)`はcount列を返ってきたSeriesで更新する形になる  
``` python
>>> # count列の値すべてを3倍してcount列を上書きする
>>> data.update(data['count'] * 3)
>>> data
        date  id     data  count  xyz
0 2021-04-01   1    data1      3    2
1 2021-04-02   2    data2      6    3
2 2021-04-03   3    data3      9    4
3 2021-04-04   4    data4     12    5
4 2021-04-05   5    data5     15    6
5 2021-04-06   6    data6     18    7
6 2021-04-07   7    data7     21    8
7 2021-04-08   8    data8     24    9
8 2021-04-09   9    data9     27   10
9 2021-04-10  10   data10     30   11
```

### 違う列の値同士を計算してその結果を新しい列に保存したい場合  
例えば足し算や掛け算はこのようにできる  

- `data['count_xyz'] = data['count'].add(data['xyz'], axis=0)`
- `data['count_xyz'] = data['count'].mul(data['xyz'], axis=0)`

少し込み入った計算やpandasのDataFrameで提供されていない関数で処理をしたい場合はapplyが使える  

- `data['count_xyz'] = data['count'].apply(math.sqrt)`

定義された関数を使う他に、lambdaで定義した関数を使うこともできる

- `data.loc[:, 'count':'xyz'].apply(lambda x: x[0] + x[1], axis='columns' )`


``` python
>>> # count列とxyz列を行ごとに足し合わせてcount_xyz列を作る
>>> data['count_xyz'] = data['count'].add(data['xyz'], axis=0)
>>> data
        date  id     data  count  xyz  count_xyz
0 2021-04-01   1    data1      3    2          5
1 2021-04-02   2    data2      6    3          9
2 2021-04-03   3    data3      9    4         13
3 2021-04-04   4    data4     12    5         17
4 2021-04-05   5    data5     15    6         21
5 2021-04-06   6    data6     18    7         25
6 2021-04-07   7    data7     21    8         29
7 2021-04-08   8    data8     24    9         33
8 2021-04-09   9    data9     27   10         37
9 2021-04-10  10   data10     30   11         41
```
