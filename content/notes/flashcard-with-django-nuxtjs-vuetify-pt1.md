Title: Making Flashcard app with Django REST framework, nuxtjs and Vuetify. part1
Date: 2021-08-11 00:00
Modified: 2021-08-11 00:00
Category: note
Tags: note, software
Slug: flashcard-with-django-nuxtjs-vuetify-pt1
Authors: sonkmr
Summary: Making Flashcard app with Django REST framework, nuxtjs and Vuetify.


## これはなに

- Django REST frameworkとnuxtjs、Vuetifyで作った単語カード風アプリ
- nuxtjsとVuetifyを使ってみたくて作りはじめた
- ソースコードのレポジトリ https://github.com/sonkm3/wordbook

## 想定していた完成形

- ユーザーは複数の単語帳を作れる
- 単語帳には単語を登録できる
- 単語のフィールドは単語と発音、ヒント、説明を登録できる
- 単語カード画面ではランダムに単語が表示される
- 単語カード画面には単語、発音、ヒントが表示され、裏返す的な操作をすると説明が見られる
- メールアドレスでログインできる
- 認証は一旦Token認証で割り切る


## 実装内容

実装内容は大きく2種類  

- リスト表示とそれぞれの項目のCRUD処理
    - 単語帳
    - 単語のリスト表示とCRUD処理
- 単語カード画面の表示

## 構成
- バックエンド
    - Django https://www.djangoproject.com
    - Django REST framework https://www.django-rest-framework.org
    - djoser https://github.com/sunscrapers/djoser
    - Django Filter https://github.com/carltongibson/django-filter/tree/main
    - drf-nested-routers https://github.com/alanjds/drf-nested-routers
    - django-cors-headers https://github.com/adamchainz/django-cors-headers

- フロントエンド
    - NuxtJS https://nuxtjs.org
    - Vuetify https://vuetifyjs.com/en/

## バックエンドの実装
### modelの実装
https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/app/models.py

- `django REST framework`の`ModelViewSet`と`ModelSerializer`から使うためデフォルトのクエリセット以外に処理を書く必要がない
- `models.Manager`クラスを使うことでクエリに関わる実装を少なくする
    - 単語帳に紐づいた単語を取得するクエリセットを返すメソッドを`WordManager`クラスに用意し
    - `viewWordViewSet`の`get_queryset`から`Word.objects.course()`と呼び出すとフィルタされたクエリセットが返ってくる
    - このクエリセットにページネーションやソートのクエリが加わっていく

### serializerの実装
https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/app/serializers.py

- `django REST framework`の`ModelViewSet`から使う想定
- `serializers.ModelSerializer`を使うので書き足した箇所はバリデーションぐらい
- 単語帳の持ち主とユーザーが一致するかのバリデーションはSerializerのバリデーションでおこなっている
    - 例えば`validate_courseメソッド`でおこなえ、`course`フィールドは`_course`のようにすることで指定できる


### viewの実装
https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/app/views.py

- `django REST framework`の`ModelViewSet`を使っているのであまり書かなくてよいが`drf-nested-routers`に関わる実装は必要
- `drf-nested-routers`に関わる実装について
    - `courses/{course_id}/words/`というパスにしたかったので`drf-nested-routers`を導入した
    - この場合`course_id`は`self.kwargs["course_pk"]`としてviewにわたってくる
    - `request.data`には入っていないので`create`メソッドをオーバーライドして`request.data`に`course_pk`を追加している
- `pagination`について
    - フロントエンドの作りに合わせて`PageNumberPagination`をもとにした`CustomPagination`を作った

### ルーティング
https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/wordbook/urls.py

- `NestedSimpleRouter`を使って`courses/{course_id}/words/`を実現している


### emailでのログインについて
https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/app/models.py#L9-L51

- `CustomUser`と`CustomUserManager`を作って対応
- `create_user`に関わる処理の変更を`CustomUserManager`でオーバーライドする
- `AbstractUser`を継承しているので`username`の条件は`CustomUser`でオーバーライドできる
- CustomUserはAbstractModelを継承しているのでfirst/last_nameなどの使わないフィールドは`Null`を代入することで削除できる


https://github.com/sonkm3/wordbook/blob/main/wordbook-backend/wordbook/settings.py

- CustomUserクラスとemailフィールドをログイン時に使うようにする変更は`settings.py`でおこなう
    - `AUTH_USER_MODEL`を上で定義した`CustomUser`に設定(Djangoが使うユーザーモデルを変更する設定)
    - `DJOSER`の`LOGIN_FIELD`を`email`に設定(djoserのユーザー名フィールドを変更する設定)
