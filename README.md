# hugo-test

Docker+GitHub Pages+Hugo で静的サイト生成を検証するためのリポジトリ

## 環境構築

リポジトリを clone して Docker イメージをビルドし、Docker コンテナを起動。

```
$ git clone <THIS REPOSITORY>
$ docker-compose up -d --build
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
- [Hugo + GitHub Pages / Actions でブログを公開する](https://zenn.dev/bryutus/articles/hugo-github-pages-actions)
- [ShotaroKataoka/ShotaroKataoka.github.io: My web page.](https://github.com/ShotaroKataoka/ShotaroKataoka.github.io)
- [gitignore/Hugo.gitignore at main · github/gitignore](https://github.com/github/gitignore/blob/main/community/Golang/Hugo.gitignore)
