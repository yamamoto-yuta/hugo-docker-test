# hugo-test

Docker+GitHub Pages+Hugo で静的サイト生成を検証するためのリポジトリ

## 環境構築

### 共通

リポジトリを clone して Docker イメージをビルドし、Docker コンテナを起動。

```
$ git clone <THIS REPOSITORY>
$ docker-compose up -d --build
```

### 初回のみ

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

サイトの作成。今回は `mysite` という名前で作成する。

```
$ docker-compose run --entrypoint "" --rm hugo bash -c "hugo new site mysite"
```

テーマのインストール。今回は [Hero](https://themes.gohugo.io/themes/hugo-hero-theme/) を使用した。

```
$ git init
$ git submodule add https://github.com/zerostaticthemes/hugo-hero-theme.git ./mysite/themes/hugo-hero-theme
```

`mysite/config.toml` にテーマ設定を追記。

```toml
theme = "hugo-hero-theme"
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
