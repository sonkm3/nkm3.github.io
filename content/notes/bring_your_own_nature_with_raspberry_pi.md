Title: Raspberry Piで自然を手元に持ってくる方法の紹介
Date: 2021-10-04 00:00
Modified: 2021-10-04 00:00
Category: note
Tags: note
Slug: bring_your_own_nature_with_raspberry_pi
Authors: sonkmr
Summary: Raspberry Piを使った自然の雰囲気を都会にいても楽しめる仕組みの紹介と作り方について

# Raspberry Piで自然を手元に持ってくる方法の紹介
![Screen Shot 2021-09-26 at 9.05.02.png]({static}/images/Screen Shot 2021-09-26 at 9.05.02.png)
映像と音声で都会にいても自然環境を楽しめる仕組みをRaspberry Piとオープンソースのソフトを使って作りました  
朝から昼の間の鳥のさえずりから夕方から夜にかけての虫の音まで一日中自然の音を聞くことができて都会での居心地が少しよくなりました  
自然を手元に、とか言っていますがやっていることはライブ配信サイトとおなじことです  
実は使い慣れた？オープンソースのソフトウェアを組み合わせれば、自分用のライブ配信サイトを作ることができるのでざっくり紹介してみます  

# 仕組み
![Screen Shot 2021-09-26 at 9.05.02.png]({static}/images/bring_your_own_nature_with_raspberry_pi.001.png)

映像配信の方法はいくつかありますが、今回はHLSという方式を使ってみました  
HLSは連続する映像、音声を短い映像、音声ファイルに分割(フラグメント)し、そのリスト(プレイリスト)と合わせて扱いやすいHTTPで配信する方式です  
ブラウザーはプレイリストをダウンロードしてから分割されたファイルを逐一ダウンロードする形になるため、遅延がフラグメントの長さより長い時間幅で発生します  
配信を見ながらコメントをしたりするサービスの場合は遅延を減らすよう、他の方式も含めて検討すると思いますが、今回は「ただ雰囲気を楽しむ」だけなのであまり追求していません

## Raspberry Piとクラウドの役割分担

- Raspberry Pi(FFmpeg)
    - Webカメラから映像と音声をRTMPプロトコルに乗せます
- クラウド上の配信サーバー(nginx-rtmp-module)
    - RTMPプロトコルで送られて来たストリームを分割します
    - 分割したファイルを並べたプレイリストを更新します
    - プレイリストと分割したファイルをHTTPで公開します
    - APIサーバー(bottlepy)
        - Raspberry Piからの配信開始、終了時にslack通知します
        - Raspberry Piからの配信状態を表示します
- ブラウザー(hls.js)

## 使ったソフトウェア、サービスなど

### 撮影部分
- Webカメラ
    - Logicool C922n
- Raspberry Pi
    - Raspberry Pi 3 Model A+
- [FFmpeg](https://ffmpeg.org)

### 配信部分
- [nginx-rtmp-module](https://github.com/arut/nginx-rtmp-module/)
- [nginx-unit](https://unit.nginx.org)
- [bottlepy](https://bottlepy.org/docs/dev/)

### 表示部分
- [hls.js](https://github.com/video-dev/hls.js/)

# ポイント
## FFmpegの実行
```
ffmpeg \
  -y \
  -f alsa -ac $CHANNELS -thread_queue_size 16384 -r 15 -re -t $DURATION -i $AUDIO_DEVICE\
  -f v4l2 -thread_queue_size 16384 -s 640x360 -r 15 -t $DURATION -i $VIDEO_DEVICE \
  -c:a aac -b:a 128k -ar $SAMPLING_RATE -bufsize 128k \
  -c:v h264_omx -b:v 500k -bufsize 500k -vsync cfr -g 300 -profile:v:1 main\
  -bsf:v h264_mp4toannexb \
  -flags +cgop+loop+global_header \
  -ignore_unknown \
  -f flv $RTMP_SERVER_URL
```
Raspberry Pi上で動作し、webカメラからの映像を配信サーバー(`$RTMP_SERVER_URL`)に送信するコマンドです(実際は`systemd`から実行されるシェルスクリプトの中で実行しています)  

ちょうど良い設定がなかなかたどりつけなかったのですが、いまとのころこのコマンドラインオプションで良さそうな感じがしています  
設置場所のwifi事情があまり良くないことや、ネットワークの利用量を抑えるため、動画のビットレートを比較的低くできるように設定しています  

`-c:v h264_omx` で`Raspberry Pi`が持っているハードウェアのh264エンコーダーを使用するようにしています  
今回は`Raspberry Pi 3 Model A+`を使っていますが、ハードウェアエンコーダーを使っているため`Raspberry Pi Zero WH`などでも比較的低い負荷でエンコードがおこなえると思います  

## nginx-rtmp-moduleの設定

こちらのdocker imageをもとにしました  
[https://hub.docker.com/r/tiangolo/nginx-rtmp/](https://hub.docker.com/r/tiangolo/nginx-rtmp/)  
[https://github.com/tiangolo/nginx-rtmp-docker](https://github.com/tiangolo/nginx-rtmp-docker)

### Dockerfile
```Dockerfile
FROM tiangolo/nginx-rtmp

COPY nginx.conf /etc/nginx/nginx.conf

WORKDIR /html/
COPY index.html /html/index.html
WORKDIR /var/www/html/output

EXPOSE 1935
```

### nginx.conf
```
# https://github.com/tiangolo/nginx-rtmp-docker/issues/18
worker_processes auto;
rtmp_auto_push on;
events {}
rtmp {
    server {
        listen 1935;
        listen [::]:1935 ipv6only=on;    
        application live {
            live on;
            record off;
            notify_method get;
            on_publish http://nginx-unit-stream-control-app:8000/publish_start_hook;
            on_publish_done http://nginx-unit-stream-control-app:8000/publish_end_hook;
            hls on;
            hls_path /var/www/html/output;
            hls_fragment 1s;
            hls_continuous on;
            hls_cleanup on;
        }
    }
}
http {
    server_tokens off;
    include mime.types;
    keepalive_timeout 65;
    server {
        listen 80;      # HTTP IPv4
        listen [::]:80; # HTTP IPv6
        location / {
            proxy_pass http://nginx-unit-stream-control-app:8000;
        }
        location /output {
            add_header Cache-Control no-cache;
            add_header 'Access-Control-Allow-Origin' '*' always;
            add_header 'Access-Control-Expose-Headers' 'Content-Length';
            if ($request_method = 'OPTIONS') {
                add_header 'Access-Control-Allow-Origin' '*';
                add_header 'Access-Control-Max-Age' 1728000;
                add_header 'Content-Type' 'text/plain charset=UTF-8';
                add_header 'Content-Length' 0;
                return 204;
            }
            types {
                application/vnd.apple.mpegurl m3u8;
                video/mp2t ts;
            }
            root /var/www/html;
        }
    }
}
```

前半の`rtmp {}`の箇所が`nginx-rtmp-module`に関わる設定になります  
後半の`http {}`はプレイリストとフラグメントの配信をする設定と、APIサーバーへのproxyの設定がされています(詳しくは`docker-compose`の箇所で説明します)  

## 配信サーバーのdocker-composeファイル
```
version: "3.9"
services:
    nginx-proxy:
        image: nginxproxy/nginx-proxy
        ports:
            - "80:80"
        expose:
            - "80"
        volumes:
            - "/var/run/docker.sock:/tmp/docker.sock:ro"
    nginx-rtmp-module:
        build: ./nginx-rtmp-module
        ports:
            - "1935:1935"
        environment:
            - VIRTUAL_HOST=stream.nkm3.org
            - VIRTUAL_PORT=80
        container_name: stream_delivery
    nginx-unit-stream-control-app:
        build: ./nginx-unit-stream-control-app
        volumes:
            - "./nginx-unit-stream-control-app/config/:/docker-entrypoint.d/"
            - "./nginx-unit-stream-control-app/log/unit.log:/var/log/unit.log"
            - "./nginx-unit-stream-control-app/state/:/var/lib/unit/"
            - "./nginx-unit-stream-control-app/webapp/:/www/"
        env_file:
            - stream-control-app.env
```
`docker-compose up`ですべて立ち上がるようにしています

- HTTPリクエストは一旦`nginx-proxy`で受けます(VIRTUAL HOSTと今後のHTTPS対応をするためです)
- indexページとHLSのフラグメントファイルは`nginx-rtmp-module`から配信されます
- APIへのリクエストは`nginx-unit-stream-control-app`から配信されます
    - ユーザーからのリクエストは`nginx-proxy`→`nginx-rtmp-module`→`nginx-unit-stream-control-app`と2段階でproxyされます
    - 配信開始、終了のwebhookリクエストは`nginx-rtmp-module`で発生するので`nginx-rtmp-module`から`nginx-unit-stream-control-app`に直接リクエストされます


#　クラウド側のサーバーについて
クラウド側のサーバーはOracle CloudがAlways freeで提供しているCompute Instance `VM.Standard.E2.1.Micro`を使っています [Oracle Cloud](https://cloud.oracle.com/)

# 終わりに
自然をなんとかと言って結局ただのライブ配信じゃないか、という話ではあるのですが、それはそれとさせてください  
実はオープンソースのソフトウェアの組み合わせて結構作れてしまうということが雰囲気だけでもお伝えできたかなと思っています
