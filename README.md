# hugo-test

Docker+GitHub Pages+Hugo で静的サイト生成を検証するためのリポジトリ

## 環境構築

リポジトリを clone して Docker イメージをビルドし、Docker コンテナを起動。

```
$ git clone <THIS REPOSITORY>
$ docker-compose up -d --build
```

## 記事の投稿

記事を作成する。今回は `test.md` という名前で作成する。

```
$ docker-compose run --entrypoint "" --rm hugo bash -c "cd mysite/ && hugo new blog/test.md"
```

すると、 `blog/` ディレクトリ内に下記の内容が記載された `test.md` が作成される。

```
+++
title = "Test"
date = 2021-12-16T12:34:44Z
tags = [""]
categories = [""]
banner = "img/banners/banner-default.jpg"
draft = false
+++

Write your article here.
```

作成されたファイルを編集して記事を執筆する。

ヘッダ部分で変更する項目及びその役割は次の通り。

- `title`
  - 記事のタイトルを入力する。
- `categories`
  - カテゴリを入力する
- `banner`
  - サムネイル画像を指定する。
  - 初期値としてデフォルト画像が指定されている。
- `draft`
  - 下書きかどうかを指定する。
  - 初期値は true。

記事が書けたらビルドする。

```
$ docker-compose run --entrypoint "" --rm hugo bash -c "cd mysite/ && hugo"
```

## サイト構築

### はじめに

サイトを 1 から作成する場合の手順を以下に示す。一度作成している場合はやらないこと。

GitHub のブランチルールと目標のディレクトリ構造を以下に示す。

GitHub のブランチルール：

- `main`
  - ビルド後のサイトのコードを管理するブランチ
  - このブランチへの push は GitHub Actions を用いて自動で行われるため弄らないこと
- `src`
  - ビルド前のソースコードを管理するブランチ
  - 基本的にこのブランチへ push していく
  - このブランチへ push すると GitHub Actions を用いて自動でビルド → `main` ブランチへの push が行われる

目標のディレクトリ構造：

```
.
├── Dockerfile
├── README.md
├── docker-compose.yml
└── mysite
    ├── archetypes
    ├── config.toml
    ├── content
    ├── data
    ├── layouts
    ├── static
    └── themes
```

### 手順

サイトの作成。今回は `mysite` という名前で作成する。

```
$ docker-compose run --entrypoint "" --rm hugo bash -c "hugo new site mysite"
```

テーマのインストールと適用。適用方法はテーマによって異なる場合があるので確認すること。今回、テーマは [Universal](https://themes.gohugo.io/themes/hugo-universal-theme/) を使用した。

```
$ git init
$ git submodule add https://github.com/devcows/hugo-universal-theme ./mysite/themes/hugo-universal-theme
```

テーマが適用できたか確認。

```
$ docker-compose run --entrypoint "" --rm hugo bash -c "cd mysite/ && hugo"
$ docker-compose run --entrypoint "" --rm hugo bash -c "cd mysite/ && hugo server"
```

## 参考記事

- [klakegg/hugo - Docker Image | Docker Hub](https://hub.docker.com/r/klakegg/hugo)
- [[Docker] Hugo を利用するための環境構築 - Qiita](https://qiita.com/ub0t0/items/4ac2f2d8c3e8fbdfcfad)
- [[Docker] Hugo でサイトを構築し、GitHub で公開 - Qiita](https://qiita.com/ub0t0/items/39b1649dffcba23517a6)
- [ベースイメージの ENTRYPOINT を無効化 - Qiita](https://qiita.com/nju33/items/733e16511f3b8e739d54)
- [Hugo + GitHub Pages / Actions でブログを公開する](https://zenn.dev/bryutus/articles/hugo-github-pages-actions)
- [ShotaroKataoka/ShotaroKataoka.github.io: My web page.](https://github.com/ShotaroKataoka/ShotaroKataoka.github.io)
- [gitignore/Hugo.gitignore at main · github/gitignore](https://github.com/github/gitignore/blob/main/community/Golang/Hugo.gitignore)
- [GitHub Actions でワークフロー中に発生した差分を Push する](https://zenn.dev/lollipop_onl/articles/eoz-gha-push-diffs)
