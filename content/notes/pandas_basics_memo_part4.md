Title: pands basics memo part4
Date: 2021-09-01 00:00
Modified: 2021-09-01 00:00
Category: note
Tags: note
Slug: pands-basics-memo-pt4
Authors: sonkmr
Summary: 東京都が出してるコロナのデータを扱って覚えたpandasの基本的な使い方たちを忘れたくないのでメモしてみた part4
Status: draft

## pandasの基本的な使い方たちを忘れないようにメモしてみる part4
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


### 列の並び順を変えたい
`DataFrame.reindex()`を使うと並び順を変えられる  

``` python
>>> # 列を並び替える(data列を末尾に移す)
>>> data.reindex(columns=['date', "id", 'count', 'xyz', 'count_xyz', 'data'])
        date  id  count  xyz  count_xyz     data
0 2021-04-01   1      3    2          5    data1
1 2021-04-02   2      6    3          9    data2
2 2021-04-03   3      9    4         13    data3
3 2021-04-04   4     12    5         17    data4
4 2021-04-05   5     15    6         21    data5
5 2021-04-06   6     18    7         25    data6
6 2021-04-07   7     21    8         29    data7
7 2021-04-08   8     24    9         33    data8
8 2021-04-09   9     27   10         37    data9
9 2021-04-10  10     30   11         41   data10
```

### reindex()で列を削除することもできる
`reindex()`のcolumns引数から要らない列名を取り除くとその列は削除される

``` python
>>> # reindexで列を取り除くこともできる(data列を取り除く)
>>> data.reindex(columns=['date', "id", 'count', 'xyz', 'count_xyz'])
        date  id  count  xyz  count_xyz
0 2021-04-01   1      3    2          5
1 2021-04-02   2      6    3          9
2 2021-04-03   3      9    4         13
3 2021-04-04   4     12    5         17
4 2021-04-05   5     15    6         21
5 2021-04-06   6     18    7         25
6 2021-04-07   7     21    8         29
7 2021-04-08   8     24    9         33
8 2021-04-09   9     27   10         37
9 2021-04-10  10     30   11         41
```


### 行と列を入れ替えたい

`DataFrame.T`で行と列を入れ替えたDataframeが得られる  

小さいcsvでデータを作ってみる

``` python
>>> import io
>>> import pandas as pd
>>>
>>> csv = '''date,id,data,count,xyz
... 2021-04-01, 1, data1, 1, 2
... 2021-04-02, 2, data2, 2, 3
... 2021-04-03, 3, data3, 3, 4
... '''
>>>
>>> data = pd.read_csv(io.StringIO(csv), parse_dates = ['date', ], low_memory=False)
>>> data
        date  id    data  count  xyz
0 2021-04-01   1   data1      1    2
1 2021-04-02   2   data2      2    3
2 2021-04-03   3   data3      3    4
>>> data.T
                         0                    1                    2
date   2021-04-01 00:00:00  2021-04-02 00:00:00  2021-04-03 00:00:00
id                       1                    2                    3
data                 data1                data2                data3
count                    1                    2                    3
xyz                      2                    3                    4
```

