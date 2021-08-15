Title: Making Flashcard app with Django REST framework, nuxtjs and Vuetify. part1
Date: 2021-08-10 00:00
Modified: 2021-08-10 00:00
Category: note
Tags: note, software
Slug: flashcard-with-django-nuxtjs-vuetify-pt1
Authors: sonkmr
Summary: Making Flashcard app with Django REST framework, nuxtjs and Vuetify. part1

## まだ書いてる途中だけどなんとなく公開
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

## 画面紹介とか
