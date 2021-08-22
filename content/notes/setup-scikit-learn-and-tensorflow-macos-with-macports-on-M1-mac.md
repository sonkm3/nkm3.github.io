Title: setup scikit-learn and tensorflow-macos with macports
Date: 2021-09-22 00:00
Modified: 2021-09-22 00:00
Category: note
Tags: note, software
Slug: setup_scikit-learn_and_tensorflow-macos_with_macports
Authors: sonkmr
Summary: macports上のPython virtualenvにpip installしづらいscikit-learnやtensorflow-macosをインストールする流れ

## macports上のPython virtualenvにpip installしづらいscikit-learnやtensorflow-macosをインストールする流れ

### scikit-learn
依存するライブラリとfortranをインストールする必要がある  

```
port install OpenBLAS boost171 gcc11 +gfortran
```

fortranコンパイラ`port search fortran`で出てくるg95かなー？と思ったけどインストールできないしメンテもされていなくて詰んだかと思ったけど`port install gcc11 +gfortran`でいける  
あとはpipでインストールする  

```
pip install scikit-learn
```

### tensorflow-macos
依存するライブラリ、ソフトウェアは以下のもの

```
ports install pkgconfig clang-9.0 hdf5
```

pipでPythonモジュールをインストールする際にいくつか環境変数を設定する必要がある

grpcioのインストール

```
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=1
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=1
export LDFLAGS="-L/opt/local/lib"	
export CPPFLAGS="-I/opt/local/include"
pip install grpcio
```

h5pyのインストール
```
export HDF5_DIR=/opt/local
pip install h5py
```

これで`tensorflow-macos`のインストールができるようになる

```
pip install tensorflow-macos
```

実際に使ってみると`ValueError: numpy.ndarray size changed, may indicate binary incompatibility. Expected 88 from C header, got 80 from PyObject`みたいなエラーが出てしまう  
これは`numpy`のバージョンを上げたら解消できる  

`tensorflow-macos`が依存するバージョンの指定は以下の方法で無視して新しいバージョンの`numpy`をインストールできる
```
pip install --no-deps numpy
```

そして`tensorflow-metal`をインストールする

```
pip install tensorflow-metal
```

これで`tensorflow-macos`が使えるようになる

``` python
$ python
Python 3.8.11 (default, Jul  3 2021, 08:42:01) 
[Clang 12.0.5 (clang-1205.0.22.9)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from tensorflow.python.client import device_lib
Init Plugin
Init Graph Optimizer
Init Kernel
>>> device_lib.list_local_devices()
Metal device set to: Apple M1

systemMemory: 16.00 GB
maxCacheSize: 5.33 GB

2021-08-21 10:32:12.586804: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:305] Could not identify NUMA node of platform GPU ID 0, defaulting to 0. Your kernel may not have been built with NUMA support.
2021-08-21 10:32:12.587071: I tensorflow/core/common_runtime/pluggable_device/pluggable_device_factory.cc:271] Created TensorFlow device (/device:GPU:0 with 0 MB memory) -> physical PluggableDevice (device: 0, name: METAL, pci bus id: <undefined>)
[name: "/device:CPU:0"
device_type: "CPU"
memory_limit: 268435456
locality {
}
incarnation: 6684442442338290487
, name: "/device:GPU:0"
device_type: "GPU"
locality {
  bus_id: 1
}
incarnation: 14382550646620981992
physical_device_desc: "device: 0, name: METAL, pci bus id: <undefined>"
]
>>> 
```


